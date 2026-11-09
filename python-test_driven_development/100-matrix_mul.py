#!/usr/bin/python3
"""Defines matrix_mul, which multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """Return the matrix product of m_a and m_b.

    Both matrices are validated in this order: list, list of lists,
    not empty, numbers only, rectangular, then compatible sizes.
    """
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if not isinstance(m, list):
            raise TypeError("{} must be a list".format(name))
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if not all(isinstance(row, list) for row in m):
            raise TypeError("{} must be a list of lists".format(name))
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if m == [] or m == [[]]:
            raise ValueError("{} can't be empty".format(name))
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if not all(isinstance(n, (int, float)) for row in m for n in row):
            raise TypeError(
                "{} should contain only integers or floats".format(name))
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if any(len(row) != len(m[0]) for row in m):
            raise TypeError(
                "each row of {} must be of the same size".format(name))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*m_b)]
            for row in m_a]
