# Valid customer IDs

ids = ["DS101", "HR202", "DS305", "IT410", "DS999"]

valid_id = [id for id in ids if id.startswith("DS")]
print(valid_id)