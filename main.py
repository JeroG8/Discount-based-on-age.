price = float(input("Enter the price (USD): "))
age = int(input("Enter your age: "))

discount = price - (price * 0.15)

if age >= 65:
    result = discount
    print(f"Your final price with discount is {result} USD!")
else:
    result = price
    print(f"Your final price is {result}")