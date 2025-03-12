# app.py
from flask import Flask, request, jsonify, render_template
import sympy as sp
from inputs import get_initial_condition, get_parameters
from solver import solve_pde_greens
from plot import plot_solution

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    try:
        # Extract parameters and initial condition from the user input
        alpha, B, C, time_steps, t_max, d_x = get_parameters(data)
        initial_condition_str = data.get('initial_condition', 'sin((pi/10)*x)')
        f_expr = get_initial_condition(initial_condition_str)

        # Solve the PDE using the solver module
        x_vals, t_vals, u, symbolic_solution = solve_pde_greens(alpha, B, C, time_steps, t_max, f_expr, d_x)
        latex_solution = sp.latex(symbolic_solution)

        # Generate the plot using the plot module
        plot_img = plot_solution(x_vals, t_vals, u)

        return jsonify({'latex_solution': latex_solution, 'plot_img': plot_img})
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
