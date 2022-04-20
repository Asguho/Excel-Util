import xlwings as xw
import re as reg
from sympy import *

x, y, z = symbols('x y z')

@xw.func
def hello(name):
    return f"Hello {name}!"

@xw.func
def mysolve(equation):

    equation=reg.sub(r"([xyz\d])([xyz])", r"\1*\2", equation)


    HowMuchBestSoltution = 999
    WhatIsBestSoltution = 0
    solutions = solve("Eq("+ equation.replace(",", ".").replace("=", ", ")+")")
    for solution in solutions:
        if HowMuchBestSoltution > len(str(solution.evalf())):
            HowMuchBestSoltution = len(str(solution.evalf()))
            WhatIsBestSoltution = solution.evalf()

    return WhatIsBestSoltution

mysolve("2z=4")