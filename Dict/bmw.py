# BMW Showroom

# Inventory: model -> details
inventory = {
    "X1": {"type": "SUV",   "price": 45000, "fuel": "Petrol",   "stock": 6},
    "X5": {"type": "SUV",   "price": 75000, "fuel": "Diesel",   "stock": 4},
    "i4": {"type": "Sedan", "price": 60000, "fuel": "Electric", "stock": 3},
    "M3": {"type": "Sedan", "price": 85000, "fuel": "Petrol",   "stock": 2},
    "iX": {"type": "SUV",   "price": 90000, "fuel": "Electric", "stock": 0},
}

# Sales: customer -> model bought
sales = {"Ali": "X5", "Sara": "i4", "John": "X5", "Emma": "M3"}

# One car on its own (for Levels 1-3)
car = {"model": "X5", "price": 75000, "fuel": "Diesel"}


print(f"Fuel Type {car["fuel"]}")
print(f"Car Color : {car.get("Color")}")


car["seats"] = 5
car["price"] = 72000
car.pop("fuel")
print(f"Updated List  : {car}")


for key, value in car.items():
    print(f"{key} : {value}")

for key in car.keys():
    print(f"Keys : {key}")

for value in car.values():
    print(f"Value : {value}")


print(f"Stock of M3 : {inventory['M3']["stock"]}")

for key,value in inventory.items():
    print(f"Model - {key} : Fuel Type - {value["fuel"]}")


if "i7" in inventory:
    print("Model Found")

else:
    print("Model not found")

print(f"Price of Z4 : {inventory.get("Z4",{}).get("price",0)}")


inventory["i7"] = {"type" : "Sedan","price":1200000,"fuel":"Electric","stock":1}
inventory["X5"]["stock"] -= 2
inventory["M3"]["price"] += 5000
del inventory["iX"]


print(f"Updated Dict : {inventory}")

for model, details in inventory.items():
    if details["price"] > 60000:
        print(f"Model -> {model}")

models = [m for m, d in inventory.items() if d["stock"] == 0]
print(models)

