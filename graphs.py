from imports import plt, mdates
from datetime import datetime

def graphs_rendering(og_data, autocorrelation_data):

    # MONTHLY NATURAL GAS PRICES GRAPH

    # Convert dates to datetime format and extract prices
    x_1 = [datetime.strptime(item[0], "%Y-%m") for item in og_data]
    y_1 = [item[1] for item in og_data]

    x_2 = [item[0] for item in autocorrelation_data]
    y_2 = [item[1] for item in autocorrelation_data]

    # Create a figure with two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))  # 1 row, 2 columns

    # First graph
    ax1.plot(x_1, y_1, color='pink', marker='o', linewidth=2, markersize=4)
    ax1.xaxis.set_major_locator(mdates.YearLocator(2)) # every 2 years
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax1.set_title("Signal")
    ax1.grid(True)
    ax1.tick_params(axis='x', rotation=45)

    # Second graph
    ax2.plot(x_2, y_2, color='purple', marker='o', linewidth=2, markersize=4)
    ax2.set_title("Autocorrelation function")
    ax2.grid(True)
    #ax2.tick_params(axis='x', rotation=45)

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()




    '''# Plotting
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, prices, color='blue', marker='o', linewidth=2, label='Natural Gas Prices')

    # Format x-axis for dates
    ax.xaxis.set_major_locator(mdates.YearLocator(2)) # every 2 years
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45)

    # Title and labels
    ax.set_title("Natural Gas Prices Over Time", fontsize=14)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Price", fontsize=12)

    # Add grid and legend
    ax.grid(True)

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()'''
    