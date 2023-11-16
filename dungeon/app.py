from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Configure your OpenAI API key
#openai.api_key = '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'

# Initialize the OpenAI client for the Assistants API
client = openai.Client(api_key='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')
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You answer questions",
    tools=[],
    model="gpt-4-1106-preview"
)
thread = client.beta.threads.create()

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/message', methods=['POST'])
def message():
    user_message = request.data.decode('utf-8')
    #user_message = data['message']

    # Create a Thread for the conversation


    # Add the user's message to the Thread
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_message
    )

    # Run the Assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    
    run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id
    )

    # Retrieve the latest messages from the Thread
    response_messages = client.beta.threads.messages.list(
        thread_id=thread.id,
    )
    print('\nresponse message: \n' + str(response_messages))

    assistant_response = None
    #for message in response_messages:
    #    assistant_response = message
    #    break
    for msg in response_messages.data:
        if msg.role == 'assistant':
            for content in msg.content:
                if content.type == 'text':
                    assistant_response = content.text.value
    
    reply = assistant_response if assistant_response else "No reply from the assistant."
    print('\nreply: \n' + str(reply))
    return jsonify({"reply": reply})
    #return reply

if __name__ == '__main__':
    app.run(debug=True)
