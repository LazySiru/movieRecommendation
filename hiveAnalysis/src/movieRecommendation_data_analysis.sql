-- Distribution of the counts per rating
CREATE TABLE ratings_distribution AS
SELECT rating, COUNT(*) as count
FROM ratings
GROUP BY rating;

-- Distribution of each movie's total count of ratings
-- Heavily skewed to small number of famous movies
CREATE TABLE rating_count_sorted AS
SELECT movie_id, COUNT(rating) AS rating_count
FROM ratings
GROUP BY movie_id
ORDER BY rating_count DESC;

-- Distribution of user's gender
-- Heavily sckewed to males
CREATE TABLE user_gender_distribution AS
SELECT gender, COUNT(uid) AS count
FROM users
GROUP BY gender;

-- Distribution of user's occupation
CREATE TABLE user_occupation_distribution AS
SELECT occupation, COUNT(uid) AS count
FROM users
GROUP BY occupation;