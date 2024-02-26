import yfinance as yf
import csv
import os

startDate = "2024-02-19"
endDate = "2024-02-26"
stocks = [
    {"id": 1, "ticker": "AAPL"}, {"id": 2, "ticker": "TSLA"}, {"id": 3, "ticker": "MSFT"},
    {"id": 4, "ticker": "AMZN"}, {"id": 5, "ticker": "GOOGL"}]


# Set CSV file name dynamically using start and end dates
csv_file_name = f"stock_data_{startDate}_to_{endDate}.csv"

# Check if the file already exists
if os.path.isfile(csv_file_name):
    file_mode = 'a'  # Append mode if file already exists
else:
    file_mode = 'w'  # Write mode if file doesn't exist yet

# Open a CSV file in write mode
with open(csv_file_name, mode=file_mode, newline='') as file:
    writer = csv.writer(file)
    # Write header row
    writer.writerow(['Id', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    
    # Iterate over each stock
    for stock in stocks:
        # Get ticker by name
        ticker = yf.Ticker(stock["ticker"])
        
        # Get historical data for the ticker
        tickerHist = ticker.history(start=startDate, end=endDate, auto_adjust=False)
        
        # Check if tickerHist is empty
        if tickerHist.empty:
            print(f"No historical data found for {stock['ticker']}")
            continue  # Skip to the next stock if no data found
        
        # Iterate over each row in historical data and write to CSV
        for index, row in tickerHist.iterrows():
            writer.writerow([stock["id"], index.strftime('%m/%d/%Y %H:%M:%S'), round(row['Open'],2), round(row['High'],2), round(row['Low'],2), round(row['Close'],2), int(row['Volume'])])

print(f"Stock data has been written to {csv_file_name}")
