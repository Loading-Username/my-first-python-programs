# This program contains functions that evaluate formulas used in geometry.
#
# Derek DiCintio
# August 30, 2017

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a
def circle_area(r):
    a = math.pi * r**2
    return a

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def parallelogram_area(b, h):
    a = b * h
    return a
# function calls
print(parallelogram_area(3, 7))

def trapezoid_area(
    a = a + b * h / (1/2)
    return a
