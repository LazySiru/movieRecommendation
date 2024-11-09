# Movie Recommendation System
This project presents a movie recommendation system that integrates big data processing techniques for data processing and various machine learning models to predict and recommend movies to users. 


#### Table of Contents
- [Repository Structure](#repository-structure)
- [Features](#features)
- [Results](#result)
- [API reference](#api-reference)
- [References](#references)

---
## Repository Structure
```
./
|- dataVisualization/: Contains scripts and notebooks for data visualization and exploratory data analysis.
|- hiveAnalysis/: Includes Hive scripts for data querying and processing within the Hadoop ecosystem.
|- recommendationSystem/: Houses the implementation of recommendation models and the Flask API code.
```

## Features
#### Data Processing and Analysis
- **Big Data Processing**: Utilized Hadoop and Spark frameworks for efficient processing and exploratory data analysis (EDA) of the MovieLens dataset, comprising 1M+ entries.
- **Data Visualization**: Employed Python libraries to visualize data insights, aiding in understanding user preferences and movie trends.
- **Text Processing**: Implemented Term Frequency-Inverse Document Frequency (TF-IDF) vectorization for word embedding, facilitating semantic analysis in content-based filtering.

#### Recommendation models
- **Content-Based Filtering**: Implemented a K-Nearest Neighbors (KNN) model utilizing semantic analysis to recommend movies based on content similarity.
- **Collaborative Filtering**: Developed both KNN and Singular Value Decomposition (SVD) models to suggest movies by analyzing user-item interactions.
- **Hybrid Recommendation Model**: Combined content-based and collaborative filtering approaches to enhance recommendation accuracy.
- **RESTful API Deployment**: Deployed the recommendation models via a REST API using Flask, hosted on AWS cloud infrastructure for scalability and accessibility.


## Results
Refer to the below documents for detailed results:
- [data analysis results](./recommendationSystem/Data%20and%20Sampling.ipynb)
- [content based recommendation model](./recommendationSystem/Content%20Based%20Recommendation.ipynb)
- [collaborative filtering model (KNN)](./recommendationSystem/KNN.ipynb)
- [collaborative filtering model (SVD)](./recommendationSystem/SVD%20Recommendation%20System.ipynb)

In summary, we were able to both achieve RMSE of below <1.0 for our predictions of user ratings for a movie. 
Using the prediction algorithm, we wrapped the models into a REST API using Flask library.


## API reference
The API by default both receives post requests and responds in JSON format.

For content based recommendationmodel, give any movie name existing in movie lens dataset in field `movie_name`. The content based model has a neat feature that will attempt to fix wrong user input to the most similar movie name:
```sh
$ curl -X POST -d '{"movie_name": "oy Story"}' https://<host>/recommend/cb_model
```
```json
{
    "prediction": [
        "Toy Story (1995)",
        "Toy Story 2 (1999)",
        "Balto (1995)",
        "Bug's Life, A (1998)",
        "King and I, The (1999)",
        "Tarzan (1999)"
    ]
}
```
<br/>

For collaborative filtering based recommendation using KNN model give any user id that exists in movie lens dataset in field `user_id`:
```sh
$ curl -X POST -d '{"user_id": 1024}' https://<host>/recommend/knn_model
```
```json
{
    "recommendations": [
        "Eaten Alive (1976)",
        "Yankee Zulu (1994)",
        "Roula (1995)",
        "Follow the Bitch (1998)",
        "Ulysses (Ulisse) (1954)"
    ]
}
```
<br/>

Collaborative filtering using SVD model takes in same input as KNN model:
```sh
$ curl -X POST -d '{"user_id": 2038}' https://<host>/recommend/svd_model
```
```json
{
    "recommendations": [
        "For All Mankind (1989)",
        "Sanjuro (1962)",
        "I Am Cuba (Soy Cuba/Ya Kuba) (1964)",
        "Lamerica (1994)",
        "Apple, The (Sib) (1998)"
    ]
}
```


## References
- [Movie Lens dataset](https://grouplens.org/datasets/movielens/)
- [Medium: complete guide to recommendation system](https://towardsdatascience.com/a-complete-guide-to-recommender-system-tutorial-with-sklearn-surprise-keras-recommender-5e52e8ceace1)
- [Medium: machine learning for recommendation systems](https://medium.com/recombee-blog/machine-learning-for-recommender-systems-part-1-algorithms-evaluation-and-cold-start-6f696683d0ed)
- [KNN mecommender system for movie recommendation](https://www.analyticsvidhya.com/blog/2020/08/recommendation-system-k-nearest-neighbors/)
- [Building a content-based recommendation system](https://www.analyticsvidhya.com/blog/2022/08/building-a-content-based-recommendation-system/)
- [Cosine similarity - understanding the math and how it works](https://www.machinelearningplus.com/nlp/cosine-similarity/?utm_content=cmp-true)


---
## Contributors
- [Sung J. Kim](https://github.com/SungJKK)
- [Kidong Kim](https://github.com/LazySiru)
