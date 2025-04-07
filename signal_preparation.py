from imports import pd

def get_data(file_path, column1, column2):
    # Load the uploaded CSV file
    df = pd.read_csv(file_path)
    data = []

    for i in range(df.shape[0]):
        data.append([df[column1][i], df[column2][i]])

    return data


'''# Swiss Francs to U.S. Dollar Spot Exchange Rate
def get_data_exchange_rate():
    # Load the uploaded CSV file
    file_path = "data/DEXSZUS.csv"
    df = pd.read_csv(file_path)

    rate_data = []

    for i in range(df.shape[0]):
        rate_data.append([df['observation_date'][i], df['DEXSZUS'][i]])

    return rate_data

# MONTHLY NATURAL GAS PRICES
def get_data_gas():
    # Load the uploaded CSV file
    file_path = "data/monthly_natural_gas_prices.csv"
    df = pd.read_csv(file_path)

    gas_data = []

    for i in range(df.shape[0]):
        gas_data.append([df['Month'][i], df['Price'][i]])

    return gas_data'''