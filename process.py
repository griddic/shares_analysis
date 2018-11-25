import pandas

from transformator import Multiplier, transformators


def load_data():
    df = pandas.read_csv("resources/multipliers_to_cost_increase.csv")
    df.fillna(0, inplace=True)
    columns_original = df.columns
    # columns_enum = []
    # for c in columns_original:
    #     if Multiplier.contains(c):
    #         columns_enum.append(Multiplier(c))
    #     else:
    #         columns_enum.append(c)
    columns_enum = [(Multiplier(c) if Multiplier.contains(c) else c) for c in columns_original]
    df.columns = columns_enum
    return df

def transform_multipliers(df):
    dft = pandas.DataFrame()
    for m in Multiplier:
        dft[m] = df[m].apply(transformators[m])
    dft['delta'] = df['delta']
    return dft