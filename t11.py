import numpy as np
from wakes import detect_wake
from pressure import calculate_pressure_gradient, predict_flow_separation
from visualization import plot_results

# Generate sample data
velocity_field = np.random.random((50, 50, 2))
pressure_field = np.random.random((50, 50))

# Detect wakes
wake_regions = detect_wake(velocity_field)

# Calculate pressure gradient
pressure_gradient = calculate_pressure_gradient(pressure_field)

# Predict flow separation
separation_regions = predict_flow_separation(pressure_gradient)

# Plot results
plot_results(velocity_field, wake_regions, pressure_gradient, separation_regions)
