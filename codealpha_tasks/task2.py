def stock_portfolio_tracker():
    # 1. Hardcoded dictionary to define stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 175,
        "MSFT": 420,
        "AMZN": 185
    }
    
    # Dictionary to store the user's current portfolio (Ticker -> Quantity)
    portfolio = {}
    
    print("--- Welcome to the Stock Portfolio Tracker ---")
    print("Available stocks and their current prices:")
    for ticker, price in stock_prices.items():
        print(f"  {ticker}: ${price}")
    print("---------------------------------------------")

    # 2. Console Input/Output Loop
    while True:
        ticker = input("\nEnter a stock ticker to add (or type 'done' to calculate): ").upper().strip()
        
        if ticker == "DONE":
            break
            
        # Check if the stock exists in our predefined database
        if ticker not in stock_prices:
            print(f"Sorry, '{ticker}' is not available in our system. Please try a valid ticker.")
            continue
            
        # Get and validate the quantity from the user
        try:
            quantity = int(input(f"Enter the quantity of {ticker} you own: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")
            continue
            
        # Add or update the stock quantity in the portfolio dictionary
        if ticker in portfolio:
            portfolio[ticker] += quantity
        else:
            portfolio[ticker] = quantity
            
        print(f"Added {quantity} shares of {ticker} to your tracking list.")

    # 3. Basic Arithmetic and Portfolio Evaluation
    if not portfolio:
        print("\nYour portfolio is empty. No calculations to perform.")
        return

    print("\n============= Your Portfolio Summary =============")
    total_investment_value = 0
    summary_lines = [] # Collected to display and easily write to a file later
    
    for ticker, quantity in portfolio.items():
        price = stock_prices[ticker]
        holding_value = quantity * price  # Basic arithmetic calculation
        total_investment_value += holding_value
        
        line = f"{ticker}: {quantity} shares @ ${price}/share = ${holding_value}"
        summary_lines.append(line)
        print(line)
        
    total_summary_str = f"Total Portfolio Investment Value: ${total_investment_value}"
    print("-" * 50)
    print(total_summary_str)
    print("==================================================")

    # 4. Optional File Handling: Save results to a .txt file
    save_choice = input("\nWould you like to save this summary to a text file? (yes/no): ").lower().strip()
    if save_choice in ['yes', 'y']:
        try:
            with open("portfolio_summary.txt", "w") as file:
                file.write("STOCK PORTFOLIO TRACKER REPORT\n")
                file.write("==============================\n")
                for line in summary_lines:
                    file.write(line + "\n")
                file.write("------------------------------\n")
                file.write(total_summary_str + "\n")
            print("Successfully saved your report to 'portfolio_summary.txt'!")
        except IOError:
            print("An error occurred while attempting to write to the file.")

if __name__ == "__main__":
    stock_portfolio_tracker()