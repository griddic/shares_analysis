import pandas
from sklearn import datasets, linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from metrics import incom_not_weighted


def lin_regr(threshhold=30):
    df = pandas.read_csv("resources/multipliers_to_cost_increase.csv")
    df.fillna(0, inplace=True)
    # df['custom'] = df['delta'] / 100 + 1
    train, test = train_test_split(df, test_size=0.3)

    x_train = train.copy()
    del x_train['delta']
    y_train = train['delta']

    x_test = test.copy()
    del x_test['delta']
    y_test = test['delta']

    # objects = df.copy()
    # del objects['delta']
    # target = df['delta']
    # objects.fillna(0, inplace=True)

    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    predicted = regr.predict(x_test)
    return incom_not_weighted(y_test, predicted, threshhold)
    # print(target.corr(pandas.Series(predicted)))

def rand_tree(depth, est):
    df = pandas.read_csv("resources/multipliers_to_cost_increase.csv")
    df.fillna(0, inplace=True)


    train, test = train_test_split(df, test_size=0.2)

    x_train = train.copy()
    del x_train['delta']
    y_train = (train['delta'] / 10).astype(int)

    x_test = test.copy()
    del x_test['delta']
    y_test = (test['delta'] / 10).astype(int)

    # Random Forest Model
    rf_model = RandomForestClassifier(max_depth=depth, n_estimators=est)
    rf_model.fit(x_train, y_train)
    predicted = rf_model.predict(x_test) * 10
    return incom_not_weighted(y_test, predicted)

    # return y_test.corr(pandas.Series(predicted))


if __name__ == "__main__":
    # max = 0
    # for i in range(1,10):
    #     for j in range(1,10):
    #         corr = rand_tree(i, j)
    #         if corr > max:
    #             max = corr
    #             print(i,j, corr)
    #
    for th in range(0,100,10):
        income = lin_regr(th)
        print(th, income)