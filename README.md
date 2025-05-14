This project is a simple chatbot built using Python and Flask. The chatbot is trained on a custom question-answer dataset and can generate appropriate responses to user input via a web interface.

🧾 Files in Project
app.py – Flask app with embedded HTML (no separate HTML file)
train_model.py – Trains and saves the model
chatbot_model.pkl – Trained ML model
vectorizer.pkl – Text vectorizer for transforming inputs
dataset.json – Custom dataset with question-answer pairs
equirements.txt – All dependencies

🚀 How to Run
Install Python packages
pip install -r requirements.txt

Train the model
python train_model.py

Start the chatbot server
python app.py

Use the chatbot
Open your browser and go to:
http://127.0.0.1:5000
You will see the chat interface directly loaded from app.py.

