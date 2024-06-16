--check distribution of rating_count per rating
CREATE TABLE ratings_distribution AS
SELECT rating, COUNT(*) as count
FROM ratings
GROUP BY rating;


--check distribution of ratings_count per movie
--movie ratings are heavily skewed
CREATE TABLE rating_count_sorted AS
SELECT movie_id, COUNT(rating) AS rating_count
FROM ratings
GROUP BY movie_id
ORDER BY rating_count DESC;


--check distribution of user's gender
--heavily sckewed to males
CREATE TABLE user_gender_distribution AS
SELECT gender, COUNT(uid) AS count
FROM users
GROUP BY gender;

--check user distribution by occupation
CREATE TABLE user_occupation_distribution AS
SELECT occupation, COUNT(uid) AS count
FROM users
GROUP BY occupation;