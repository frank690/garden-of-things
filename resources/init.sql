CREATE TABLE garden-of-things.garden
(
    id SERIAL PRIMARY KEY,
    "timestamp" text NOT NULL,
    temperature real,
    humidity real,
    moisture real,
    sun_intensity real
);

ALTER TABLE garden-of-things.garden
    OWNER to postgres;
