import numpy as np


def first_derv(func, x, h=1e-5):
    """Applying First Derivative"""
    return (func(x + h) - func(x - h)) / (2 * h)


def sec_derv(func, x, h=1e-5):
    """ Applying Second Derivative"""
    return (func(x + h) - 2 * func(x) + func(x - h)) / h**2


def new_optimize(start, func, tol = 1e-6):
    """Implementation of Newton's Method Formula"""
    if not callable(func):
        raise TypeError(f"Argument is not a function, it is of type {type(func)}")
    x_new = start - (first_derv(func,start)/sec_derv(func,start))
    x= start 

    while abs(x_new-x)< tol:
        x=x_new
        x_new = start - (first_derv(func,start)/sec_derv(func,start))
    return {"x: ": x_new}
    
