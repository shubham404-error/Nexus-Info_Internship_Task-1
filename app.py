import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

conversation_history = []


@app.route('/message', methods=['POST'])
def handle_message():
    """
    Handles incoming messages and generates appropriate responses.

    Returns:
        A JSON response containing the generated message.
    """
    message = request.json['message']
    conversation_history.append(message)
    if message == 'Hi':
        response = 'Hello, how can I assist you today?'
    elif message == 'hi':
        response = 'Hello, how can I assist you today?'
    elif message == 'How are you?':
        response = 'I am a chatbot, I do not have feelings, but thank you for asking.'
    elif message == 'What is your name?':
        response = 'My name is Chatbot, nice to meet you!'
    elif message == 'Bye':
        response = 'Goodbye, have a great day!'
    elif message == 'bye':
        response = 'Goodbye, have a great day!'
    elif message == 'What time is it':
        response = datetime.datetime.now().strftime("%H:%M:%S")
    elif message == 'What is the weather like today?':
        response = 'I am sorry, I do not have access to weather information.'
    elif message == 'Tell me a joke':
        response = 'Why don’t scientists trust atoms? Because they make up everything!'
    elif message == 'What is the capital of France?':
        response = 'The capital of France is Paris.'
    elif message == 'Can you help me with math?':
        response = 'Sure, what math problem do you need help with?'
    else:
        response = 'I am sorry, I did not understand that. Could you please rephrase?'
    return jsonify({'message': response})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)