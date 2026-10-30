order_id = "ORD-2026-IN-004582".split("-")

print(f"Year: {order_id[1]} | Country: {order_id[3]} | Serial: {order_id[-1][-4:]}")
print(f"Domestic 2026+ order? {int(order_id[1]) >= 2026 and order_id[2] == "IN"}")
next_id = int(order_id[-1][-4:])+1
print(f"Next ID: {order_id[0]}-{order_id[1]}-{order_id[2]}-{next_id}")
