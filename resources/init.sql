CREATE SCHEMA got
    AUTHORIZATION postgres;

CREATE TABLE got.greenhouse
(
    id SERIAL PRIMARY KEY,
    "timestamp" date NOT NULL,
    temperature real,
    humidity real,
    moisture real,
    sun_intensity real
);

ALTER TABLE got.greenhouse
    OWNER to postgres;
