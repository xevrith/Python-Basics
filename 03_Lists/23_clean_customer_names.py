# Customer name cleaning

names = [" aman ", "SARA", " rahul", "PRIYA "]

clean_name = [name.capitalize().strip() for name in names]
print(f"Before :{names}")
print(f"After :{clean_name}")