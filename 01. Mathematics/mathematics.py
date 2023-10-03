import math

# Basic Arithmetic Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

# Advanced Mathematical Functions
def square_root(x):
    if x < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Trigonometric Functions
def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

# Logarithmic Functions
def natural_log(x):
    if x <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers.")
    return math.log(x)

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Logarithm is only defined for positive numbers with a valid base.")
    return math.log(x, base)

# Constants
PI = math.pi
EULER_NUMBER = math.e
