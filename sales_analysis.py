import pandas as pd
df = pd.read_csv("C:\\Users\\manda\\Downloads\\sales_data.csv")

print("\n--- DATA INFO ---")
print(df.head()) # Returns the first four rows
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData Types:")
print(df.dtypes)

print("\n--- CLEANING DATA ---")
print("\nMissing values before cleaning:")
print(df.isna().sum())

numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[nuSAmeric_cols].fillna(0)
df = df.drop_duplicates()

print("\nMissing values after cleaning:")
print(df.isna().sum())

# TOTAL REVENUE

print("\n--- ANALYSIS ---")
total_revenue = df['Total_Sales'].sum()

##  BEST PRODUCT ANALYSIS

product_sales = df.groupby('Product')['Total_Sales'].sum()
best_product = product_sales.idxmax()

##AVERAGE ORDER

average_order = df['Total_Sales'].mean()

## OVERALL SALES REPORT

print("\n=== SALES REPORT ===")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best-Selling Product: {best_product}")
print(f"Average Order Value: ₹{average_order:,.2f}")
print("\nInsights:")
print("- Revenue looks healthy — monitor trends over time.")
print("- Best-seller shows where demand is highest.")
print("- Consider improving products with low contribution.")
