
import json  # Importing the json module to work with JSON data files
import random  # Importing random module (though not used in this code, but could be useful for future extensions)

class Chatbot:
    # Constructor method that initializes the chatbot object.
    # Takes the path to the dataset file and loads it using the `load_dataset` method.
    def __init__(self, dataset_path):
        # Loading the dataset from the provided file path and storing it in `self.dataset`
        self.dataset = self.load_dataset(dataset_path)

    # This method loads the dataset from the given JSON file path.
    # The dataset is expected to be a JSON file where the questions and answers are inside a 'data' key.
    def load_dataset(self, path):
        with open(path, 'r') as file:
            # Reading the JSON file and returning the 'data' part (list of questions and answers).
            return json.load(file)['data']

    # This method receives the user's input and attempts to find a matching answer from the dataset.
    # It checks if any question in the dataset contains the user's input (case-insensitive match).
    def get_response(self, user_input):
        for item in self.dataset:
            # If the user's input (in lowercase) is found in the question (also converted to lowercase), return the answer.
            if user_input.lower() in item['question'].lower():
                return item['answer']
        # If no match is found, return a default message.
        return "I'm sorry, I don't understand that."

# Example usage of the Chatbot class:
if __name__ == "__main__":
    # Creating an instance of the Chatbot class by passing the dataset file path
    chatbot = Chatbot('dataset.json')

    # Taking user input from the console
    user_input = input("You: ")

    # Getting the chatbot's response to the user's input
    response = chatbot.get_response(user_input)

    # Printing the chatbot's response
    print("Chatbot:", response)

