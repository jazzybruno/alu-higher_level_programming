-- Converts the database hbtn_0c_0, first_table and its name field to UTF8
-- Converts the database default character set and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Selects the database to convert its table
USE hbtn_0c_0;
-- Converts first_table and its text fields, including name
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
