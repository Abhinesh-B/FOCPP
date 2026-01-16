# def get_pizza_price(pizza_number):
#     """Get a valid pizza price from the user."""
#     while True:
#         try:
#             price = float(input(f"Enter Price of Pizza #{pizza_number}: "))
#             if price <= 0:
#                 print("Please enter a valid price!")
#             else:
#                 return price
#         except ValueError:
#             print("Please enter a valid price!")

# def main():
#     # Display header
#     print("Beckett Pizza Plaza 4-for-3 Offer")
#     print("=================================")
#     print()
    
#     # Get four pizza prices
#     prices = []
#     for i in range(1, 5):
#         price = get_pizza_price(i)
#         prices.append(price)
    
#     # Calculate total (sum of all minus the cheapest)
#     total_before_discount = sum(prices)
#     cheapest = min(prices)
#     total_after_discount = total_before_discount - cheapest
    
#     # Calculate discount percentage
#     discount_percentage = (cheapest / total_before_discount) * 100
    
#     # Display result
#     print()
#     print(f"Order Total is £{total_after_discount:.2f}, a fabulous discount of {discount_percentage:.0f}%!")

# if __name__ == "__main__":
#     main()


import math

def read_price(pizza_number: int) -> float:
    """Read one valid pizza price (> 0) from the user."""
    while True:
        raw = input(f"Enter Price of Pizza #{pizza_number}: ").strip()
        try:
            price = float(raw)
            if price <= 0:
                raise ValueError
            return price
        except ValueError:
            print("Please enter a valid price!")

def main() -> None:
    print("Beckett Pizza Plaza 4-for-3 Offer")
    print("=================================\n")

    prices = [read_price(i) for i in range(1, 5)]

    full_total = sum(prices)
    free_pizza = min(prices)
    charged_total = full_total - free_pizza

    # Discount is the free pizza as a percentage of the full (undiscounted) total.
    discount_percent = (free_pizza / full_total) * 100.0

    # Match the sample outputs: 23.4% becomes 24%, 18.6% becomes 19%.
    discount_display = math.ceil(discount_percent)

    print(f"\nOrder Total is £{charged_total:.2f}, a fabulous discount of {discount_display}%!")

if __name__ == "__main__":
    main()
