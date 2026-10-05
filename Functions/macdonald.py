# #### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_mac(text):
    text1 = text[0:3].capitalize()
    text2 = text[3:].capitalize()
    new_text = text1 + text2

    return new_text


print(old_mac("macdonald"))