# Display header
print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================")
print()

prices = []

for i in range(1, 5):
    while True:
        try:
            price = float(input(f"Enter Price of Pizza #{i}: "))
            if price <= 0:
                print("Please enter a valid price!")
            else:
                prices.append(price)
                break
        except ValueError:
            print("Please enter a valid price!")


total_before_discount = sum(prices)
cheapest_pizza = min(prices)
order_total = total_before_discount - cheapest_pizza

# Calculate the discount percentage
discount_percentage = (cheapest_pizza / total_before_discount) * 100

# Display the result
print()
print(f"Order Total is £{order_total:.2f}, a fabulous discount of {round(discount_percentage)}%!")