import numpy
import pandas

from metrics import incom_not_weighted
from process import load_data, transform_multipliers
from transformator import Multiplier, transformators

df = load_data()
delta = df['delta']
dft = transform_multipliers(df)
M = Multiplier
columns = ["P/E", "E/P", "P/B", "P/S", "P/CF", "L/A", "NetDebt / EBITDA", "EV / EBITDA", "ROA", "ROE", "ROS", "delta"]


def find_correlations():
    # df['custom'] = df['delta'] / 100 + 1
    corr = dft.corr()['delta']
    corr = abs(corr)
    print(corr)


if __name__ == "__main__":
    find_correlations()
    s = dft[M.p_to_e]
    print(incom_not_weighted(delta, s, 80))
    print(transformators[M.p_to_b].restore(60))
