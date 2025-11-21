import pandas as pd
from sqlalchemy import create_engine, text
from config import DB_URL

engine = create_engine(DB_URL)

def load_to_db(df):
    with engine.begin() as conn:
        df.to_sql("sales", conn, if_exists="append", index=False)

def process_new_data():
    df = pd.read_csv("data/stream.csv", names=["timestamp","product","category","quantity","price","total"])
    load_to_db(df)
    print("Inserted:", len(df), "records")

if __name__ == "__main__":
    process_new_data()
