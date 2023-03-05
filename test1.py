import math

from scipy import integrate
import numpy as np
def f(x):
    return 1/((67.74/3.08568)*10**(-19)*math.sqrt((1+x)**3*0.3089+0.6911))
a=integrate.quad(f,0,0.09)
print(a[0]*3*10**10*(1+0.09))