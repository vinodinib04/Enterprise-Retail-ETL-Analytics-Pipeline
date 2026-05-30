import pandas as pd
from sqlalchemy import create_engine
import logging
import os

# Create logs folder
os.makedirs("../logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename='../logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Read cleaned dataset
df = pd.read_csv("data/cleaned_superstore.csv")

# SQLite connection
engine = create_engine("sqlite:///../retail.db")

try:
    # Read existing data
    existing_df = pd.read_sql("SELECT * FROM sales", engine)

    # Incremental loading
    new_data = df[~df['Order_ID'].isin(existing_df['Order_ID'])]

    if len(new_data) > 0:
        # Insert only new rows
        new_data.to_sql("sales", engine, if_exists="append", index=False)

        print(f"{len(new_data)} new records inserted")
        logging.info(f"{len(new_data)} new records inserted")

    else:
        print("No new records found")
        logging.info("No new records found")

except:
    # Create table first time
    df.to_sql("sales", engine, if_exists="replace", index=False)

    print("Initial database created")
    logging.info("Initial database created")