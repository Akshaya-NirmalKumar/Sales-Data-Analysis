import pandas as pd

HEAD
sales_data = {
    "Product": ["Laptop", "Headphones", "Keyboard", "Mouse", "Monitor"],
    "Units Sold": [150, 300, 200, 250, 100],
    "Price": [1000, 50, 30, 20, 200]
}

df = pd.DataFrame(sales_data)

df["Total Sales"] = df["Units Sold"] * df["Price"]

print("Sales Data Analysis")
print(df)
print("\nTotal Revenue: $", df["Total Sales"].sum())
data = pd.read_csv('sales_data.csv')  
print(data.head()) 
print(data.describe()) 
 677c53f6669818dd02b5a0e412b0dfab1956d434
