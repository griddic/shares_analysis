import numpy
from scipy.stats import gmean


def income_by_filter(actual_delta, predicted, filter = lambda x: True):
    indexes = predicted.apply(filter)
    to_buy = actual_delta[indexes]
    if len(to_buy) == 0:
        return 0
    return numpy.mean(to_buy)


def incom_not_weighted(actual_delta, predicted, threshold=30):
    actual_delta = numpy.array(actual_delta)
    predicted = numpy.array(predicted)
    indexes = numpy.where(predicted > threshold)
    to_buy = actual_delta[indexes]
    if len(to_buy) < 3:
        return None
    return (gmean((to_buy / 100) + 1) - 1) * 100
    # return numpy.mean(to_buy)

if __name__ == "__main__":
    income = incom_not_weighted([10,20,30,40], [25,34,31,2])
    print(income)
