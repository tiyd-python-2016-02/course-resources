import numpy as np
from numpy.testing import *
from funcs import *


def test_get_positive_values():
    actual = get_positive_values(
        np.array([0, -7, 1, 0, -5, 3, 0, -1, 3, -2, 0, -5, 7, -3]))
    expected = np.array([1, 3, 3, 7])
    assert_array_equal(actual, expected)


def test_get_non_zero_values():
    actual = get_non_zero_values(
        np.array([0, -7, 1, 0, -5, 3, 0, -1, 3, -2, 0, -5, 7, -3]))
    expected = np.array([-7, 1, -5, 3, -1, 3, -2, -5, 7, -3])
    assert_array_equal(actual, expected)


def test_create_zeros_vector():
    actual = create_zeros(5)
    expected = np.array([0, 0, 0, 0, 0])
    assert_array_equal(actual, expected)


def test_create_zeros_matrix():
    actual = create_zeros((2, 2))
    expected = np.array([[0, 0], [0, 0]])
    assert_array_equal(actual, expected)


def test_create_ones_vector():
    actual = create_ones(5)
    expected = np.array([1, 1, 1, 1, 1])
    assert_array_equal(actual, expected)


def test_create_ones_matrix():
    actual = create_ones((2, 2))
    expected = np.array([[1, 1], [1, 1]])
    assert_array_equal(actual, expected)


def test_create_range():
    actual = create_range(10)
    expected = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert_array_equal(actual, expected)


def test_create_reversed_range():
    actual = create_reversed_range(5)
    expected = np.array([4, 3, 2, 1, 0])
    assert_array_equal(actual, expected)


def test_convert_to_3x3_matrix():
    actual = convert_to_3x3_matrix(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    expected = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert_array_equal(actual, expected)


def test_create_4x4_identity_matrix():
    actual = create_identity_matrix(2)
    expected = np.array([[1, 0], [0, 1]])
    assert_array_equal(actual, expected)


def test_create_3x3_identity_matrix():
    actual = create_identity_matrix(3)
    expected = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert_array_equal(actual, expected)


def test_create_evenly_spaced_numbers():
    actual = create_evenly_spaced_numbers(0, 100, 5)
    expected = np.array([0, 25, 50, 75, 100])
    assert_array_equal(actual, expected)


def test_mean():
    actual = mean(np.array([1, 2, 3]))
    expected = 2.0
    assert actual == expected


def test_median():
    actual = median(np.array([1, 5, 10]))
    expected = 5.0
    assert actual == expected


def test_stdev():
    actual = stdev(np.array([1, 2]))
    expected = 0.5
    assert actual == expected


def test_minimum():
    actual = minimum(np.array([4, 3, 1, 5, 2]))
    expected = 1
    assert actual == expected


def test_maximum():
    actual = maximum(np.array([4, 3, 1, 5, 2]))
    expected = 5
    assert actual == expected


def test_absolute_values():
    actual = absolute_values(np.array([-1, 2, -3, 4, -5]))
    expected = np.array([1, 2, 3, 4, 5])
    assert_array_equal(actual, expected)


def test_shape_2():
    actual = shape(np.array([0, 0]))
    expected = (2,)
    assert actual == expected


def test_shape_2x3():
    actual = shape(np.array([[0, 0, 0], [0, 0, 0]]))
    expected = (2, 3)
    assert actual == expected


def test_shape_3x2():
    actual = shape(np.array([[0, 0], [0, 0], [0, 0]]))
    expected = (3, 2)
    assert actual == expected


def test_dimensions_1():
    actual = dimensions(np.array([0]))
    expected = 1
    assert actual == expected


def test_dimensions_2():
    actual = dimensions(np.array([[0], [0]]))
    expected = 2
    assert actual == expected


def test_dot_product():
    actual = dot_product(np.array([1, 2, 3]), np.array([4, 5, 6]))
    expected = 32
    assert actual == expected


def test_reshape_3x3():
    actual = reshape(np.arange(9), (3, 3))
    expected = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    assert_array_equal(actual, expected)


def test_create_zeros_around_one():
    actual = create_zeros_around_one()
    expected = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    assert_array_equal(actual, expected)


def test_create_ones_around_zero():
    actual = create_ones_around_zero()
    expected = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    assert_array_equal(actual, expected)
