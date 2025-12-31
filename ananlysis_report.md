# Sales Data Analysis

A concise Python project that demonstrates loading, cleaning, and analysing sales data to produce actionable business metrics such as total revenue, best‑selling products, and average order value.

## Contents
- `sales_analysis.py` — Main Python script that loads the dataset, performs cleaning, computes core metrics, and prints results.
- `sales_data.csv` — Sales dataset (replace with your URL or local path).
- `README.md` — Project documentation.

## Quick start

1. Clone the repository:
   git clone https://github.com/kanth072/Pandas.git

2. Install dependencies (recommended to use a virtual environment):
   pip install pandas

3. Update the dataset path in `sales_analysis.py`:
   - Replace the placeholder URL with the path or URL to your `sales_data.csv`.

4. Run the analysis:
   python sales_analysis.py

## What the script does (high level)
1. Load the dataset into a pandas DataFrame.
2. Inspect basic structure (first rows, shape, column names, dtypes).
3. Clean the data:
   - Report missing values.
   - Replace missing numeric values with 0.
   - Remove duplicate rows.
4. Compute key metrics:
   - Total revenue (sum of `Total_Sales`).
   - Revenue per product and best‑selling product.
   - Average order value (mean of `Total_Sales`).
5. Print formatted results and brief insights.

## Example core logic (summary)
- Read CSV: `df = pd.read_csv(path_or_url)`
- Identify numeric columns and fill missing values:  
  `numeric_cols = df.select_dtypes(include="number").columns`  
  `df[numeric_cols] = df[numeric_cols].fillna(0)`
- Remove duplicates: `df = df.drop_duplicates()`
- Metrics:  
  `total_revenue = df['Total_Sales'].sum()`  
  `product_sales = df.groupby('Product')['Total_Sales'].sum()`  
  `best_product = product_sales.idxmax()`  
  `average_order = df['Total_Sales'].mean()`

Formatted output examples:
- Total Revenue: ₹1,234,567.89
- Best-Selling Product: Widget A
- Average Order Value: ₹1,234.56

## Notes & recommendations
- Ensure `Total_Sales` and `Product` columns exist and are correctly typed.
- For production analysis, consider:
  - Handling missing categorical data (e.g., imputation or removal).
  - Preserving original timestamps to allow time-series analysis.
  - Validating currency/locale formatting.
  - Adding unit tests and logging for reproducibility.


