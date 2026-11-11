# Write a lambda that takes a temperature in Celsius and returns "Hot" if it is above 30, otherwise "Not hot"

temp = lambda x: "Hot" if x >= 30 else "Not Hot"
print(temp(45))
print(temp(25))