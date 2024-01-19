import tiktoken

"""
----------------------------- Description ----------------------------------
    Given a text string (e.g., "tiktoken is great!") and an encoding 
    (e.g., "cl100k_base"), a tokenizer can split the text string 
    into a list of tokens. For example:

    ["t", "ik", "token", " is", " great", "!"]

--------------------------- Model Encodings --------------------------------
cl100k_base 	      - gpt-4, gpt-3.5-turbo, text-embedding-ada-002
p50k_base 	          - Codex models, text-davinci-002, text-davinci-003
r50k_base (or gpt2)   -	GPT-3 models like davinci

------------------------------ Sample Use ----------------------------------

    text = "How are you today, i'm doing excellent"
    model = cl100k_base

    token_count = tokount(text, model) -> returns as 9

"""

gpt4 = 'cl100k_base'

def tokount(string: str, encoding_name: str) -> int:
    # GPT model stored as encoding_name
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# num_of_tokens = tokount("How are you today, i'm doing excellent", gpt4)
# print(num_of_tokens)