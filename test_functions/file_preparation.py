import os
import pypandoc
import token_counter
from datetime import datetime

"""
------------------------------- Introduction -------------------------------

Text input handles the intake of text data, converts it to a .txt if it is
not already, and makes appropriate calculations for the type of text stored
inside. 

------------------------------- Sample Input -------------------------------

    Last year, TD reported US$285 million in net income in its first quarter 
    from its investment in Schwab.

    TD says adjusted net income should work out to about US$230 million, for 
    about a 30 per cent drop from last year’s US$328 million.

    Canaccord Genuity Group Inc. analyst Matthew Lee says the Schwab results 
    came in slightly higher than expected, but that the financial firm’s outlook 
    for the year disappointed.

    Lee said key takeaways for the year from U.S. bank earnings in recent days 
    are net income pressure, improved capital markets and continued credit 
    challenges on commercial real estate loans, some of which translate into 
    Canadian trends as well.

    “In terms of cross-border read-throughs, we expect the Canadian banks 
    to see similar trends in capital markets and loan growth but do not 
    necessarily expect to see the same level of net interest margin pressure 
    as mortgage renewals help to offset increasing deposit costs.”

    Lee said Bank of Montreal and Royal Bank of Commerce should benefit 
    the most from improvements in U.S. capital markets, while TD will be
    most affected by softer net interest income in the country.

------------------------------- Sample Output ------------------------------ 

    char_count = 1214
    token_estimate = 254

    send_to => medium importance (financial)

    descriptive_summary = "TD's Net Income from Schwab Investment Falls 
                           30% to US$230M; Analysts Highlight Mixed Financial 
                           Outlook and Parallel Trends in Canadian Banks"

    topic = financial

    relevance = medium

    tenwordtitle = tdbanksschwabbincomedropssignificantly

    storage_name = dd%mm%yy_financial_medium_tdbankschwabbincomedropsignificantly.txt

-------------------------------- Variables ---------------------------------



"""

txt_dir = 'txt'
model = 'cl100k_base'



# renames file to descriptive title 
def file_rename(text_file_path, topic, relevance, tenwordtitle) -> str:
    # Get the current date and time
    current_datetime = datetime.now()

    # Format the datetime as a string to use as the filename
    timestamp = str((current_datetime.strftime("%Y%m")))

    # descriptive file title
    descriptive_file_title = ("{timestamp}_{topic}_{relevance}_{tenwordtitle}".format(timestamp, topic, relevance, tenwordtitle))
    
    # rename text file to descriptive file title
    os.rename(text_file_path, descriptive_file_title )

    return text_file_path

# checks to see if txt directory exists, if not - makes one
if not os.path.exists(txt_dir):
    os.makedirs(txt_dir)

# Simplified function to get file type
def filetype(original_file_dir: str) -> str:
    _, file_extension = os.path.splitext(original_file_dir)
    return file_extension

# Converts docx to txt
def convert_docx_to_txt(docx_file_path):
    if not os.path.exists(docx_file_path):
        return "File does not exist: " + docx_file_path

    base_filename = os.path.splitext(os.path.basename(docx_file_path))[0]
    txt_file_path = os.path.join(txt_dir, base_filename + '.txt')

    pypandoc.convert_file(docx_file_path, 'plain', outputfile=txt_file_path)
    return txt_file_path

"""
def convert_pdf_to_txt(pdf_file_path):
    if not os.path.exists(pdf_file_path):
        return "File does not exist: " + pdf_file_path
"""   

def file_preparation(original_file_dir: str):
    # determine file type
    extension = filetype(original_file_dir)
    if extension == '.docx':
        
        # convert original docx file to txt
        text_file_path = convert_docx_to_txt(original_file_dir)

        # take apart txt and analyze
        with open(text_file_path, 'r', encoding="utf8") as file:
            char_count = 0
            word_count = 0 
            space_count = 0
            line_count = 0
            token_estimate = 0

            for line in file:
                line_count += 1
                char_count += len(line)
                words = line.split()
                word_count += len(words)
                space_count += len(words) - 1
                token_estimate += token_counter.token_counter(line, model)

            print("char_count: %d\nword_count: %d\nspace_count: %d\nline_count: %d\ntoken_estimate: %d" % (char_count, word_count, space_count, line_count, token_estimate))

            return text_file_path

        
