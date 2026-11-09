-- Creates the table unique_id whose id defaults to 1 and is unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
