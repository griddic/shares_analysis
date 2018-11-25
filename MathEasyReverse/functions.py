class FunctionWithReverse:
    def __call__(self, x):
        raise NotImplementedError("Abstract class. Please inherit.")
    def restore(self, y):
        raise NotImplementedError("Abstract class. Please inherit.")

class CompositeFunction(FunctionWithReverse):
    def __init__(self, *functions):
        self.function_chain = functions

    def __call__(self, x):
        for f in self.function_chain:
            x = f(x)
        return x

    def restore(self, y):
        for f in reversed(self.function_chain):
            y = f.restore(y)
        return y

class MyltiplyBy(FunctionWithReverse):
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, x):
        return x * self.multiplier

    def restore(self, y):
        return y / self.multiplier


class Add(FunctionWithReverse):
    def __init__(self, additional):
        self.additional = additional

    def __call__(self, x):
        return x + self.additional

    def restore(self, y):
        return y - self.additional

class RaiseToAPower(FunctionWithReverse):
    def __init__(self, power):
        self.power = power

    def __call__(self, x):
        return x ** self.power

    def restore(self, y):
        return y ** (1/self.power)

