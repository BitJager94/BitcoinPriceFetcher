# Code Documentation - Bitcoin Price Chart

This Python script allows users to fetch and plot historical Bitcoin prices using the CoinDesk API. The script utilizes the `requests`, `matplotlib`, `datetime`, `calendar`, `tkinter`, `tkcalendar`, and `colorama` libraries.

## Requirements

To run this code, the following packages need to be installed:

- `requests`
- `matplotlib`
- `datetime`
- `calendar`
- `tkinter`
- `tkcalendar`
- `colorama`

Make sure these packages are installed in your Python environment.

## Functionality

### `fetch_bitcoin_prices(start_date, end_date)`

This function fetches historical Bitcoin prices from the CoinDesk API within the specified date range. It takes the `start_date` and `end_date` as parameters and returns the Bitcoin price data in the form of a dictionary.

### `plot_bitcoin_prices(prices)`

This function plots the Bitcoin prices using the `matplotlib` library. It takes the `prices` dictionary as input, where the keys represent the dates and the values represent the corresponding Bitcoin prices. It generates a line chart with dates on the x-axis and prices on the y-axis.

### `fetch_and_plot_prices()`

This function is the callback function for the "Fetch and Plot" button. It retrieves the selected start and end dates from the calendar widgets, validates the date range, and fetches the Bitcoin prices using the `fetch_bitcoin_prices()` function. If the date range is valid, it proceeds to plot the prices using the `plot_bitcoin_prices()` function. If any error occurs during the validation process, an error message is displayed using the `messagebox` module from `tkinter`.

## GUI

The script creates a graphical user interface (GUI) using the `tkinter` library. The GUI consists of the following components:

- Two calendar widgets for selecting the start and end dates.
- A "Fetch and Plot" button to trigger the fetching and plotting of Bitcoin prices.

## Usage

To use the script, simply run it as a Python script. The GUI window will appear, allowing you to select the desired start and end dates using the calendar widgets. Click the "Fetch and Plot" button to fetch and plot the historical Bitcoin prices.

**Note:** Make sure to have the required packages installed before running the script.