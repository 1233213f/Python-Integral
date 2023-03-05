from scipy import integrate
import numpy as np
def f(x):
    return (((-0.10444 + 2.2) * 48.5224 / ((2 - 0.10444) * 100)) ** (-0.10444 + 2.2)) * np.exp((-2.2 + 0.10444) * (x / 100))**(-2.2)
v,err = integrate.quad(f,3.33,3333.333)
print(v,err)