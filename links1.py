
import pandas
import pandas as pd
import numpy as np
import pickle
import time
import bs4
import requests

if __name__ == "__main__":

    links_df = pd.read_csv('D:\shaw_flooring\links.csv',
                      usecols=["links"])

    for 

    res = requests.get(lin)
    soup = bs4.BeautifulSoup(res.text)
    for link in soup.select('a[property="schema:url"]'):
    print link.get('href')
