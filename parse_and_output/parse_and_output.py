import re
from sympy import sympify
from sympy.abc import x

def parseFunc(function):
    return sympify(function.replace('e', 'E'))

def outputFunc(function):
    function = str(function).replace('log', 'ln')
    return function

