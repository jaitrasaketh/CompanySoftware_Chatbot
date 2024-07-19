from flask import Flask, request, jsonify, render_template
from query_data import query_rag  # Ensure this function processes the chatbot's response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = query_rag(user_message)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)