import yfinance as yf

def get_stock_data(ticker, start_date, end_date):
    """
    Retrieve historical stock data using yfinance.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_metrics(stock_data):
    """
    Calculate basic fundamental analysis metrics.
    """
    # Calculate average closing price
    stock_data['Avg_Close'] = stock_data['Close'].mean()

    # Calculate 30-day moving average
    stock_data['30_MA'] = stock_data['Close'].rolling(window=30).mean()

    # Add more metrics as needed

    return stock_data

def main():
    # Set stock information
    stock_ticker = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2023-01-01'

    # Get stock data
    stock_data = get_stock_data(stock_ticker, start_date, end_date)

    # Calculate metrics
    stock_data = calculate_metrics(stock_data)

    # Print the results
    print(stock_data[['Close', 'Avg_Close', '30_MA']])

if __name__ == "__main__":
    main()
