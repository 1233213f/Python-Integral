from sympy import *
x = symbols("x")
b = symbols("b")
a = symbols("a")
print(integrate(exp(x), (x, a, b)))
#  integer的参数(函数，（变量，起始位置，终止位置))