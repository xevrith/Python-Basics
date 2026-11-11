# Diamond

i = 1
j = 4


while i <= 5:
    k = 1
    while k <= 5 - i:
        print(" ",end="")
        k += 1

    l = 1
    while l <= i:
        print("*",end=" ")
        l += 1

    print()
    i += 1

while j >= 1:

    m = 1
    while m <= 5 - j:
        print(" ",end="")
        m += 1

    n = 1
    while n <= j:
        print("*",end=" ")
        n += 1

    print()
    j -= 1