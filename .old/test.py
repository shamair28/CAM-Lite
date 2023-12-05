import openai
import time

client = openai.Client(api_key='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',)

# Upload your knowledge base document
file = client.files.create(
    file=open("static/test_document.txt", "rb"),
    purpose='assistants'
)


assistant = client.beta.assistants.create(
    name="Customer Support Assistant with Knowledge Retrieval",
    instructions="You are an AI assistant that provides customer support for a tech company. Answer user questions, provide troubleshooting steps, and offer detailed product information. You are an AI assistant that provides customer support. Answer in step by step instructions if appropriate. Use the knowledge base to best respond to customer queries.",
    tools=[{"type": "retrieval"}],
    file_ids=[file.id],
    model="gpt-4-1106-preview"
)

thread = client.beta.threads.create()

def chat_with_assistant():
    print("Welcome to the Customer Support Assistant! Ask any question, or type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        message = client.beta.threads.messages.create(
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

            time.sleep(1)  # Sleep for a second
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )

        # Assistant's response
        for msg in messages.data:
            if msg.role == 'assistant':
                for content in msg.content:
                    if content.type == 'text':
                        print("Assistant:", content.text.value)



chat_with_assistant()