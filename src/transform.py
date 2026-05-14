import pandas as pd
from logger import get_logger

logger = get_logger(__name__)

def transform(datas_olist):
    try:
        logger.info("Datas transform  started...")

        customers = datas_olist['customers']
        orders = datas_olist['orders']
        orders_items = datas_olist['order_items']
        products = datas_olist['products']

        # DF orders
        orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
        orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
        orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
        orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
        orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

        # DF order_items
        orders_items['shipping_limit_date'] = pd.to_datetime(orders_items['shipping_limit_date'])

        # DF products
        products['product_category_name'] = products['product_category_name'].fillna("sem categoria")

        logger.info("Datas transform concluded.")

        return {
            'customers': customers,
            'orders': orders,
            'order_items': orders_items,
            'products': products
        }
    
    except Exception as e:
        logger.error(f"Ocurred some error: {e}")
        raise