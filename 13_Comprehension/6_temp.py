temperatures = {
    "Monday": 35,
    "Tuesday": 22,
    "Wednesday": 15,
    "Thursday": 30
}

temperature = {day: ("Hot" if temp >= 30 else "Warm" if temp > 20 else "Cold")for day,temp in temperatures.items()}
print(temperature)