# Movie Recommendation System

## About
A simple movie recommendation system developed using Python and Pandas. The system recommends movies based on the user's preferred genre, language, and minimum rating.

## Features
- Takes genre, language, and minimum rating from the user
- Allows the user to set the importance of each preference
- Calculates a similarity score for each movie
- Sorts movies based on their scores
- Displays the top 3 movie recommendations
- Uses a CSV dataset

## Dataset
The dataset contains:
- Movie
- Genre
- Language
- Rating

## Technologies Used
- Python
- Pandas
- CSV
- Recommendation Logic

## How It Works

1. The movie dataset is loaded using Pandas.
2. The user enters their preferred genre, language, and minimum rating.
3. The user gives an importance value from 1 to 5 for each preference.
4. The program checks every movie against these preferences.
5. A similarity score is calculated for each movie.
6. Movies are sorted from the highest score to the lowest score.
7. The top 3 movies are displayed as recommendations.

## Recommendation Logic

The score is calculated using the user's preference weights:

- Matching genre → adds `genre_weight`
- Matching language → adds `language_weight`
- Movie rating meeting the minimum rating → adds `rating_weight`

The movie with the highest matching score gets a higher recommendation.

## Learning Outcome
This project helped me understand Pandas, CSV data handling, user preferences, scoring logic, sorting, and basic recommendation systems.
