# #### MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(sentance):
    reverse_sentance = " "
    new_sentance = sentance.split()
    print(" ".join(new_sentance[::-1]))
    


master_yoda(input("Enter a sentance : "))