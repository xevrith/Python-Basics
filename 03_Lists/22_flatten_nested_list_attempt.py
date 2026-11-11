# Flatten a nested list

numbers = [[1, 2], [3, 4]]

fix_list = [value for value in numbers for value in numbers]
print(fix_list)