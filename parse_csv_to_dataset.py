import re
from pprint import pprint

import numpy as np
import pandas as pandas


def atomic_filter(x: str):
    if x == '':
        return np.nan
    x = x.strip("%₽ ")
    x = x.replace(" ","")
    x = x.replace("q2", "")
    x = x.replace("q3", "")
    x = x.replace("кв2", "")
    return float(x)


def extract(multiplicator, lines, get_first=False):
    _lines = [l for l in lines if l.startswith(multiplicator)]
    if len(_lines) == 0:
        return [np.nan for x in range(10)]
    if not get_first:
        assert len(_lines) == 1
    line = _lines[0]
    ans = line.split(',')[1:]
    ans = [atomic_filter(x) for x in ans]
    return ans


def parse_one_company(lines):
    pe = extract('P/E', lines)
    ep = extract('E/P', lines)
    pb = extract('P/B', lines)
    ps = extract('P/S', lines)
    pcf = extract('P/CF', lines)
    la = extract('L/A', lines)
    nde = extract('NetDebt / EBITDA', lines)
    eve = extract('EV / EBITDA', lines)
    roa = extract('ROA', lines)
    roe = extract('ROE', lines)
    ros = extract('ROS', lines)
    price = extract('Цена ао', lines)
    ears = extract('Отчетный период', lines, get_first=True)
    ears = [e for e in ears if e is not np.nan]
    n_sets = len(ears) - 1

    sets = []
    for i in range(n_sets):
        set = [pe[i], ep[i], pb[i], ps[i], pcf[i], la[i], nde[i], eve[i], roa[i], roe[i], ros[i]]
        delta = ((price[i+1] / price[i]) - 1) * 100
        set.append(delta)
        sets.append(set)
    return sets

def parse_to_dataset()->pandas.DataFrame:
    dataest = []
    columns = ["P/E", "E/P", "P/B", "P/S", "P/CF", "L/A", "NetDebt / EBITDA", "EV / EBITDA", "ROA", "ROE", "ROS", "delta"]
    with open("resources/история мультиплкаторов - Лист1.csv") as inn:
        lines = inn.readlines()
    lines = [x.strip() for x in lines]

    startes = [i for i,l in enumerate(lines) if ')' in l]
    ends = startes[1:] + [len(lines)]
    borders = list(zip(startes, ends))
    # pprint(borders)
    for b, e in borders:
        sets = parse_one_company(lines[b:e])
        dataest += sets

    df = pandas.DataFrame(dataest, columns=columns)
    return df

if __name__ == "__main__":
    df = parse_to_dataset()
    df.to_csv("resources/multipliers_to_cost_increase.csv", index=False)