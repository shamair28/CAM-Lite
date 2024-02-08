'''
take a text file, use ai to do some shit

'''
import os
from openai import OpenAI

client = OpenAI(api_key = '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')

from token_counter import tokount

topics = ["business", "tech", "politics"]
relevance = ["low", "medium", "high"]
textfiledir = r"test_functions/txt/sample_article_1.txt"

def inputoutput(textfiledir: str, topics: list, relevance: list) -> str:

    with open(textfiledir, 'r', encoding='utf8') as file:

        text_contents = ''

        for line in file:
            text_contents += line

        text_input = """I am going to send you text, as well as options for topics and relevance, 
        that you will decide based on the text contents. The options for relevance is low medium or high, 
        with the criteria for relevance being related to a small business's personal needs. the options for topics are as follows: {topics}. 
        if the text does not fit one of these topics, please write a new one that fits better. you will then write a 10 word descriptive summary of the text, 
        to be returned as '10wordtitle', do not include spaces or punctuation for the 10wordtitle. 
        your expected output is as follows: topic=[topic], relevance=[relevance], 10wordtitle=[10wordtitle]. The text is as follows {text_contents}""".format(topics = topics, text_contents = text_contents)

        token_estimate = tokount(text_input, 'cl100k_base')
        return [text_input, token_estimate]

[result, tokens] = inputoutput(textfiledir, topics, relevance)

scriptresult = str(inputoutput(textfiledir, topics, relevance))

# print("this process used", tokens, "tokens\n\n", result)
print("token count: ", tokens)





def chatbot():
    
    messages = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": scriptresult}]
    while True:
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        response = completion.choices[0].message.content
        output = print(response)
        return response
    


if __name__ == "__main__":
    chatbot()