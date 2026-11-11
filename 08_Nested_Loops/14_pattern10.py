# Simple Pyramid

i = 1

while i <= 5:
    
    j = 1
    while j <= 5 - i:
        print(" ",end="")
        j += 1

    k = 1
    while k <= i:
        print("*",end=" ")
        k += 1

    print()
    i += 1