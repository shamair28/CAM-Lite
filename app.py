
from flask import Flask, request, jsonify, render_template
import openai
import time
import os
## import config

app = Flask(__name__)

# Use the actual OpenAI API key
client = openai.Client(api_key="placeholder")

# The original code for file upload and assistant creation
#file = client.files.create(file=open("static/billionaire.txt", "rb"), purpose='assistants')
assistant = client.beta.assistants.create(
    name="CAM-Lite",
    instructions = "AI assistant that deals in business related inquiries for all levels of an organization.",
    #tools = [{"type": "retrieval"}],
    tools = [],
    #file_ids=[file.id],
    model="gpt-4-1106-preview"
    )
thread = client.beta.threads.create()


@app.route('/')
def home():
    global thread
    thread = client.beta.threads.create()
    return render_template('chat_modified.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.data.decode('utf-8')
    print(user_input)
    #user_input = request.g['message']
    #thread = client.beta.threads.create()
    messages = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input,
            #file_ids=[file.id],
        )
    run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
    )
    
    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

        if run_status.completed_at is not None:
            break
        
    messages = client.beta.threads.messages.list(
             thread_id=thread.id,
             order='asc'
    )
    print('\nresponse message from threads: \n:' + str(messages))
    for msg in messages.data:
                if msg.role == 'assistant':
                    for content in msg.content:
                        if content.type == 'text':
                                assistant_response = content.text.value

    print('\nassistant output: ' + str(assistant_response) + '\n')
    return jsonify({'response': assistant_response})

if __name__ == '__main__':
    app.debug=False
    #app.run(debug=True)
