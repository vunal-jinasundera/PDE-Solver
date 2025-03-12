# solver.py
import sympy as sp
import numpy as np
from scipy.signal import fftconvolve


def greens_function(x, xi, t, tau, A, B, C):
    """
    Returns the Green's function for the parabolic PDE.
    """
    if t == tau:
        return sp.DiracDelta(x - xi)
    else:
        return (1 / sp.sqrt(4 * sp.pi * A * (t - tau))) * sp.exp(-((x - xi - B * (t - tau)) ** 2) / (4 * A * (t - tau)))


def solve_pde_greens(alpha, B, C, time_steps, t_max, f_expr, d_x):
    """
    Solves the parabolic PDE using a Green's function approach.
    Returns the spatial grid, time grid, numerical solution, and symbolic solution.
    """
    # Define symbolic variables
    x, xi, t, tau = sp.symbols('x xi t tau')
    # Compute the symbolic Green's function
    G_xt = greens_function(x, xi, t, tau, alpha, B, C)
    # Compute the convolution integral symbolically
    u_xt = sp.integrate(G_xt * f_expr.subs(x, xi), (xi, -sp.oo, sp.oo))
    symbolic_solution = sp.simplify(u_xt)

    # Numerical evaluation
    f_func = sp.lambdify(x, f_expr, 'numpy')
    L = 10  # Use a large domain to approximate infinity
    x_vals = np.linspace(-L, L, d_x)
    t_vals = np.linspace(0, t_max, time_steps)
    f_samples = f_func(x_vals)
    u = np.zeros((len(x_vals), len(t_vals)))

    for j, t_val in enumerate(t_vals):
        if t_val == 0:
            u[:, j] = f_samples
        else:
            G_t = sp.lambdify(x, greens_function(x, 0, t_val, 0, alpha, B, C).evalf(), 'numpy')
            G_samples = G_t(x_vals)
            u[:, j] = fftconvolve(f_samples, G_samples, mode='same') * (x_vals[1] - x_vals[0])

    return x_vals, t_vals, u, symbolic_solution
