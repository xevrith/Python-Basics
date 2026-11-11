# Given prices = [100, 250, 75, 300], use map() and a lambda to add 18% GST to each price.

prices = [100, 250, 75, 300]
final_amount = list(map(lambda x : round(x + (1 + 0.18 / 100)),prices))
print(final_amount)