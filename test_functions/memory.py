"""
--------------------------------- Introduction ---------------------------------

Memory will act as a pseudo brain for handling the types of information received
during the data process. Earlier in the project, we generated descriptive titles
for each text input, this will help with the retrieval process when coming up
with data backed judgements

---------------------------------- Explanation --------------------------------- 

The descriptive title is the key for retrieving text files, as well as bunching
them up, removing them when they get too old for use and so on. first, the script
will check the title and separate the relevant information, and set up a file 
system for each respective location. 

------------------------------- File Organization ------------------------------ 

------------------------------------- Input ------------------------------------

dd%mm%yy_financial_medium_tdbankschwabbincomedropsignificantly.txt

------------------------------------- Output -----------------------------------
"""
import os
import shutil

def foldersetupverify(base_directory, topics, relevance_levels):
    for topic in topics:
        for relevance in relevance_levels:
            folder_path = os.path.join(base_directory, topic, relevance)
            os.makedirs(folder_path, exist_ok=True)

def sendtolocation(file: str, file_location: str, base_directory: str): 
    file_raw = file.split('_')
    filetopic = file_raw[1]
    file_relevance = file_raw[2]

    # Construct the new location path
    new_location = os.path.join(base_directory, filetopic, file_relevance, file)

    # Move the file
    shutil.move(file_location, new_location)
    print(f"Moved {file} to {new_location}")

# Example usage
base_directory = r'C:\Users\danie\Desktop\consult-gpt-poc-main\Dataprocessing Demo\memory'
topics = ['business', 'local', 'politics']
relevance = ['medium', 'high', 'low']  # Add your relevance levels here

# Setup and verify folders
foldersetupverify(base_directory, topics, relevance)

# Move a specific file
file_name = r'dd%mm%yy_business_medium_tdbankschwabbincomedropsignificantly.txt'
file_location = r'C:\Users\danie\Desktop\consult-gpt-poc-main\Dataprocessing Demo\txt\%mm%yy_business_medium_tdbankschwabbincomedropsignificantly.txt'
sendtolocation(file_name, file_location, base_directory)

