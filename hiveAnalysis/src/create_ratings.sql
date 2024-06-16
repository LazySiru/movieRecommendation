CREATE DATABASE IF NOT EXISTS movies;

USE movies;

CREATE TABLE IF NOT EXISTS ratings_tmp (
    uid INT,
    temp1 STRING, -- Temporary field due to :: delimiter handling error
    movie_id INT,
    temp2 STRING, -- Temporary field due to :: delimiter handling error
    rating INT,
    temp3 STRING, -- Temporary field due to :: delimiter handling error
    ts BIGINT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '::'
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH './ratings.dat' 
INTO TABLE ratings_tmp;

CREATE TABLE IF NOT EXISTS ratings AS
SELECT
    uid,
    movie_id, 
    rating, 
    ts
FROM ratings_tmp;

DROP TABLE IF EXISTS ratings_tmp;