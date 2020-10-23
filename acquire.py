import pandas as pd
import requests

def new_payload_items_data():
    response = requests.get('https://python.zach.lol/api/v1/items')
    data = response.json()
    df = pd.DataFrame(data['payload']['items'])
    df.to_csv('new_items_df.csv')
    return df

def new_payload_stores_data():
    response = requests.get('https://python.zach.lol/api/v1/items')
    data = response.json()
    df = pd.DataFrame(data['payload']['stores'])
    df.to_csv('new_stores_df.csv')
    return df

def new_payload_sales_data():
    response = requests.get('https://python.zach.lol/api/v1/items')
    data = response.json()
    df = pd.DataFrame(data['payload']['sales'])
    df.to_csv('new_sales_df.csv')
    return df