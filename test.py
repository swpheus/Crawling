import requests
import time
import pandas as pd
from bs4 import BeautifulSoup

def time_convert(dt):
    time.strptime(dt,'%Y-%m-%d %H:%M:%S')
    s = time.mktime(time.strptime(dt,'%Y-%m-%d %H:%M:%S'))
    return str(int(s))

s = requests.Session()
start = time_convert("2016-07-01 00:00:00")
end   = time_convert("2017-07-21 00:00:00")

r = s.get("https://uk.finance.yahoo.com/quote/BTC-USD/history?period1="+start+"&period2="+end+"&interval=1d&filter=history&frequency=1d")

soup = BeautifulSoup(r.text, 'lxml')
tables = soup.select('table')

df_list = []
for table in tables:
    df_list.append(pd.concat(pd.read_html(table.prettify())))
    df = pd.concat(df_list)
    df.to_excel("E:\PythonData\price_"+'.xlsx')