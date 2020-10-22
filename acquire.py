import pandas as pd

def new_payload_data():
    df = pd.DataFrame(data['payload']['items'])
    df.to_csv('new_zillow_df.csv')
    return df