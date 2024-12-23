import pandas as pd

# Load your dataset
data = pd.read_csv('sales_data.csv')  # Make sure to replace with your file path

# Basic data overview
print(data.head())  # Shows the first 5 rows of the data
print(data.describe())  # Shows summary statistics
