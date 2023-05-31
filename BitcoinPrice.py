import requests
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime
import calendar
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from colorama import Fore
from dateutil.relativedelta import relativedelta



try:
    # Try importing as tkinter.messagebox (Python 3.x)
    import tkinter.messagebox as messagebox
except ImportError:
    # Fallback to importing as tkMessageBox (Python 2.x)
    import tkMessageBox as messagebox

def fetch_bitcoin_prices(start_date, end_date):
    url = f"https://api.coindesk.com/v1/bpi/historical/close.json?start={start_date}&end={end_date}"
    response = requests.get(url)
    data = response.json()
    print(f"{Fore.RED}")

    print(data)
    print(f"{Fore.WHITE}")
    return data['bpi']

def plot_bitcoin_prices(prices):
    dates = list(prices.keys())
    values = list(prices.values())

    # Convert dates to datetime objects
    dates = [datetime.strptime(date, "%Y-%m-%d") for date in dates]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, values)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Bitcoin Price Chart')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


def fetch_and_plot_prices():
    start_date = cal_start.get_date()
    end_date = cal_end.get_date()
    current_date = datetime.now().date()

    num_days = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days
    three_months_ago = current_date - relativedelta(months=3)

    # Check if the range is at least 30 days
    if datetime.strptime(end_date, "%Y-%m-%d") < datetime.strptime(start_date, "%Y-%m-%d"):
        messagebox.showerror("Error", "End date can't be less than start date")
        return
    elif num_days < 200:
        messagebox.showerror("Error", "Please select a date range of at least 200 days.")
        return
    elif datetime.strptime(end_date, "%Y-%m-%d").date() > three_months_ago:
        messagebox.showerror("Error", "Please make sure the selected date range is older than 3 months from today.")
        return

    prices = fetch_bitcoin_prices(start_date, end_date)
    plot_bitcoin_prices(prices)

# Create the main window
window = tk.Tk()
window.title("Bitcoin Price Chart")
window.geometry("800x800")

# Create calendar widgets for start and end dates
cal_start = Calendar(window, selectmode="day", date_pattern="yyyy-mm-dd")
cal_start.grid(row=0, column=0, padx=10, pady=10)
cal_end = Calendar(window, selectmode="day", date_pattern="yyyy-mm-dd")
cal_end.grid(row=1, column=0, padx=10, pady=10)

# Create a button to fetch and plot prices
btn_fetch = ttk.Button(window, text="Fetch and Plot", command=fetch_and_plot_prices)
btn_fetch.grid(row=2, column=0, padx=10, pady=10)

# Run the GUI main loop
window.mainloop()