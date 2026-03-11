from sqlalchemy import create_engine
import pandas as pd


def load(data_frames):
    engine = create_engine("postgresql://postgres:hakkjj97@localhost:5432/olist")

    data_frames['customers'].to_sql("customers", engine, if_exists='replace')
    data_frames['orders'].to_sql("orders", engine, if_exists='replace')
    data_frames['order_items'].to_sql("order_items", engine, if_exists='replace')
    data_frames['products'].to_sql("products", engine, if_exists='replace')

    print("Loading successfully!")