# Simple Shopping Cart

customer = input("Enter customer name: ")

product1 = input("Enter Product 1 name: ")
price1 = float(input("Enter Product 1 price: "))

product2 = input("Enter Product 2 name: ")
price2 = float(input("Enter Product 2 price: "))

product3 = input("Enter Product 3 name: ")
price3 = float(input("Enter Product 3 price: "))

# Calculate subtotal
subtotal = price1 + price2 + price3

# Determine discount rate
if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0

# Calculate discount and final total
discount = subtotal * discount_rate
final_total = subtotal - discount

# Display shopping summary
print(f"\nCustomer Name: {customer}")
print(f"Product 1: {product1}")
print(f"Price: {price1:.0f}")
print(f"Product 2: {product2}")
print(f"Price: {price2:.0f}")
print(f"Product 3: {product3}")
print(f"Price: {price3:.0f}")
print(f"Subtotal: {subtotal:.0f}")
print(f"Discount: {discount:.0f}")
print(f"Final Total: {final_total:.0f}")