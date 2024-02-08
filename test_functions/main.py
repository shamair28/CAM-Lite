from dependencies import check_and_install_dependencies
from file_preparation import *
from ai_summarizer import ai_summarizer

original_file = r'test_functions/raw_articles/sample_article_1.docx'



def main(original_file) -> str:

    txt_path = file_preparation(original_file)

    description = ai_summarizer(txt_path)

    topic = description[0]
    relevance = description[1]
    tenwordtitle = description[2]

    file_rename(txt_path, topic, relevance, tenwordtitle)

    return

result = main(original_file)

print(result)