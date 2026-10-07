# #### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    new_char = ""
    for char in text:
        new_char = new_char + char *2
    return new_char

print(paper_doll("Hello"))