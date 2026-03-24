#Project Description

This is a Python-based command-line application developed to recommend movies to users based on their preferences. The system suggests similar movies by analyzing their genres using basic machine learning techniques.
It uses a content-based filtering approach, where movies are compared with each other based on their features (genres). The system converts text data into numerical form and calculates similarity scores to recommend the most relevant movies.


#Features
Content-Based Recommendation: Suggests movies similar to the input movie
Data Handling: Uses a CSV file to store movie data
Case-Insensitive Search: Accepts input in any format (e.g., titanic, Titanic)
Fast Processing: Instantly generates recommendations
CLI-Based Interface: Simple and easy-to-use command-line interaction


Tech Stack
Language: Python 3.x
Libraries:
pandas
scikit-learn


#How to Run
Ensure Python is installed on your system

1. Install required libraries:

pip install pandas scikit-learn
Open terminal in the project folder

2 .Run the command:

python main.py
Enter a movie name when prompted


#Project Structure
main.py: Main program (user interaction)
recommender.py: Recommendation logic
movies.csv: Dataset file containing movie details


#Conclusion 
This project demonstrates the basic concepts of machine learning such as data preprocessing, feature extraction, and similarity measurement. It provides a simple understanding of how recommendation systems work in real-world applications like streaming platforms.


