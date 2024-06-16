--Creates new database 
CREATE DATABASE IF NOT EXISTS movies;

--Use database
USE movies;

--Creates users_tmp table
CREATE TABLE users_tmp
(uid INT,
e1 STRING, --Don't like this part but need because of '::' delimiter for right now
gender STRING,
e2 STRING, --Don't like this part but need because of '::' delimiter for right now
age INT,
e3 STRING, --Don't like this part but need because of '::' delimiter for right now
occupation INT,
e4 STRING, --Don't like this part but need because of '::' delimiter for right now
zipcode STRING
)

ROW FORMAT DELIMITED
FIELDS TERMINATED BY '::'
STORED AS TEXTFILE;

--Loads data from local data file
LOAD DATA LOCAl INPATH './users.dat' 
INTO TABLE users_tmp;

--Get metadata of table
DESCRIBE users_tmp;

--Create ratings table
CREATE TABLE users AS
SELECT uid, gender, age, occupation, zipcode
FROM users_tmp;

--Drop users_tmp table
DROP TABLE users_tmp;