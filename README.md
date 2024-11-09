# Movie Recommendation System

This project presents a comprehensive movie recommendation system that integrates various machine learning models and big data processing techniques to deliver personalized movie suggestions.

## Features

- **Content-Based Filtering**: Implemented a K-Nearest Neighbors (KNN) model utilizing semantic analysis to recommend movies based on content similarity.
- **Collaborative Filtering**: Developed both KNN and Singular Value Decomposition (SVD) models to suggest movies by analyzing user-item interactions.
- **Hybrid Recommendation Model**: Combined content-based and collaborative filtering approaches to enhance recommendation accuracy.
- **RESTful API Deployment**: Deployed the recommendation models via a REST API using Flask, hosted on AWS cloud infrastructure for scalability and accessibility.

## Data Processing and Analysis

- **Big Data Handling**: Utilized Hadoop and Spark frameworks for efficient processing and exploratory data analysis (EDA) of the MovieLens dataset, comprising over 1 million entries.
- **Data Visualization**: Employed Python libraries to visualize data insights, aiding in understanding user preferences and movie trends.
- **Text Processing**: Implemented Term Frequency-Inverse Document Frequency (TF-IDF) vectorization for word embedding, facilitating semantic analysis in content-based filtering.

## Repository Structure

- **`dataVisualization/`**: Contains scripts and notebooks for data visualization and exploratory data analysis.
- **`hiveAnalysis/`**: Includes Hive scripts for data querying and processing within the Hadoop ecosystem.
- **`recommendationSystem/`**: Houses the implementation of recommendation models and the Flask API code.
