import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 145
}

portfolio = {}

print("Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish.\n")

while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found.\n")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.\n")
            continue
    except ValueError:
        print("Invalid number.\n")
        continue

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

print("\nPortfolio Summary")
total_investment = 0

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock}: {qty} × {price} = {value}")

print(f"\nTotal Investment: {total_investment}")

save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    filename = input("Enter filename (e.g., portfolio.csv): ")
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            writer.writerow([stock, qty, price, value])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total_investment])
    print("File saved successfully.")
else:
    print("Data not saved.")
