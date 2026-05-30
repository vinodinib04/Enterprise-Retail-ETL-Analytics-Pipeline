import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///../retail.db")

df = pd.read_sql("SELECT * FROM sales LIMIT 5", engine)

print(df)