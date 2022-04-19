from sympy import python, sympify, integrate, lambdify, E
from sympy.abc import x
import sys
sys.path.append('parse_and_output')
from parse_and_output import parseFunc, outputFunc

def indefinite_integration_calculator(function: str) -> str:
  return outputFunc(integrate(parseFunc(function)))


def definite_integration_calculator(function, lower_bound, upper_bound):
  function = parseFunc(function)
  a = lambdify(x, integrate(sympify(function))) #integrating and lammbdifying a given function
  return outputFunc("{:.5f}".format((upper_bound)-a(lower_bound)))

print(indefinite_integration_calculator('x**2'))
