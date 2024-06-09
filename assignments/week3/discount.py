# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
def calculate_discount(price,discount_percent):
    final_price = price - price * discount_percent
    if discount_percent >= 20/100 :
        return final_price
    else:
        return price
price = float(input("Enter your price\n"))
discount_percent = float(input("Enter discount\n"))/100
print(calculate_discount(price,discount_percent))


