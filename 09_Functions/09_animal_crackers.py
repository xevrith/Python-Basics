# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):

    char = text
    first_char = char[0]
    second_char = char[char.find(" ") + 1]
    
    if first_char == second_char:
        print(True)
    else:
        print(False)


animal_crackers("Find Fish")