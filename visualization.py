import matplotlib.pyplot as plt
import numpy as np

def plot_results(velocity_field, wake_regions, pressure_gradient, separation_regions):
    """
    Plots the results of wake detection and flow separation.
    
    Parameters:
    velocity_field (np.ndarray): The velocity field array.
    wake_regions (np.ndarray): Boolean array indicating wake regions.
    pressure_gradient (np.ndarray): The pressure gradient array.
    separation_regions (np.ndarray): Boolean array indicating flow separation regions.
    """
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))

    ax[0].imshow(np.linalg.norm(velocity_field, axis=2), cmap='jet')
    ax[0].contour(wake_regions, colors='red')
    ax[0].set_title('Wake Detection')

    ax[1].imshow(pressure_gradient, cmap='jet')
    ax[1].set_title('Pressure Gradient')

    ax[2].imshow(separation_regions, cmap='jet')
    ax[2].set_title('Flow Separation')

    plt.show()
