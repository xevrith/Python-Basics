# Party List

guest = {
    "Name" : ["Bob","Alice","David"],
    "Games": ("Football","Chess","Boxing"),
    "Food" : ["Shawerma","Juices","Bargur","Pizza"]
}

print(f"Only Keys : {guest.keys()}")
print(f"Only Values : {guest.values()}")
print(f"Items : {guest.items()}")

print(guest.get("Name"))