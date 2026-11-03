# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_evens(num1, num2):

    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 < num2:
            print(num1)
        else:
            print(num2)

    elif num1 % 2 == 0 or num2 % 2 != 0:
        if num1 > num2:
            print(num1)
        else:
            print(num2)


lesser_of_evens(2,5)