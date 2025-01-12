import matplotlib.pyplot as plt

def plot_solution(x_vals, t_vals, u):
    """
    Plot the solution u(x, t) at various time steps.
    """
    for j in range(0, len(t_vals), len(t_vals) // 10):
        plt.plot(x_vals, u[:, j], label=f't={t_vals[j]:.2f}')
    plt.xlabel('x')
    plt.ylabel('u(x, t)')
    plt.title('Solution of the Parabolic PDE')
    plt.legend()
    plt.show()
