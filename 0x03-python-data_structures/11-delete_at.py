#!/usr/bin/python3
<<<<<<< HEAD
# 11-delete_at.py
# Brennan D Baraban <375@holbertonschool.com>

=======
>>>>>>> 135b120004f2d3c2dad96982f601b2973ae6e36f

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
