import os
import pickle
import time
from pprint import pprint

import pandas
import requests
from bs4 import BeautifulSoup


import requests

__current_folder = os.path.dirname(os.path.realpath(__file__))
cache_folder = os.path.join(__current_folder, 'cache')
class NoDataException(Exception):
    pass

def download_page_for_a_ticker(ticker):
    cache_file_name = os.path.join(cache_folder, f"{ticker}.pickle")
    if not os.path.exists(cache_file_name):
        time.sleep(10)
        resp = requests.get(f"https://smart-lab.ru/q/{ticker}/f/y/")
        if "Ошибка: 404" in resp.text:
            raise NoDataException()

        with open(cache_file_name, 'wb') as outt:
            pickle.dump(resp, outt)
    with open(cache_file_name, 'rb') as inn:
        return pickle.load(inn)

def extract_years_columns(df):
    years_line = df.loc[1]
    mapping = {}
    for i,v in enumerate(years_line):
        try:
            val = int(v)
        except:
            continue
        mapping[val] = i
    return mapping


def get_data_for_ticker(ticker):
    resp= download_page_for_a_ticker(ticker)
    df = pandas.read_html(resp.content)
    df = df[0]

    mapping = extract_years_columns(df)

    df_new = pandas.DataFrame()
    for year, col_name in mapping.items():
        df_new[year] = df[col_name]
    df_new['mult'] = df[0]
    df_new = df_new[df_new['mult'].apply(lambda x: isinstance(x, str))]
    df_new = df_new[df_new['mult'].apply(lambda x: ',' in x or '/' in x)]
    df_new.index = df_new['mult']
    del df_new['mult']
    df_new.reset_index()
    return df_new

def normalize_table(df, ticker):
    multiki = []
    for year in df:
        for i in range(len(df)):
            multiki.append([ticker, year, df.index[i], df[year][i]])
    return multiki

if __name__ == "__main__":
    with open("./../supporting/tickers_mmvb") as inn:
        tickers = [x.strip() for x in  inn.readlines()]
        tickers = [x for x in tickers if x != ""]
    for ticker in tickers:
        try:
            print(ticker)
            get_data_for_ticker(ticker)
        except NoDataException:
            print("To Delete: ", ticker)
    #
    # df = get_data_for_ticker('BANEP')
    # print(normalize_table(df, "ZILL"))