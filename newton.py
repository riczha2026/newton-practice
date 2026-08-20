import numpy as np
from scipy.differentiate import jacobian
#numpy.linalg.solve(H,g)


def f(x):
    return np.array([
        x[0]**2 + x[1]**2 - 4,
        x[0] - x[1]
    ])
    

def optimize(start, f, tol = 1e-6):
    """Implementation of Newton's Method Formula"""
    x = np.asarray(x0,dtype=float)

    if x.ndim ==0:
        for _ in range(1000):
            fx = f(x)
            if abs(fx)<tol:
                return x.item()
            dfx = derivatie(f,x).df

            if dfx ==0:
                raise ValueError("Derivative is zero.")

            x = x - (fx/dfx)

        raise RuntimeError("Newton's method did not converge.")

    else:
        for _ in range(10000):
            fx=f(x)

            if np.linalg.norm(fx)<tol:
                return x
            J=jacobian(f,x).df

            try:
                 delta = np.linalg.solve(J,fx)
            except np.linalg.LinAlgError:
                raise ValueError("Jacobian is singular.")
            
            x=x-delta
        raise RuntimeError("Newton's method did not converge.")
    
