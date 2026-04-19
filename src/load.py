from sqlalchemy import create_engine
import os


def load(data_frames):
    engine = create_engine(os.getenv("DB_URL"))

    data_frames['customers'].to_sql("customers", engine, if_exists='replace')
    data_frames['orders'].to_sql("orders", engine, if_exists='replace')
    data_frames['order_items'].to_sql("order_items", engine, if_exists='replace')
    data_frames['products'].to_sql("products", engine, if_exists='replace')

    print("Loading successfully!")