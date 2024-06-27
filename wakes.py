import numpy as np

def detect_wake(velocity_field, threshold=0.1):
    """
    Detects wake regions in a velocity field.
    
    Parameters:
    velocity_field (np.ndarray): A 3D array of velocity vectors.
    threshold (float): A threshold for detecting low-velocity regions.
    
    Returns:
    np.ndarray: A boolean array indicating wake regions.
    """
    speed = np.linalg.norm(velocity_field, axis=2)
    wake_regions = speed < threshold
    return wake_regions
