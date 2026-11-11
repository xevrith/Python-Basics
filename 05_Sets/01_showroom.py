# Models available in the showroom
showroom = {"X1", "X5", "i4", "M3", "iX"}

# Models customers searched for online
online_searches = {"X5", "i4", "Z4", "i7"}

# Models customers actually bought this month
sold = {"X5", "M3"}

# Electric models
electric = {"i4", "iX", "i7"}

# SUV models
suv = {"X1", "X5", "iX"}

# Colors in stock (note the duplicates in the list)
color_list = ["Black", "White", "Black", "Blue", "White", "Red"]

print(suv)
print(len(suv))
print(type(showroom))
print()

waiting_list = set()
unique_color = set(color_list)
print(unique_color)

print()
waiting_list.add("Z4")
waiting_list.add("i7")
waiting_list.add("i5",)
waiting_list.add("Z4")
print(len(waiting_list))
print(waiting_list)


print()
waiting_list.remove("i5")
print(waiting_list.discard("Q8"))


item = showroom.pop()
print(item)


all_models = showroom.union(online_searches)
print(all_models)

electric_models = suv.union(electric)
print(electric_models)

common = showroom.union(online_searches)
print(common)

sold_model = suv.union(sold)
print(sold_model)