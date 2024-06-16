--Creates new database 
CREATE DATABASE IF NOT EXISTS movies;

--Use database
USE movies;

--Creates occupation table
CREATE TABLE occupation
(id INT,
occupation STRING,
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

--Loads data from local data file
LOAD DATA LOCAl INPATH './occupation.csv' 
INTO TABLE occupation;

--Get metadata of table
DESCRIBE occupation;
