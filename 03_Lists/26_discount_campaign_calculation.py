# Discount campaign

prices = [500, 1000, 1500, 2000]

discount = [price * 0.20 for price in prices]
after_discount = [price + disc for price,disc in zip(prices,discount)if price >= 1000]
print(after_discount)