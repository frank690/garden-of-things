CREATE TABLE greenhouse.greenhouse
(
    id SERIAL PRIMARY KEY,
    "timestamp" text NOT NULL,
    temperature real,
    humidity real,
    moisture real,
    sun_intensity real
);

ALTER TABLE greenhouse.greenhouse
    OWNER to postgres;
