# Customer Database
def customer_details(data):
    first_customer = data[0]
    third_customer = data[2]
    last_customer = data[-1]
    number_customer = len(data)

    print(f"First Customer : {first_customer}")
    print(f"Third Customer : {third_customer}")
    print(f"Last Customer : {last_customer}")
    print(f"Number of Customer : {number_customer}")


customers = ["Aman", "Rahul", "Sara", "Mohammad", "Priya"]
customer_details(customers)