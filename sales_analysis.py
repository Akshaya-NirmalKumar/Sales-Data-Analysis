import pandas as pd

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
