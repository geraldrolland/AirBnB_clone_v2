-- Creates a MySQL server with
--   Database hbnb_test_db
--   User hbnb_test with pwd hbnb_test_pwd in localhost
--   Grant ALL PRIVILEGES TO user hbnb_test  on hbnb_test_db
--   Grant SELECT PRIVILEGE on performance_schema
--   If db hbnb_test_db or USER hbnb_test already exists, script shld not fail

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILIGES
    ON `hbnb_test_db`.*
    TO 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;
