import numpy as np


def get_positive_values(values):
    return values[values > 0]


def get_non_zero_values(values):
    return values[np.nonzero(values)]


def create_zeros(shape):
    return np.zeros(shape)


def create_ones(shape):
    return np.ones(shape)


def create_identity_matrix(shape):
    return np.eye(shape)


def create_range(count):
    return np.arange(count)


def create_reversed_range(count):
    return np.arange(count)[::-1]


def convert_to_3x3_matrix(values):
    return values.reshape(3, 3)


def create_evenly_spaced_numbers(start, stop, num):
    return np.linspace(start, stop, num)


def mean(values):
    return np.mean(values)


def stdev(values):
    return np.std(values)


def median(values):
    return np.median(values)


def minimum(values):
    return values.min()


def maximum(values):
    return values.max()


def absolute_values(values):
    return np.abs(values)


def dimensions(values):
    return values.ndim


def shape(values):
    return values.shape


def dot_product(a, b):
    return np.dot(a, b)


def reshape(values, shape):
    return values.reshape(shape)


def create_zeros_around_one():
    matrix = np.zeros((3, 3))
    matrix[1, 1] = 1
    return matrix


def create_ones_around_zero():
    matrix = np.ones((3, 3))
    matrix[1, 1] = 0
    return matrix
