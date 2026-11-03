# Information

info = {
    "Name":"Alice",
    "Age": 28,
    "is_adult": True,
    "Height": 5.69
}

print(f"Info : {info}")
print(f"Name : {info['Name']}")
print(len(info))
print(info.keys())
print(info.values())

info["Name"] = "Bob"
info["City"] = "New York"
print(info)
