# Product Inventory
def product_details(data):
    first_product = data[0]
    last_product = data[-1]
    second_last_product = data[-2]
    third_product = data[2]

    return first_product, last_product, second_last_product, third_product


products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

inventory = product_details(products)
print(inventory)
