import pandas as pd
import matplotlib.pyplot as plt

# Function to generate dummy data if the CSV file is not available
def generate_dummy_data():
    data = {
        'SalesDate': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
        'ProductName': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B'],
        'Region': ['North', 'South', 'East', 'West', 'North'],
        'SalesQuantity': [10, 15, 7, 12, 5],
        'Price': [100, 150, 120, 90, 200]
    }
    df = pd.DataFrame(data)
    df['SalesDate'] = pd.to_datetime(df['SalesDate'])  # Ensure correct date format
    return df

# Load data from CSV file, or use dummy data if file not found
try:
    df = pd.read_csv('sales_data.csv')
    df['SalesDate'] = pd.to_datetime(df['SalesDate'])  # Ensure correct date format
except FileNotFoundError:
    print("CSV file not found. Using dummy data.")
    df = generate_dummy_data()

# Calculate total sales price (SalesQuantity * Price)
df['TotalSalesPrice'] = df['SalesQuantity'] * df['Price']

# Total sales price per region
region_sales = df.groupby('Region')['TotalSalesPrice'].sum()

# Plot 1: Bar chart of total sales price per region
plt.figure(figsize=(10, 6))
region_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales Price per Region')
plt.xlabel('Region')
plt.ylabel('Total Sales Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Plot 2: Pie chart of sales price distribution across regions
plt.figure(figsize=(8, 8))
region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#ff9999', '#99ff99', '#ffcc99'])
plt.title('Percentage Distribution of Sales Price by Region')
plt.ylabel('')  # Hide y-label for better presentation
plt.tight_layout()

# Plot 3: Line chart showing the trend of prices over time
# Aggregating data by date for line chart (using mean price per day for simplicity)
date_price = df.groupby('SalesDate')['Price'].mean()

plt.figure(figsize=(10, 6))
date_price.plot(kind='line', marker='o', color='purple')
plt.title('Price Trend Over Time')
plt.xlabel('Sales Date')
plt.ylabel('Average Price')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show all plots
plt.show()
