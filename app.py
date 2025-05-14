
from flask import Flask, request, jsonify, render_template_string  # Import necessary modules from Flask
import joblib  # Import joblib for loading pre-trained models
import numpy as np  # Import NumPy (though not used in this code, it could be useful for future data manipulation)

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and vectorizer
try:
    # Attempt to load the model and vectorizer from disk using joblib
    model = joblib.load('chatbot_model.pkl')  # Load the pre-trained model
    vectorizer = joblib.load('vectorizer.pkl')  # Load the vectorizer used to transform user input
except Exception as e:
    # If an error occurs while loading the model or vectorizer, print the error message
    print("Error loading model or vectorizer:", e)

# HTML + CSS + JS for the web-based chatbot interface
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Chatbot</title>
    <style>
        /* Styling for the webpage */
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            padding: 40px;
        }
        .chatbox {
            background: white;
            width: 400px;
            margin: 0 auto;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
            color: #333;
        }
        input[type="text"] {
            width: calc(100% - 90px);
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            width: 70px;
            padding: 10px;
            background: #007BFF;
            border: none;
            color: white;
            border-radius: 5px;
            cursor: pointer;
            margin-left: 10px;
        }
        button:hover {
            background: #0056b3;
        }
        #response {
            margin-top: 20px;
            padding: 10px;
            background: #e9e9e9;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="chatbox">
        <h2>Chat with Bot</h2>
        <div>
            <!-- Input field for user message and send button -->
            <input type="text" id="userInput" placeholder="Type your message...">
            <button onclick="sendMessage()">Send</button>
        </div>
        <!-- Area to display bot's response -->
        <div id="response"></div>
    </div>

    <script>
        // Function to handle sending user message and receiving chatbot's response
        function sendMessage() {
            const message = document.getElementById("userInput").value;  // Get user input from the text box
            fetch("/chat", {
                method: "POST",  // Send POST request to the server with user message
                headers: {
                    "Content-Type": "application/json"  // Set content type as JSON
                },
                body: JSON.stringify({ message: message })  // Send the message as JSON in the body
            })
            .then(response => response.json())  // Parse the JSON response from the server
            .then(data => {
                // Display the bot's response or an error message if available
                document.getElementById("response").innerText = "Bot: " + (data.response || data.error);
            })
            .catch(error => {
                // Handle any errors that occur during the request
                document.getElementById("response").innerText = "Error: " + error;
            });
        }
    </script>
</body>
</html>
'''

# Home route to render the chatbot interface (HTML page)
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)  # Render the HTML template as a string (to be displayed in the browser)

# Chat route to handle communication between the user and the chatbot
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    try:
        if request.method == 'POST':  # Check if it's a POST request (when user sends a message)
            user_input = request.json.get('message')  # Extract the user message from the JSON body
            if not user_input:
                return jsonify({"error": "No message provided"}), 400  # Return an error if no message is provided

            # Transform the user's input using the vectorizer (convert it to the model's required format)
            input_vector = vectorizer.transform([user_input])

            # Predict the chatbot's response using the pre-trained model
            response = model.predict(input_vector)

            # Return the chatbot's response as JSON
            return jsonify({"response": response[0]})
        else:
            # If the request is not POST (e.g., GET request), return an informative message
            return jsonify({"message": "Use POST request to talk to the chatbot."})
    except Exception as e:
        # Return an error response if any exception occurs during the chat request
        return jsonify({"error": str(e)}), 500

# Run the Flask application on the local server
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development (shows detailed error messages)




