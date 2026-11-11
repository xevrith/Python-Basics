# Transaction review

transactions = [-500, 1200, 0, 2500, -100, 700]

positive_trans = [trans for trans in transactions if trans >= 0]
print(f"Only Positive Values : {positive_trans}")