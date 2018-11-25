from MathEasyReverse.functions import FunctionWithReverse



class LessThenTo(FunctionWithReverse):
    def __init__(self, threshold, target):
        if target < threshold:
            raise ValueError(f"Reverse transformation will be imposible if target {target} "
                             f"is less then threshold {threshold}")
        self.threshold = threshold
        self.target = target

    def __call__(self, x):
        if x < self.threshold:
            return self.target
        return x

    def restore(self, y):
        if y < self.threshold:
            raise ValueError(f"Value {y} was imposible to obtain. It is less then threshold {self.threshold}.")
        return y

class MoreThenTo(FunctionWithReverse):
    def __init__(self, threshold, target):
        if target > threshold:
            raise ValueError(f"Reverse transformation will be imposible if target {target} "
                             f"is more then threshold {threshold}")
        self.threshold = threshold
        self.target = target

    def __call__(self, x):
        if x > self.threshold:
            return self.target
        return x

    def restore(self, y):
        if y > self.threshold:
            raise ValueError(f"Value {y} was imposible to obtain. It is more then threshold {self.threshold}.")
        return y
