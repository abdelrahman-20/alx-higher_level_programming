#!/usr/bin/python3
"""Module For A Method."""


def is_same_class(obj, a_class):
    """A Function To Check For Instances.
    
    Args:
        obj: The Object.
        a_class: The Class Name.
    
    Returns:
        True or False
    """
    
    if type(obj) == a_class:
        return True
    return False
