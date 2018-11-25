# from enum import Enum, EnumMeta
#
#
# class Multiplier(Enum):
#     p_to_e = "P/E"
#     e_to_p = "E/P"
#     p_to_b = "P/B"
#     p_to_s = "P/S"
#     p_to_cf = "P/CF"
#     l_to_a = "L/A"
#     netDebt_to_ebitda = "NetDebt / EBITDA"
#     ev_to_ebitda = "EV / EBITDA"
#     roa = "ROA"
#     roe = "ROE"
#     ros = "ROS"
#
#     @classmethod
#     def contains(cls, value):
#         return any(value == item.value for item in cls)
#
# class Bender:
#     def __init__(self, power=1., norm_max=100.):
#         self.norm_max = float(norm_max)
#         self.power = float(power)
#
#     def transform(self, value):
#         return (value / self.norm_max) ** self.power * self.norm_max
#
#     def restore(self, value):
#         return (value / self.norm_max) ** (1/self.power) * self.norm_max
#
# class Linear:
#     def __init__(self, shift, multiplier, revers = False):
#         self.shift = float(shift)
#         self.multiplier = multiplier
#         self.revers = revers
#
#     def transform(self, value):
#         return (self.shift + (-1 if self.revers else 1) * value) * self.multiplier
#
#     def restore(self, value):
#         return ((value / self.multiplier) - self.shift) * (-1 if self.revers else 1)
#
#
# def p_to_e_atomic_transformator(x):
#     if x < 0:
#         return 0
#     if x > 33:
#         return 0
#     l = (34 - x) * 3
#     return (l/100.)**4*100
#
# def e_to_p_atomic_transformator(x):
#     if x < 0:
#         return 0
#     return x
#
# def p_to_b_atomic_transformator(x):
#     if x < 0:
#         return 0
#     l = (5-x) * 20
#     l = max(l,0)
#     return (l / 100.)**3*100
#
# def p_to_s_atomic_transformator(x):
#     if x < 0:
#         return 0
#     if x > 5:
#         return 0
#     l = (5 - x) * 20
#     return (l/100.)**3*100
#
# def p_to_cf_atomic_transformator(x):
#     if x < 0:
#         return 0
#     if x > 30:
#         return 0
#     l = (30 - x) * 3.
#     return (l/100)**1.5*100
#
# def l_to_a_atomic_transformator(x):
#     if x < 0:
#         return 0
#     if x > 100:
#         return 0
#     l = (100 - x) * 1.
#     return (l/100)**1*100
#
# def net_debt_to_ebitda_atomic_transformator(x):
#     if x < 0:
#         return 0
#     if x > 5:
#         return 0
#     l = (5 - x) * 20.
#     return (l/100)**3*100
#
# def ev_to_ebitda_atomic_transformator(x):
#     if x < 0:
#         return 0
#     if x > 33:
#         return 0
#     l = (34 - x) * 3.
#     return (l/100.)**4*100
#
# def roa_atomic_transformator(x):
#     return x
#
# def roe_atomic_transformator(x):
#     return x
#
# def ros_atomis_transformator(x):
#     return x
#
# transformators = {
#     Multiplier.p_to_e: p_to_e_atomic_transformator,
#     Multiplier.e_to_p: e_to_p_atomic_transformator,
#     Multiplier.p_to_b: p_to_b_atomic_transformator,
#     Multiplier.p_to_s: p_to_s_atomic_transformator,
#     Multiplier.p_to_cf: p_to_cf_atomic_transformator,
#     Multiplier.l_to_a: l_to_a_atomic_transformator,
#     Multiplier.netDebt_to_ebitda: net_debt_to_ebitda_atomic_transformator,
#     Multiplier.ev_to_ebitda: ev_to_ebitda_atomic_transformator,
#     Multiplier.roa: roa_atomic_transformator,
#     Multiplier.roe: roe_atomic_transformator,
#     Multiplier.ros: ros_atomis_transformator
# }
#
# if __name__ == "__main__":
#     v = 10
#     tr = Bender(3, 100)
#     v_t = tr.transform(v)
#     v_r = tr.restore(v_t)
#     print(v, v_t, v_r)