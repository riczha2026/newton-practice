import sympy as sp
import numpy as np

h=sp.symbols('h')


    
def first_derv(f,x):
    return sp.limit((f(x+h)-f(x))/h,h,0)
def sec_derv(f,x):
    return sp.limit((f(x+h)-2*f(x)+f(x-h))/h**2,h,0)
def optimize(start,f):
    x = start
    for i in range(1000):
        f1=first_derv(f,x)
        f2=sec_derv(f,x)
        x_new = x-(f1/f2)
        if abs(x_new-x)<1e-6:
            break
        x=x_new
    return x

    
def main():
    optimize(2.5, np.cos)
if __name__ == '__main__':
    main()




