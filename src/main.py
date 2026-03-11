from extract import extract_olist_data
from transform import transform
from load import load

olist_datas = extract_olist_data()
olist_data_frames = transform(olist_datas)
load(olist_data_frames)