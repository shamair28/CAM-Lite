import os
from token_counter import tokount

topics = ["business", "tech", "politics"]
relevance = ["low", "medium", "high"]
textfiledir = r"test_functions/txt/sample_article_1.txt"

def inputoutput(textfiledir: str, topics: list, relevance: list) -> str:

    with open(textfiledir, 'r', encoding='utf8') as file:

        text_contents = ''

        for line in file:
            text_contents += line

        text_input = "I am going to send you text, as well as options for topics and relevance, that you will decide based on the text contents. The options for relevance is low medium or high, with the criteria for relevance being related to a small business's personal needs. the options for topics are as follows: {topics}. if the text does not fit one of these topics, please write a new one that fits better. you will then write a 10 word descriptive summary of the text, to be returned as '10wordtitle', do not include spaces or punctuation for the 10wordtitle. your expected output is as follows: topic=[topic], relevance-[relevance], 10wordtitle=[10wordtitle]. The text is as follows {text_contents}".format(topics = topics, text_contents = text_contents)

        token_estimate = tokount(text_input, 'cl100k_base')
        return [text_input, token_estimate]

[result, tokens] = inputoutput(textfiledir, topics, relevance)

print("this process used", tokens, "tokens\n\n", result)