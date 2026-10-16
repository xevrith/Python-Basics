# Daily Study Tracker

def idx(data):
    print(f"First Idx : {data[0]}")
    print(f"Last Idx : {data[-1]}")
    print(f"Mid Idx : {data[len(data)//2]}")

def info(data):
    print(f"Length of the list : {len(data)}")
    print(f"Total Hours : {sum(data)}")
    print(f"Max Hours : {max(data)}")
    print(f"Min Hours : {min(data)}")

def avg(data):
    average = sum(data) / len(data)
    return average

hours = [2, 3, 1, 4, 2, 5, 3]   # hours studied Mon to Sun
idx(hours)
print()
info(hours)
print()
avg_hour = avg(hours)
print(f"Average Hour : {round(avg_hour,2)}")

hours.append(3) # next monday
hours.insert(6,2)
hours.remove(1)
hours.pop()

print()
info(hours)