-- Table: vehicle.vehicle_services

-- DROP TABLE vehicle.vehicle_services;

CREATE TABLE IF NOT EXISTS vehicle.vehicle_services
(
	_id				    BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (MINVALUE 1 START WITH 1 CACHE 1),
	services	   		CHARACTER VARYING(50) NOT NULL,
	cost				BIGINT NOT NULL
)
TABLESPACE pg_default;

ALTER TABLE vehicle.vehicle_services
	OWNER to vehicle_repair;

