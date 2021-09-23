# garden-of-things
[![Coverage Status](https://coveralls.io/repos/github/frank690/garden-of-things/badge.svg?branch=main)](https://coveralls.io/github/frank690/garden-of-things?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)


I like to be in the garden, but I also like to tinker and code.
This project is meant to combine both and turn my garden into a weird IoT version: the garden-of-things (GoT).
Let us hope that this projects starts off as well as the show but continues steadily instead of ending in a catastrophy.

## Hardware
What hardware is used and how is it set up?

### Client(s)
One (or possibly multiple) esp32 units that are equipped with various sensors
(to measure e.g. temperature, sun intensity, humidity, ...). The measured values are streamed via MQTT to a home server (e.g. a raspberry pi).
The PCB board design can be found [ħere](./resources/client_pcb_board.brd).

<table>
  <tr>
    <td>
      <img src="./resources/pcb_board_front.png" alt="pcb board front" width="200"/> 
    </td>  
    <td>
      <img src="./resources/pcb_board_back.png" alt="pcb board back" width="200"/>
    </td>
  </tr>
</table>

### Server
A raspberry pi that has a [mosquitto mqtt broker](https://mosquitto.org/) running on it but also listens for incoming data of the client.
Once data is received, it is processed and put into a local postgres database.
The data in said database is then visualized in graphs (e.g. by using grafana, kibana or something DIY).
I also aim to make this dashboard publicly available by using some DynDNS routing.

## What is currently going on?
Check out the [CHANGELOG.md](./CHANGELOG.md) to see what is done and planned for the future.
<<<<<<< HEAD

## Notes
- Using the client code for the esp32 depends on the following repositories to be installed beforehand:
    - https://github.com/beegee-tokyo/DHTesp (for reading the DHT humidity sensor)
