-- Creates user_0d_1 with all privileges on the server
-- Creates the user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grants every privilege on every database
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
