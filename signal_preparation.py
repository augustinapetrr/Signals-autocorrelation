from imports import pd

# MONTHLY NATURAL GAS PRICES
def get_data_gas():
    # Load the uploaded CSV file
    file_path = "data/monthly_natural_gas_prices.csv"
    df = pd.read_csv(file_path)

    # Convert 'Month' column to datetime format
    #df['Month'] = pd.to_datetime(df['Month'])

    gas_data = []

    for i in range(df.shape[0]):
        gas_data.append([df['Month'][i], df['Price'][i]])

    return gas_data