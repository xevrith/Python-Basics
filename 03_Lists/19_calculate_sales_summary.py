#  Sales Analysis

def sales_analysis(data):
    total_sales = sum(data)
    max_sale = max(data)
    min_sale = min(data)
    avg_sale = total_sales / len(data)

    print(f"Total Sales : {total_sales}")
    print(f"Maximum Sale : {max_sale}")
    print(f"Minimum Sale : {min_sale}")
    print(f"Average Sale : {avg_sale}")


sales = [4500, 2300, 7800, 1200]
sales_analysis(sales)

