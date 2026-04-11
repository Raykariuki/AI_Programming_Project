# Import Python Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display first rows
print("first 5 rows:")
print(df.head())

# Data Cleaning
print("\nChecking for missing values:")
print(df.isnull().sum())

# Simple statistics
print("\nDiscriptive statistics:")
print(df.describe())

# Create total sales column
df['Total_Sales'] = df['Price'] * df['Quantity']

# Display The Total sales column
print("\nUpdated Dataset with Total Sales:")
print(df.head())

# Total Revenue
total_revenue = df['Total_Sales'].sum()
print("\ntotal Revenue:", total_revenue)

# Average Sales
average_sales = df['Total_Sales'].mean()
print("Average Sales:", average_sales)

# Sales by Category
category_sales = df.groupby('Category')['Total_Sales'].sum()
print("\nSales by Category:")
print(category_sales)

# Visualization
plt.figure()
category_sales.plot(kind='bar')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()