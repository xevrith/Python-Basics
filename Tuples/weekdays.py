# Weekdays 

weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

print(f"First day : {weekdays[0]}")
print(f"last day : {weekdays[-1]}")
print(f"Weekend : {weekdays[-2:]}")
print()
print(f"Is Fri exist : {"Fri" in weekdays}")
print(f"Position Of Wed : {weekdays.index("Wed")}")
print(f"Number of times Mon Appears : {weekdays.count("Mon")}")