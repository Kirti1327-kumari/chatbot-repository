'''
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
def load_dataset(path):
    with open(path, 'r') as file:
        return json.load(file)['data']

# Prepare data for training
def prepare_data(data):
    questions = [item['question'] for item in data]
    answers = [item['answer'] for item in data]
    return questions, answers

# Train the model
def train_model(dataset_path):
    data = load_dataset(dataset_path)
    questions, answers = prepare_data(data)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(questions)
    model = LogisticRegression()
    model.fit(X, answers)

    # Save the model and vectorizer
    joblib.dump(model, 'chatbot_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

if __name__ == "__main__":
    train_model('dataset.json')'''


import json  # Import the JSON module to work with JSON data files
from sklearn.feature_extraction.text import TfidfVectorizer  # Import the TfidfVectorizer for converting text to numerical form
from sklearn.linear_model import LogisticRegression  # Import Logistic Regression model for classification
import joblib  # Import joblib to save and load machine learning models

# Load dataset from a JSON file
def load_dataset(path):
    with open(path, 'r') as file:
        # Read the JSON file and return the 'data' part (list of questions and answers)
        return json.load(file)['data']

# Prepare the data for training by separating questions and answers
def prepare_data(data):
    # Extract all questions from the dataset and store them in a list
    questions = [item['question'] for item in data]
    # Extract all answers from the dataset and store them in a list
    answers = [item['answer'] for item in data]
    return questions, answers

# Train the chatbot model using the dataset
def train_model(dataset_path):
    # Load the dataset from the given path
    data = load_dataset(dataset_path)
    # Prepare the questions and answers
    questions, answers = prepare_data(data)

    # Initialize the TfidfVectorizer, which converts text data into numerical vectors based on term frequency and inverse document frequency
    vectorizer = TfidfVectorizer()
    # Fit and transform the questions into numerical vectors
    X = vectorizer.fit_transform(questions)

    # Initialize the Logistic Regression model (a type of classifier)
    model = LogisticRegression()
    # Train the model using the transformed questions (X) and their corresponding answers
    model.fit(X, answers)

    # Save the trained model and vectorizer to disk so they can be reused later
    joblib.dump(model, 'chatbot_model.pkl')  # Save the trained model
    joblib.dump(vectorizer, 'vectorizer.pkl')  # Save the vectorizer

# Main entry point to train the model
if __name__ == "__main__":
    # Train the model using the dataset 'dataset.json'
    train_model('dataset.json')

