import math

"""
-------------------
------ hello ------
-- this function --
---- returns a ----
----- string ------
--- with equal ----
--- length dash ---
------ lines ------



input:
-> number of lines: nolines
-> text/line: text
-> ideal width: width

output:
dashline headers

"""

def dashcalc(text:list[str], width: int) -> list[str]:
    
    # output storage
    headers = []

    for i in range(0, len(text)):
        
        lencomment = len(text[i])

        nodash = (width - lencomment - 2)//2

        print(nodash*'-', text[i], nodash*'-')

    return headers

def dashline():
    nolines = int(input("How many headers would you like? "))
    width = int(input("What is your desired width?: "))
    text = []

    for i in range(nolines):
        phrase = input("Please enter header text: ")
        text.append(phrase)

    return dashcalc(text, width)
    


dashline()

