"""
Script to get everything to work quick and dirty.
"""

import json
from contextlib import contextmanager
from time import sleep
from typing import Dict

from garden.auxiliary.connections import Listener
from garden.auxiliary.logging import get_logger
from garden.database import Greenhouse, Session


class Server:
    """
    GoT server class that awaits mqtt messages from clients and processes them.
    """

    def __init__(self, ip: str, port: int, topic: str):
        """
        Initialize class and setup properties as well as listener.
        :param ip: address of mqtt broker.
        :param port: port of mqtt broker.
        :param topic: topic to listen to.
        """
        self.logger = get_logger(self.__class__.__name__)
        self.listener = Listener(
            ip=ip, port=port, topic=topic, on_message=self._on_message
        )
        self.buffer = []
        self.running = True
        self._run()

    def _on_message(self, client, userdata, msg):
        """
        Define what to do when message is received.
        """
        self.buffer.append(json.loads(msg.payload.decode()))

    def _run(self):
        """
        Define the main run method of this class.
        """
        try:
            while self.running:
                sleep(1)
                print(f"Buffersize is {len(self.buffer)}")
                self._process_buffer()
        except Exception:
            self.listener.disconnect()
            self.logger.error("run loop was broken.", exc_info=True)

    def _process_buffer(self):
        """
        Define what to do with buffer content.
        """
        try:
            while content := self.buffer.pop(0):
                with self._session_scope() as session:
                    self._add_content(content=content, session=session)
        except IndexError as _:
            return

    @contextmanager
    def _session_scope(self):
        """
        Use the previously defined session_maker to create a database session and yield it to the process.
        In case something goes wrong, rescue the current content.
        """
        session = Session()
        try:
            yield session
            session.commit()
        except Exception:
            self.logger.error("Something went wrong. Rolling back now.", exc_info=True)
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def _add_content(content: Dict, session: Session):
        """
        Add current content to the session.
        :param content: Content to fill classes with that will be written to database.
        :param session: Current session with target database.
        """
        session.add(Greenhouse(**content))


if __name__ == "__main__":
    s = Server(ip="test.mosquitto.org", port=1883, topic="sffrenzy")
