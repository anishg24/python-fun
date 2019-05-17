#!/usr/bin/env python3
from math import sqrt

def quadratic_formula(a,b,c):
    """
    Calculates the answer for any quadratic formula given

    >>> quadratic_formula(a,b,c)
        a = coefficient of x^2 (can't be 0)
        b = coefficient of x
        c = constant
    
    Outputs in quadratic_formula.x1 & quadratic_formula.x2
    """
    if a == 0:
        return print("Not a quadratic formula")
    else:
        discrim = (b**2 - 4*a*c)
        div = 2*a
        if discrim < 0:
            return print("This function has no real solutions")
        else:
            root = sqrt(discrim)
            quadratic_formula.x1 = (-b + root)/div
            quadratic_formula.x2 = (-b - root)/div
