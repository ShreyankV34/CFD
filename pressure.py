import numpy as np
from scipy.ndimage import gaussian_gradient_magnitude

def calculate_pressure_gradient(pressure_field, sigma=1.0):
    """
    Calculates the pressure gradient of a pressure field.
    
    Parameters:
    pressure_field (np.ndarray): A 2D or 3D array of pressure values.
    sigma (float): Standard deviation for Gaussian kernel.
    
    Returns:
    np.ndarray: A gradient magnitude array.
    """
    gradient_magnitude = gaussian_gradient_magnitude(pressure_field, sigma=sigma)
    return gradient_magnitude

def predict_flow_separation(pressure_gradient, threshold=0.5):
    """
    Predicts flow separation based on pressure gradients.
    
    Parameters:
    pressure_gradient (np.ndarray): A gradient magnitude array.
    threshold (float): A threshold for detecting flow separation.
    
    Returns:
    np.ndarray: A boolean array indicating flow separation regions.
    """
    separation_regions = pressure_gradient > threshold
    return separation_regions
