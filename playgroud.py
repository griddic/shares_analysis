import numpy

from process import load_data, transform_multipliers
from transformator import Multiplier

df = load_data()
delta = df['delta']
dft = transform_multipliers(df)
M = Multiplier
columns = ["P/E", "E/P", "P/B", "P/S", "P/CF", "L/A", "NetDebt / EBITDA", "EV / EBITDA", "ROA", "ROE", "ROS", "delta"]

if __name__ == "__main__":
    for i in range(0, 100, 10):
        indexes = (dft[M.p_to_b] > i) & (dft[M.netDebt_to_ebitda] > 50)
        incoms = delta[indexes]
        print(i, len(incoms), numpy.mean(incoms))


