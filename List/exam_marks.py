# Exam Marks Analysis

def result_details(data):

    print(f"Highest Marks : {max(data)}")
    print(f"Lowest Marks : {min(data)}")
    print(f"Total Marks : {sum(data)}")
    print(f"Average Marks : {sum(data)/len(data)}")

marks = [78, 92, 45, 66, 88, 35, 71, 59, 95, 82]

result_details(marks)

new_list = sorted(marks)
print(new_list)

new_result = []
for result in marks:

    if result >= 35:
        new_result.append("Pass")
    else:
        new_result.append("Fail")

print(new_result)

second_new_result = ["Pass" if result >= 35 else "Fail" for result in marks]
print(second_new_result)

del min(marks)
