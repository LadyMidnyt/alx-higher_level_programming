#!/usr/bin/python3
<<<<<<< HEAD
# 8-multiple_returns.py
# Brennan D Baraban <375@holbertonschool.com>

=======
>>>>>>> 135b120004f2d3c2dad96982f601b2973ae6e36f

def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
