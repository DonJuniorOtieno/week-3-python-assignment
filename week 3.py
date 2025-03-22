def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if it's 40% or higher."""
    if discount_percent >= 40:
        final_price = price - (price * discount_percent / 100)
        return final_price
    return price

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)
print(f"Final price after discount: ${final_price:.2f}")