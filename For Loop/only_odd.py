my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
odd_list = []

for i in my_list:
    if my_list.index(i) % 2 != 0:
        odd_list.append(i)
    else:
        continue


print(odd_list)
