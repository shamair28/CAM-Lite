import json

def rulereader():
    with open('aisummarizer_rules.json', 'r') as f:
        data = json.load(f)
        # {'topics':['business','politics'], 'text_input':'text input blah blah'}

    topics = data.get('topics', [])
    text_input = data.get('text_input', '')

    return topics, text_input

def newtopicwriter(topic: str):
    with open('aisummarizer_rules.json', 'r') as f:
        data = json.load(f)

    if 'topics' in data:
        data['topics'].append(topic)
    else:
        data['topics'] = [topic]

    with open('aisummarizer_rules.json', 'w') as f:
        json.dump(data, f, indent=4)

    return

# Example usage
topics, text_input = rulereader()
print(topics)  # Print existing topics

newtopicwriter("science")  # Add a new topic

topics, text_input = rulereader()
print(topics)  # Print updated topics
