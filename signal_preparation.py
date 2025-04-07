from imports import pd

def get_data(file_path, column1, column2):
    # Load the uploaded CSV file
    df = pd.read_csv(file_path)
    data = []

    for i in range(df.shape[0]):
        data.append([df[column1][i], df[column2][i]])

    return data