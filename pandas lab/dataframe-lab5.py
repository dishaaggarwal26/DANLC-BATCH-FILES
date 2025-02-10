import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("sales_data1.csv")

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Calculate Total Revenue for the Year
df['Total Revenue'] = df['Quantity'] * df['Price']
total_revenue = df['Total Revenue'].sum()
print(f"Total Revenue for the Year: {total_revenue}")

# Calculate Average Revenue per Sale
average_revenue = df['Total Revenue'].mean()
print(f"Average Revenue per Sale: {average_revenue}")

# Find the Best-Selling Product (based on quantity sold)
best_selling_product = df.groupby('Product Name')['Quantity'].sum().idxmax()
print(f"Best-Selling Product: {best_selling_product}")

# Find the Date with the Highest Total Revenue
date_highest_revenue = df.groupby('Date')['Total Revenue'].sum().idxmax()
print(f"Date with Highest Total Revenue: {date_highest_revenue}")

# Generate a Bar Chart - Total Sales per Product
product_sales = df.groupby('Product Name')['Quantity'].sum()
plt.figure(figsize=(10, 5))
product_sales.plot(kind='bar', color='skyblue')
plt.title("Total Sales per Product")
plt.xlabel("Product Name")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45)
plt.show()

# Generate a Bar Chart - Total Revenue per Product
product_revenue = df.groupby('Product Name')['Total Revenue'].sum()
plt.figure(figsize=(10, 5))
product_revenue.plot(kind='bar', color='lightgreen')
plt.title("Total Revenue per Product")
plt.xlabel("Product Name")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.show()
