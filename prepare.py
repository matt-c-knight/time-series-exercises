import pandas as pd

def prep(df):
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')
    df = df.set_index('sale_date').sort_index()
    df['month'] = df.index.month
    df['day_of_week'] = df.index.dayofweek
    df['sales_total'] = df.sale_amount * df.item_price
    return df

def germany_prep():
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index('Date').sort_index()
    df['month'] = df.index.month
    df['year'] = df.index.year
    df.Wind.fillna(0, inplace=True)
    df.Solar.fillna(0, inplace=True)
    df['Wind+Solar'].fillna(0, inplace=True)
    return df