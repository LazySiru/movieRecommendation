--Creates new database 
CREATE DATABASE IF NOT EXISTS movies;

--Use database
USE movies;

--Creates ratings table
CREATE TABLE ratings_tmp
(uid INT,
e1 STRING, --Don't like this part but need because of '::' delimiter for right now
movie_id INT,
e2 STRING, --Don't like this part but need because of '::' delimiter for right now
rating INT,
e3 STRING, --Don't like this part but need because of '::' delimiter for right now
ts BIGINT
)

ROW FORMAT DELIMITED
FIELDS TERMINATED BY '::'
STORED AS TEXTFILE;

--Loads data from local data file
LOAD DATA LOCAl INPATH './ratings.dat' 
INTO TABLE ratings_tmp;

--Get metadata of table
DESCRIBE ratings_tmp;

--Create ratings table
CREATE TABLE ratings AS
SELECT uid, movie_id, rating, ts
FROM ratings_tmp;

--Drop ratings_tmp table
DROP TABLE ratings_tmp;
