import json
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key='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')

def read_rules():
    """Reads rules from a JSON file."""
    with open(r'aisummarizer_rules.json', 'r') as f:
        data = json.load(f)
    return data.get('topics', []), data.get('text_input', '')

def write_new_topic(topic: str):
    """Writes a new topic to the JSON file."""
    with open(r'aisummarizer_rules.json', 'r') as f:
        data = json.load(f)

    data.setdefault('topics', []).append(topic)

    with open('aisummarizer_rules.json', 'w') as f:
        json.dump(data, f, indent=4)

def process_input(file_path: str, text_input_format: str, topics: list) -> str:
    """Processes the input text file and formats the input for the chatbot."""
    with open(file_path, 'r', encoding='utf8') as file:
        text_contents = ''.join(file.readlines())

    topics_str = ', '.join(topics)  # Convert list of topics to a string
    formatted_input = text_input_format.format(topics=topics_str, text_contents=text_contents)
    return formatted_input

def get_chatbot_response(script_input: str) -> str:
    """Gets a response from the chatbot."""
    messages = [
        {"role": "system", "content": ("You are a helpful assistant that will receive instructions followed by a "
                                       "text input, you will follow the instructions as they are written and not "
                                       "deviate from requests other than those instructions.")},
        {"role": "user", "content": script_input}
    ]
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message.content

def ai_summarizer(file_path):
    """Main function to process the text file and get a summary."""
    topics, text_input_format = read_rules()
    script_input = process_input(file_path, text_input_format, topics)
    aisummary = get_chatbot_response(script_input).split('^')

    topic = aisummary[0][6:]
    relevance = aisummary[1][10:]
    ten_word_title = aisummary[2][13:].lower()

    if topic not in topics:
        write_new_topic(topic)

    ten_word_title = ''.join(e for e in ten_word_title if e.isalnum())
    
    return [topic, relevance, ten_word_title]

"""
text_file_path = r"txt\sample_article_1.txt"

result = main(text_file_path)
print(result)
"""
