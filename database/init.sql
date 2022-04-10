CREATE DATABASE IF NOT EXISTS energy;

USE energy;

CREATE TABLE IF NOT EXISTS energy (
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    hour INTEGER NOT NULL,
    minute INTEGER NOT NULL,
	gas FLOAT,
	high_produces FLOAT,
	low_produced FLOAT,
	high_consumed FLOAT,
	low_consumed FLOAT,
	ppv_produced FLOAT,
	primary key (year, month, day, hour, minute)
)  ENGINE=INNODB;
