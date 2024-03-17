# fractal based data splitting

import numpy as np

def split_data(data, fractal, axis=0):
    """
    Split data into two parts based on the fractal value
    """
    if axis == 0:
        return data[:int(fractal*data.shape[0]), :], data[int(fractal*data.shape[0]):, :]
    elif axis == 1:
        return data[:, :int(fractal*data.shape[1])], data[:, int(fractal*data.shape[1]):]
    else:
        raise ValueError("Axis must be 0 or 1")
    
def split_data_3(data, fractal, axis=0):
    """
    Split data into three parts based on the fractal value
    """
    if axis == 0:
        return data[:int(fractal[0]*data.shape[0]), :], data[int(fractal[0]*data.shape[0]):int(fractal[1]*data.shape[0]), :], data[int(fractal[1]*data.shape[0]):, :]
    elif axis == 1:
        return data[:, :int(fractal[0]*data.shape[1])], data[:, int(fractal[0]*data.shape[1]):int(fractal[1]*data.shape[1])], data[:, int(fractal[1]*data.shape[1]):]
    else:
        raise ValueError("Axis must be 0 or 1")

def split_data_4(data, fractal, axis=0):
    """
    Split data into four parts based on the fractal value
    """
    if axis == 0:
        return data[:int(fractal[0]*data.shape[0]), :], data[int(fractal[0]*data.shape[0]):int(fractal[1]*data.shape[0]), :], data[int(fractal[1]*data.shape[0]):int(fractal[2]*data.shape[0]), :], data[int(fractal[2]*data.shape[0]):, :]
    elif axis == 1:
        return data[:, :int(fractal[0]*data.shape[1])], data[:, int(fractal[0]*data.shape[1]):int(fractal[1]*data.shape[1])], data[:, int(fractal[1]*data.shape[1]):int(fractal[2]*data.shape[1])], data[:, int(fractal[2]*data.shape[1]):]
    else:
        raise ValueError("Axis must be 0 or 1")






