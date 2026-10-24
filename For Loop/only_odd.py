my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
odd_list = []

for odd in range(0,len(my_list)):
    if my_list.index(odd) % 2 == 0:
        odd_list.append(my_list.index(odd))
    else:
        continue

print(odd_list)
