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

new_plan = {"Budget":[200.0,300.20,55.00]}
guest.update(new_plan)

print(guest)