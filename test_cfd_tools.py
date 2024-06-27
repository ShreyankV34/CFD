import numpy as np
from cfd_tools import detect_wake, calculate_pressure_gradient, predict_flow_separation

def test_detect_wake():
    velocity_field = np.random.random((10, 10, 2))
    wake_regions = detect_wake(velocity_field)
    assert wake_regions.shape == (10, 10)

def test_calculate_pressure_gradient():
    pressure_field = np.random.random((10, 10))
    gradient = calculate_pressure_gradient(pressure_field)
    assert gradient.shape == (10, 10)

def test_predict_flow_separation():
    pressure_gradient = np.random.random((10, 10))
    separation_regions = predict_flow_separation(pressure_gradient)
    assert separation_regions.shape == (10, 10)

if __name__ == "__main__":
    test_detect_wake()
    test_calculate_pressure_gradient()
    test_predict_flow_separation()
    print("All tests passed.")
