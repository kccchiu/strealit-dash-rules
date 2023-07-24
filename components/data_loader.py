import pandas as pd

# Function to load data from CSV files
def load_data(category, rule):
    file_path = f"data/{category}/{rule}.csv"
    data = pd.read_csv(file_path)
    return data
