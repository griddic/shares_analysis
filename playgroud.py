from enum import Enum

from metrics import incom_not_weighted
from transformator_old import Multiplier

if __name__ == "__main__":
    from sympy import symbols, solve, simplify, factor
    from sympy.parsing.sympy_parser import (
        parse_expr,
        standard_transformations,
        implicit_multiplication,
        implicit_multiplication_application)

    trf = (
            standard_transformations +
            (implicit_multiplication_application,))

    x, y, z, t = symbols('x y z t')

    # formula_str = "5*x + 10"
    formula_str = " ((((34-x)*3)/100)**4)*100"

    formula = parse_expr(formula_str, transformations=trf)
    print(formula)
    # 5*x + 10

    # подставим 4 вместо `x`:
    res = formula.subs(x, 4)
    print(res)
    # 30

    # решение уравнения: `5*x + 10 = 0`
    print(solve(formula))
    # [-2]

    # решение уравнения: `5*x + 10 = 30` или `5*x + 10 - 30 = 0`
    print(solve(formula_str + f" - {res}"))
    # [4]

    print(16**(1/4))


