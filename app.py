import openai
import time

# init openai client
client = openai.Client(api_key='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')

# sample upload for knowledge base
file = client.files.create(
    file=open("static/billionaire.txt", "rb"),
    purpose="assistants"
)

assistant = client.beta.assistants.create(
    name="CAM-Lite",
    instructions = "AI assistant that deals in business related inquiries for all levels of an organization",
    tools = [{"type": "retrieval"}],
    file_ids=[file.id],
    model="gpt-4-1106-preview"    
)
thread = client.beta.threads.create()

def chat_with_assistant():
    print("Welcome to CAM-Lite, my current knowledgebase is on the Forbes 2018 Billionaires List")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
                break
        
        message =  client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input,
            file_ids=[file.id]
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
             
             time.sleep(1) # sleep 1 sec
        messages = client.beta.threads.messages.list(
             thread_id=thread.id
        )

        # CAM-Response
        for msg in messages.data:
             if msg.role == 'assistant':
                  for content in msg.content:
                       if content.type == 'text':
                            print("CAM-Lite: ", content.text.value)

chat_with_assistant()