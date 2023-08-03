-- Table: vehicle.customer_details

-- DROP TABLE vehicle.customer_details;

CREATE TABLE IF NOT EXISTS vehicle.customer_details
(
	vehicle_id			BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (MINVALUE 1 START WITH 1 CACHE 1),
	vehicle_number	    CHARACTER VARYING(200) NOT NULL,
	vehicle_type			BIGINT NOT NULL,
	vehicle_model_number CHARACTER VARYING(200) NOT NULL,
	vehicle_owner_name	CHARACTER VARYING(50) NOT NULL,
	phone_number	 	BIGINT NOT NULL,
	date_of_service		DATE NOT NULL
)
TABLESPACE pg_default;

ALTER TABLE vehicle.customer_details
	OWNER to vehicle_repair;
