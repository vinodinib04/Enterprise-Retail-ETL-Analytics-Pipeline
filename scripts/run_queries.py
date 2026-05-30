import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite database
engine = create_engine("sqlite:///../retail.db")

# Query 1
query1 = '''
SELECT Region, SUM(Sales) AS TotalSales
FROM sales
GROUP BY Region
'''

df1 = pd.read_sql(query1, engine)

print("\nRegion-wise Sales")
print(df1)

# Query 2
query2 = '''
SELECT Product_Name, SUM(Sales) AS TotalSales
FROM sales
GROUP BY Product_Name
ORDER BY TotalSales DESC
LIMIT 10
'''

df2 = pd.read_sql(query2, engine)

print("\nTop Selling Products")
print(df2)

# Query 3
query3 = '''
SELECT Month, SUM(Sales) AS Revenue
FROM sales
GROUP BY Month
ORDER BY Month
'''

df3 = pd.read_sql(query3, engine)

print("\nMonthly Revenue")
print(df3)

# Query 4
query4 = '''
SELECT Category, SUM(Profit) AS TotalProfit
FROM sales
GROUP BY Category
'''

df4 = pd.read_sql(query4, engine)

print("\nCategory-wise Profit")
print(df4)

print("\nAll Queries Executed Successfully")