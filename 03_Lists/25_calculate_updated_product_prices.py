# Product price conversion

prices = [100, 250, 500, 1000]
print(f"Old Price : {prices}")

increase_price = [price * 0.10 for price in prices]
total_price = [old_price + new_price for old_price,new_price in zip(prices,increase_price)]

print(f"New Price : {total_price}")