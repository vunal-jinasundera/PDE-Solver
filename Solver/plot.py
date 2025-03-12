# plot.py
import io
import base64
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

def plot_solution(x_vals, t_vals, u):
    """
    Creates a 3D surface plot of u(x,t) and returns a base64-encoded PNG.
    """
    X, T = np.meshgrid(x_vals, t_vals)
    U = u.T  # Transpose so that time is on the correct axis
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, T, U, cmap='viridis', edgecolor='none')
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('u(x, t)')
    ax.set_title('3D Solution of the Parabolic PDE')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close(fig)
    return img_data