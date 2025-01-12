from solver import solve_pde
from inputs import get_user_equation, get_initial_condition, get_parameters
from utils import plot_solution


def main():
    print("Welcome to the Symbolic Parabolic PDE Solver using SymPy!")

    # Get user-defined coefficients for the PDE
    a_func, b_func, c_func = get_user_equation()

    # Get other parameters from the user
    L, alpha, n_terms, time_steps, t_max = get_parameters()

    # Get the initial condition
    initial_condition = get_initial_condition()

    # Solve the PDE
    x_vals, t_vals, u = solve_pde(L, alpha, n_terms, time_steps, t_max, initial_condition)

    # Plot the solution
    plot_solution(x_vals, t_vals, u)


if __name__ == "__main__":
    main()
