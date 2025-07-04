from imports import plt, mdates, np, locale
from datetime import datetime

def graphs_rendering(og_data, autocorrelation_data, ax2_xlabel, years):

    # Set Lithuanian locale
    locale.setlocale(locale.LC_TIME, 'lt_LT.UTF-8')

    # Convert dates to datetime format and extract other values
    x_1 = [datetime.strptime(str(item[0]), "%Y-%m") if len(str(item[0])) == 7 else datetime.strptime(str(item[0]), "%Y-%m-%d") if len(str(item[0])) == 10 else datetime.strptime(str(item[0]), "%Y") for item in og_data]
    y_1 = [item[1] for item in og_data]

    x_2 = [item[0] for item in autocorrelation_data]
    y_2 = [item[1] for item in autocorrelation_data]

    # Create a figure with two subplots side by side
    plt.rcParams.update({
        'axes.titlesize': 20,
        'axes.labelsize': 16,
        'xtick.labelsize': 13,
        'ytick.labelsize': 13
    })
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))  # 1 row, 2 columns
    

    # First graph
    ax1.plot(x_1, y_1, color='pink', linewidth=1.5)
    ax1.xaxis.set_major_locator(mdates.YearLocator(years))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax1.set_title("Signalas")
    ax1.grid(True)
    ax1.tick_params(axis='x', rotation=45)

    # Second graph
    ax2.plot(x_2, y_2, color='purple', linewidth=1.5)
    ax2.set_title("Autokoreliacijos funkcija")
    ax2.grid(True)
    ax2.set_xlabel(ax2_xlabel, fontsize=16)

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()    