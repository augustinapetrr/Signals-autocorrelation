from imports import plt, mdates
from datetime import datetime

def graphs_rendering(og_data, autocorrelation_data, ax2_xlabel, years):

    # Convert dates to datetime format and extract other values
    x_1 = [datetime.strptime(str(item[0]), "%Y-%m") if len(str(item[0])) == 7 else datetime.strptime(str(item[0]), "%Y-%m-%d") if len(str(item[0])) == 10 else datetime.strptime(str(item[0]), "%Y") for item in og_data]
    y_1 = [item[1] for item in og_data]

    x_2 = [item[0] for item in autocorrelation_data]
    y_2 = [item[1] for item in autocorrelation_data]

    # Create a figure with two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))  # 1 row, 2 columns

    # First graph
    ax1.plot(x_1, y_1, color='pink', marker='o', linewidth=2, markersize=4)
    ax1.xaxis.set_major_locator(mdates.YearLocator(years))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax1.set_title("Signal")
    ax1.grid(True)
    ax1.tick_params(axis='x', rotation=45)

    # Second graph
    ax2.plot(x_2, y_2, color='purple', marker='o', linewidth=2, markersize=4)
    ax2.set_title("Autocorrelation function")
    ax2.grid(True)
    ax2.set_xlabel(ax2_xlabel, fontsize=12)

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()    