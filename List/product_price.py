# Product price conversion

prices = [100, 250, 500, 1000]
print(f"Old Price : {prices}")

increase_price = [price * 0.10 for price in prices]
new_price = [price + increase_price for price in prices]

print(new_price)