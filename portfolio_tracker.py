stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 120, "MSFT": 150}
portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")
print("Enter 'done' when finished.")

while True:
    stock = input("Enter stock symbol (AAPL, TSLA, GOOGL, MSFT): ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock name! Try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Quantity must be a number. Try again.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

for stock, qty in portfolio.items():
    total_investment += stock_prices[stock] * qty

print(f"\nYour total investment value: ${total_investment}")
