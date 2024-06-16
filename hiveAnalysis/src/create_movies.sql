CREATE DATABASE IF NOT EXISTS movies;

USE movies;

CREATE TABLE IF NOT EXISTS movies_tmp (
    movie_id INT,
    temp1 STRING, -- Temporary field due to :: delimiter handling error
    title STRING,
    temp2 STRING, -- Temporary field due to :: delimiter handling error
    genres STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '::'
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH './movies.dat' 
INTO TABLE movies_tmp;

CREATE TABLE IF NOT EXISTS movies AS
SELECT 
    movie_id, 
    title, 
    genres
FROM movies_tmp;

DROP TABLE IF EXISTS movies_tmp;
