from extract import extract_olist_data
from transform import transform
from load import load
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))), ".env"))

olist_datas = extract_olist_data()
olist_data_frames = transform(olist_datas)
load(olist_data_frames)