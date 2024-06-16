--Creates new database 
CREATE DATABASE IF NOT EXISTS movies;

--Use database
USE movies;

--Creates movies table
CREATE TABLE movies_tmp
(movie_id INT,
e1 STRING, --Don't like this part but need because of '::' delimiter for right now
title INT,
e2 STRING, --Don't like this part but need because of '::' delimiter for right now
genres STRING
)

ROW FORMAT DELIMITED
FIELDS TERMINATED BY '::'
STORED AS TEXTFILE;

--Loads data from local data file
LOAD DATA LOCAl INPATH './movies.dat' 
INTO TABLE movies_tmp;

--Get metadata of table
DESCRIBE movies_tmp;

--Create movies table
CREATE TABLE movies AS
SELECT movie_id, title, genres
FROM movies_tmp;

--Drop movies_tmp table
DROP TABLE movies_tmp;
