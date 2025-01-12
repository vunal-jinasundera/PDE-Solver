import sympy as sp
from sympy import symbols
from sympy import lambdify
from sympy import sympify



def get_user_equation():
    """
    Prompt the user for the coefficients of the PDE.
    """
    print("Enter the coefficients for the PDE in the form:")
    print("∂u/∂t = a(x) * ∂²u/∂x² + b(x) * ∂u/∂x + c(x) * u(x, t)")

    a_input = input("a(x) = ")
    b_input = input("b(x) = ")
    c_input = input("c(x) = ")

    x = sp.symbols('x')
    a_expr = sp.sympify(a_input)
    b_expr = sp.sympify(b_input)
    c_expr = sp.sympify(c_input)

    # Convert to functions
    a_func = sp.lambdify(x, a_expr, 'numpy')
    b_func = sp.lambdify(x, b_expr, 'numpy')
    c_func = sp.lambdify(x, c_expr, 'numpy')

    return a_func, b_func, c_func


def get_initial_condition():
    """
    Prompt the user for the initial condition function f(x).
    """
    print("Enter the initial condition function f(x) (use 'x' as the variable, e.g., 'sin(pi*x)', 'x*(1-x)', etc.):")
    user_input = input("f(x) = ")
    x = sp.symbols('x')
    f_expr = sp.sympify(user_input)
    return sp.lambdify(x, f_expr, 'numpy')


def get_parameters():
    """
    Prompt the user for domain length, diffusion coefficient, and numerical parameters.
    """
    L = float(input("Enter the length of the domain (L): "))
    alpha = float(input("Enter the diffusion coefficient (alpha): "))
    n_terms = int(input("Enter the number of Fourier terms to use (n_terms): "))
    time_steps = int(input("Enter the number of time steps to calculate: "))
    t_max = float(input("Enter the maximum time (t_max): "))
    return L, alpha, n_terms, time_steps, t_max
