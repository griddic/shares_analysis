from enum import Enum, EnumMeta

from MathEasyReverse.functions import CompositeFunction, MyltiplyBy, RaiseToAPower, FunctionWithReverse, Add
from MathEasyReverse.loss_transformations import LessThenTo, MoreThenTo


class Multiplier(Enum):
    p_to_e = "P/E"
    e_to_p = "E/P"
    p_to_b = "P/B"
    p_to_s = "P/S"
    p_to_cf = "P/CF"
    l_to_a = "L/A"
    netDebt_to_ebitda = "NetDebt / EBITDA"
    ev_to_ebitda = "EV / EBITDA"
    roa = "ROA"
    roe = "ROE"
    ros = "ROS"

    @classmethod
    def contains(cls, value):
        return any(value == item.value for item in cls)

def construct_bender(power=1., norm_max=100.):
    return CompositeFunction(MyltiplyBy(1./norm_max),
                             RaiseToAPower(power),
                             MyltiplyBy(norm_max))

def construct_linear(shift, multiplier, revers = False):
    return CompositeFunction(MyltiplyBy(-1 if revers else 1),
                             Add(shift),
                             MyltiplyBy(multiplier))

p_to_e_atomic_transformator = CompositeFunction(
    LessThenTo(0, 33),
    MoreThenTo(33,33),
    construct_linear(34, 3, True),
    construct_bender(4)
)

e_to_p_atomic_transformator = LessThenTo(0,0)

p_to_b_const = 5
p_to_b_atomic_transformator = CompositeFunction(
    LessThenTo(0, p_to_b_const),
    MoreThenTo(p_to_b_const, p_to_b_const),
    construct_linear(p_to_b_const, 20, True),
    construct_bender(3)
)

p_to_s_atomic_transformator = CompositeFunction(
    LessThenTo(0, 5),
    MoreThenTo(5, 5),
    construct_linear(5, 20, True),
    construct_bender(3)
)

p_to_cf_atomic_transformator = CompositeFunction(
    LessThenTo(0,30),
    MoreThenTo(30,30),
    construct_linear(30, 3, True),
    construct_bender(1.5)
)

l_to_a_atomic_transformator = CompositeFunction(
    LessThenTo(0, 100),
    MoreThenTo(100,100),
    construct_linear(100, 1, True)
)

net_debt_to_ebitda_atomic_transformator = CompositeFunction(
    LessThenTo(0, 5),
    MoreThenTo(5, 5),
    construct_linear(5, 20, True),
    construct_bender(3)
)

ev_to_ebitda_atomic_transformator = CompositeFunction(
    LessThenTo(0, 33),
    MoreThenTo(33, 33),
    construct_linear(34, 3, True),
    construct_bender(4)
)

roa_atomic_transformator = Add(0)

roe_atomic_transformator = Add(0)

ros_atomis_transformator = Add(0)

transformators = {
    Multiplier.p_to_e: p_to_e_atomic_transformator,
    Multiplier.e_to_p: e_to_p_atomic_transformator,
    Multiplier.p_to_b: p_to_b_atomic_transformator,
    Multiplier.p_to_s: p_to_s_atomic_transformator,
    Multiplier.p_to_cf: p_to_cf_atomic_transformator,
    Multiplier.l_to_a: l_to_a_atomic_transformator,
    Multiplier.netDebt_to_ebitda: net_debt_to_ebitda_atomic_transformator,
    Multiplier.ev_to_ebitda: ev_to_ebitda_atomic_transformator,
    Multiplier.roa: roa_atomic_transformator,
    Multiplier.roe: roe_atomic_transformator,
    Multiplier.ros: ros_atomis_transformator
}

if __name__ == "__main__":
    v = 10
    tr = construct_bender(3, 100)
    v_t = tr(v)
    v_r = tr.restore(v_t)
    print(v, v_t, v_r)