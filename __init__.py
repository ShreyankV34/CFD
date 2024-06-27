from .wakes import detect_wake
from .pressure import calculate_pressure_gradient, predict_flow_separation
from .visualization import plot_results

__all__ = ['detect_wake', 'calculate_pressure_gradient', 'predict_flow_separation', 'plot_results']
