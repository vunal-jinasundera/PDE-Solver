import numpy as np
import scipy as sp
from sympy.abc import x, t
from sympy import symbols
from sympy import lambdify
from sympy import sympify


def compute_coefficients(n, L, f):
    """
    Compute the Fourier coefficients symbolically using sympy.
    """
    sin_term = sp.sin(n * np.pi * x / L)
    integral = sp.integrate(f(x) * sin_term, (x, 0, L))
    return (2 / L) * integral


def solve_pde(L, alpha, n_terms, time_steps, t_max, f):
    """
    Solve the parabolic PDE symbolically using separation of variables.
    """
    x_vals = np.linspace(0, L, 100)
    t_vals = np.linspace(0, t_max, time_steps)
    u = np.zeros((len(x_vals), len(t_vals)))


    for n in range(1, n_terms + 1):
        # Compute eigenvalue and Fourier coefficient
        lambda_n = (n * np.pi / L) ** 2
        C_n = compute_coefficients(n, L, f)

        # Construct the symbolic solution for each term
        X_n = sp.sin(n * np.pi * x / L)
        T_n = sp.exp(-alpha * lambda_n * t)
        u_n = C_n * X_n * T_n

        # Evaluate the solution numerically
        for i, x_val in enumerate(x_vals):
            for j, t_val in enumerate(t_vals):
                u[i, j] += float(u_n.subs({x: x_val, t: t_val}))

    return x_vals, t_vals, u
