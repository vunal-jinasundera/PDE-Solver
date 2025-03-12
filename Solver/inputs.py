# inputs.py
import sympy as sp


def get_initial_condition(user_input=None):
    """
    Convert the user input into a symbolic expression.
    Raises a ValueError if the input cannot be parsed properly.
    """
    x = sp.symbols('x')
    if user_input is None:
        user_input = "sin((pi/10)*x)"
    try:
        f_expr = sp.sympify(user_input)
    except Exception as e:
        raise ValueError("Invalid initial condition input: " + str(e))

    # Check that the expression actually depends on x (or is a valid constant)
    if not hasattr(f_expr, 'free_symbols'):
        raise ValueError("The initial condition must be a valid symbolic expression in x.")

    return f_expr

def get_parameters(data):
    """
    Extracts and converts PDE parameters from the provided data dictionary.
    """
    alpha = float(data.get('alpha', 0.0025))
    B = float(data.get('B', 0))
    C = float(data.get('C', 0))
    time_steps = 25000
    t_max = 1300
    d_x = 1000
    return alpha, B, C, time_steps, t_max, d_x
