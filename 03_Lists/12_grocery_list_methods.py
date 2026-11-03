# Grocery Shopping List

groceries = ["milk", "eggs", "bread", "rice", "eggs", "tea"]

print(f"Eggs occurance : {groceries.count("eggs")}")
print(f"Position of rice : {groceries.index("rice")}")
print(f"Is suger in the list ? {"suger" in groceries}")

new_list = ["suger","salt","oil"]
groceries.extend(new_list)
groceries.remove("eggs")
groceries.sort()
print(f"Updated list {groceries}")

copy_list = groceries.copy()
groceries.clear()

print(f"Copy list : {copy_list}")
print(f"Old List : {groceries}")