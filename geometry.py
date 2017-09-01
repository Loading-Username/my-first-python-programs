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

def trapezoid_area(b, h):
    a = b * h / (1/2)
    return a

# function calls
print (trapezoid_area(4, 7))

def volume_rectangularprism(l, w, h):
    v = l * w * h
    return v

# function calls
print (volume_rectangularprism(5, 6, 7))
v = input()

def volume_cone(r, h):
    v = math.pi * r * r * h / 3
    return v

# function calls
print(volume_cone(4, 7))

def volume_sphere(r):
    v = 4 / 3 * math.pi * r * r * r
    return v

# function calls
print(volume_sphere(7))

def surfacearea_rectangularprism(l, w, h):
    a = 2 * w, l, h
    return a

# function calls
print(surfacearea_rectangularprism(3, 4, 5))


def surfacearea_sphere(r):
    a = 4 * math.pi * r * r
    return a

# function calls
print(surfacearea_sphere(7))


def hypotenuse_righttriangle(a, c):
    h = a * a * c * c // a + b
    return h

# function calls
print(hypotenuse_righttriangle(4, 7))










