import numpy as np


def first_derv(f, x, h=1e-5):
    """Applying First Derivative"""
    return (f(x + h) - f(x - h)) / (2 * h)


def sec_derv(f, x, h=1e-5):
    """Applying Second Derivative"""
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2


def optimize(start, f):
    """Implementation of Newton's Method Formula"""
    x = start
    for i in range(1000):
        f1 = first_derv(f, x)
        f2 = sec_derv(f, x)
        x_new = x - (f1 / f2)
        if abs(x_new - x) < 1e-6:
            break
        x = x_new
    return x


help(optimize)