from sqlalchemy import create_engine
from logger import get_logger
import os

logger = get_logger(__name__)

def load(data_frames):

    try:
        engine = create_engine(os.getenv("DB_URL"))
        logger.info("Datas load start..")
        data_frames['customers'].to_sql("customers", engine, if_exists='replace')
        data_frames['orders'].to_sql("orders", engine, if_exists='replace')
        data_frames['order_items'].to_sql("order_items", engine, if_exists='replace')
        data_frames['products'].to_sql("products", engine, if_exists='replace')
        logger.info("Datas load conclued")
    except Exception as e:
        logger.error(f"Ocurred some error: {e}")
        raise