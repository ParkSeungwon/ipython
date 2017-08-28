from sympy import *
init_printing()
x = Symbol('x')
y = Symbol('y')
exp = x**-1*y/(x*y**2)
print exp
print latex(exp)

