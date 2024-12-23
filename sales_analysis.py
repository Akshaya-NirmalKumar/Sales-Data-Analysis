import pandas as pd

<<<<<<< HEAD
# Load sales data
sales_data = {
    "Product": ["Laptop", "Headphones", "Keyboard", "Mouse", "Monitor"],
    "Units Sold": [150, 300, 200, 250, 100],
    "Price": [1000, 50, 30, 20, 200]
}

df = pd.DataFrame(sales_data)

# Calculate total sales
df["Total Sales"] = df["Units Sold"] * df["Price"]

print("Sales Data Analysis")
print(df)
print("\nTotal Revenue: $", df["Total Sales"].sum())
=======
# Load your dataset
data = pd.read_csv('sales_data.csv')  # Make sure to replace with your file path

# Basic data overview
print(data.head())  # Shows the first 5 rows of the data
print(data.describe())  # Shows summary statistics
>>>>>>> 677c53f6669818dd02b5a0e412b0dfab1956d434
