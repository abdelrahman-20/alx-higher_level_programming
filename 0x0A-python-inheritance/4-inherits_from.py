#!/usr/bin/python3
"""Module For A Method."""


def inherits_from(obj, a_class):
    """ A Function To Check if Object is Instance.

    Args:
        obj: The Object.
        a_class: The Class.

    Returns:
        True of False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
