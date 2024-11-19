import requests

API_KEY = 'YOUR_API_KEY'  # Replace with your Alpha Vantage API key

def fetch_stock_quote(ticker):
    """Fetches stock data from Alpha Vantage API."""
    try:
        api_url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
        response = requests.get(api_url)
        response.raise_for_status()
        stock_info = response.json()
        if "Global Quote" in stock_info:
            return stock_info["Global Quote"]
        else:
            print(f"Error: Unable to fetch data for {ticker}.")
            return None
    except requests.RequestException as e:
        print(f"Error: API request failed. {e}")
        return None

class InvestmentPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_investment(self, ticker, shares):
        """Adds stocks to the portfolio."""
        if shares <= 0:
            print("Error: Shares must be a positive number.")
            return
        if ticker in self.portfolio:
            self.portfolio[ticker] += shares
        else:
            self.portfolio[ticker] = shares
        print(f"Added {shares} shares of {ticker} to your portfolio.")

    def remove_investment(self, ticker, shares):
        """Removes stocks from the portfolio."""
        if ticker not in self.portfolio:
            print(f"Error: {ticker} is not in your portfolio.")
            return
        if shares <= 0 or shares > self.portfolio[ticker]:
            print("Error: Invalid number of shares.")
            return
        self.portfolio[ticker] -= shares
        if self.portfolio[ticker] <= 0:
            del self.portfolio[ticker]
        print(f"Removed {shares} shares of {ticker} from your portfolio.")

    def calculate_total_value(self):
        """Calculates the total value of the portfolio."""
        total = 0
        for ticker, shares in self.portfolio.items():
            stock_info = fetch_stock_quote(ticker)
            if stock_info:
                try:
                    stock_price = float(stock_info['05. price'])
                    total += stock_price * shares
                except KeyError:
                    print(f"Error: Unable to fetch price for {ticker}.")
        return total

def calculate_profit_or_loss(initial_value, current_value):
    """Calculates profit or loss."""
    return current_value - initial_value

def evaluate_diversification(portfolio):
    """Evaluates portfolio diversification."""
    distribution = {}
    total_value = portfolio.calculate_total_value()
    if total_value == 0:
        return {}
    for ticker, shares in portfolio.portfolio.items():
        stock_info = fetch_stock_quote(ticker)
        if stock_info:
            try:
                stock_price = float(stock_info['05. price'])
                value = shares * stock_price
                sector = stock_info.get('01. symbol', ticker)
                distribution[sector] = distribution.get(sector, 0) + value
            except KeyError:
                print(f"Error: Unable to process data for {ticker}.")
    return {sector: (value / total_value) * 100 for sector, value in distribution.items()}

def portfolio_manager():
    """Main function to manage the investment portfolio."""
    if not API_KEY or API_KEY == 'YOUR_API_KEY':
        print("Error: Please provide a valid Alpha Vantage API key.")
        return

    portfolio = InvestmentPortfolio()
    initial_investment = None

    while True:
        print("\n--- Portfolio Manager ---")
        print("1. Add a stock to your portfolio")
        print("2. Remove a stock from your portfolio")
        print("3. View the total portfolio value")
        print("4. Exit the portfolio manager")

        selection = input("Choose an option: ").strip()

        if selection == '1':
            ticker = input("Enter the stock ticker symbol: ").strip().upper()
            try:
                shares = int(input("Enter the number of shares: ").strip())
                portfolio.add_investment(ticker, shares)
            except ValueError:
                print("Error: Please enter a valid number of shares.")
        elif selection == '2':
            ticker = input("Enter the stock ticker symbol: ").strip().upper()
            try:
                shares = int(input("Enter the number of shares to remove: ").strip())
                portfolio.remove_investment(ticker, shares)
            except ValueError:
                print("Error: Please enter a valid number of shares.")
        elif selection == '3':
            current_value = portfolio.calculate_total_value()
            if initial_investment is None:
                initial_investment = current_value
            print(f"\nCurrent Portfolio Value: ${current_value:.2f}")
            print(f"Total Profit/Loss: ${calculate_profit_or_loss(initial_investment, current_value):.2f}")
            print("\nPortfolio Diversification Breakdown:")
            diversification = evaluate_diversification(portfolio)
            if diversification:
                for sector, percentage in diversification.items():
                    print(f"{sector}: {percentage:.2f}%")
            else:
                print("Your portfolio is currently empty or data is unavailable.")
        elif selection == '4':
            print("Exiting the Portfolio Manager. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    portfolio_manager()
