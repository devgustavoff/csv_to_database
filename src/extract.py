import pandas as pd
from logger import get_logger

logger = get_logger(__name__)

def extract_olist_data(base_path="data"):
    try:
        logger.info('Start extracting...')

        customers = pd.read_csv(f"{base_path}/olist_customers_dataset.csv")
        orders = pd.read_csv(f"{base_path}/olist_orders_dataset.csv")
        order_items = pd.read_csv(f"{base_path}/olist_order_items_dataset.csv")
        products = pd.read_csv(f"{base_path}/olist_products_dataset.csv")
        
        logger.info('Extract concluded')
        
        return {
            "customers": customers,
            "orders": orders,
            "order_items": order_items,
            "products": products
        }
        
    except FileNotFoundError as e:
        logger.error(f'Extract falied: {e}')
        raise