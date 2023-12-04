#!/usr/bin/python3
"""Module For A Method."""


def is_kind_of_class(obj, a_class):
    """A Function To Determine if The Object is an Instance.

    Args:
        obj: The Object.
        a_class: The Class To Check.

    Returns:
        True of False
    """
    if isinstance(obj, a_class):
        return True
    return False
