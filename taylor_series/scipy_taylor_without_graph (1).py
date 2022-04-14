from sympy import lambdify, sympify, diff, E
from math import factorial
from sympy.abc import x
import numpy as np


def taylor(function, num_of_iter, center):
  function = function.replace('e', 'E')
  taylorPolynomial = str(lambdify(x, sympify(function))(center))
  for i in range(1, num_of_iter):
      f_diff = str(lambdify(x, diff(function, x, i))(center))
      taylorPolynomial += '+' + f_diff +'/'+str(factorial(i))+'*(x-{})**{}'.format(center, i)
  taylorPolynomial = sympify(taylorPolynomial, rational=True)
  return str(taylorPolynomial)

print(taylor('e**x', 5, 0))