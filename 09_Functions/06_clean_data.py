def clean_list(data):
    clean_data = [item.strip().title() for item in data]
    return clean_data

raw_names = [" aSHA verma ", "RAHUL sharma", " priya nair ", "mohd FAIZAN khan"]
clean_names = clean_list(raw_names)
print(clean_names)