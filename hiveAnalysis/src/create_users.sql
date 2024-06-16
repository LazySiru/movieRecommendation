CREATE DATABASE IF NOT EXISTS movies;

USE movies;

CREATE TABLE IF NOT EXISTS users_tmp (
    uid INT,
    temp1 STRING, -- Temporary field due to :: delimiter handling error
    gender STRING,
    temp2 STRING, -- Temporary field due to :: delimiter handling error
    age INT,
    temp3 STRING, -- Temporary field due to :: delimiter handling error
    occupation INT,
    temp4 STRING, -- Temporary field due to :: delimiter handling error
    zipcode STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '::'
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH './users.dat' 
INTO TABLE users_tmp;

CREATE TABLE IF NOT EXISTS users AS
SELECT
    uid,
    gender, 
    age, 
    occupation,
    zipcode
FROM users_tmp;

DROP TABLE IF EXISTS users_tmp;