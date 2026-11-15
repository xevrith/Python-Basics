marks = {
    "Aman": 95,
    "Riya": 72,
    "Karan": 45,
    "Neha": 58
}

result = {name: ("Excellent" if mark >= 90 else "Pass" if mark >= 60 else "Fail") for name, mark in marks.items()}
print(result)

