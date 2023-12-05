
from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Use the actual OpenAI API key
openai.api_key = 'YOUR_API_KEY_HERE'

# The original code for file upload and assistant creation
file = openai.File.create(file=open("static/billionaire.txt", "rb"), purpose='answers')
assistant = openai.Assistant.create(name="CAM-Lite", model="gpt-3.5-turbo")
thread = openai.Thread.create(assistant_id=assistant.id)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    global thread
    user_input = request.form['message']
    message = openai.Message.create(
        assistant_id=assistant.id,
        thread_id=thread.id,
        message={'role': 'user', 'content': user_input}
    )
    assistant_response = message['data']['content']
    return jsonify({'response': assistant_response})

if __name__ == '__main__':
    app.run(debug=True)
