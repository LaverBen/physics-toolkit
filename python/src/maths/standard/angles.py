import numpy as np

def degrees_to_radians(angle_degrees):
    return (angle_degrees / 360) * 2 * np.pi

def radians_to_degrees(angle_radians):
    return (angle_radians / (2 * np.pi)) * 360