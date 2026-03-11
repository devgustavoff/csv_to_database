import pandas as pd

def extract_olist_data(base_path="data"):
    customers = pd.read_csv(f"{base_path}/olist_customers_dataset.csv")
    orders = pd.read_csv(f"{base_path}/olist_orders_dataset.csv")
    order_items = pd.read_csv(f"{base_path}/olist_order_items_dataset.csv")
    products = pd.read_csv(f"{base_path}/olist_products_dataset.csv")

    return {
        "customers": customers,
        "orders": orders,
        "order_items": order_items,
        "products": products
    }
