import pandas as pd

# ----------------------------
# 1. Load dataset
# ----------------------------
df = pd.read_csv("transactions.csv")

# ----------------------------
# 2. Clean column names
# ----------------------------
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
# If BOM exists in first column, fix it
df.columns = [col.replace('\ufeff','') for col in df.columns]

# ----------------------------
# 3. Inspect data
# ----------------------------
print("First 5 rows:\n", df.head(), "\n")
print("Info:\n", df.info(), "\n")
print("Describe:\n", df.describe(), "\n")

# ----------------------------
# 4. Clean data
# ----------------------------
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# ----------------------------
# 5. Add TotalAmount column
# ----------------------------
df["TotalAmount"] = df["Quantity"] * df["Price"]

# ----------------------------
# 6. Top 5 most purchased products
# ----------------------------
top_products = (
    df.groupby("ProductID")["Quantity"]
      .sum()
      .reset_index()
      .sort_values(by="Quantity", ascending=False)
      .head(5)
)
top_products.to_csv("top_products.csv", index=False)
print("✅ top_products.csv created")

# ----------------------------
# 7. Customers with highest spending
# ----------------------------
top_customers = (
    df.groupby("CustomerID")["TotalAmount"]
      .sum()
      .reset_index()
      .sort_values(by="TotalAmount", ascending=False)
)
top_customers.to_csv("top_customers.csv", index=False)
print("✅ top_customers.csv created")

# ----------------------------
# 8. Average transaction value
# ----------------------------
avg_transaction = df["TotalAmount"].mean()
print(f"Average Transaction Value: {round(avg_transaction,2)}")

# ----------------------------
# 9. Revenue contribution by product category
# ----------------------------
category_revenue = (
    df.groupby("ProductCategory")["TotalAmount"]
      .sum()
      .reset_index()
      .sort_values(by="TotalAmount", ascending=False)
)
category_revenue.to_csv("category_revenue.csv", index=False)
print("✅ category_revenue.csv created")

# ----------------------------
# 10. Summary statistics
# ----------------------------
summary_stats = {
    "Total Transactions": [df["TransactionID"].nunique()],
    "Total Customers": [df["CustomerID"].nunique()],
    "Average Transaction Value": [round(avg_transaction, 2)],
    "Total Revenue": [df["TotalAmount"].sum()]
}
summary_stats_df = pd.DataFrame(summary_stats)
summary_stats_df.to_csv("summary_stats.csv", index=False)
print("✅ summary_stats.csv created")

print("\n🎉 Analysis complete! All CSV files are ready for the dashboard.")

