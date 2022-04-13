# -*- coding: utf-8 -*-
"""Scipy_Taylor_with_graph.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1glxpr8moNZ2JXJAE1YDBpQ2rdNwCtVfI
"""

import sympy as sym
from math import *
from sympy.abc import x
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
from sympy.plotting import plot
function = input("Please enter the function: ")
function = function.replace('e', 'E')
n = int(input("Please enter the number of terms for expansion: "))
c = float(input("Please enter the centre: "))
def taylor(function,n,c):
  taylorPolynomial = str(sym.lambdify(x, function)(c))
  for i in range(1, n):
      diff = str(sym.lambdify(x, sym.diff(function, x, i))(c))
      taylorPolynomial += '+' + diff +'/'+str(factorial(i))+'*(x-{})**{}'.format(c, i)
  taylorPolynomial = sym.sympify(taylorPolynomial, rational=True)
  return taylorPolynomial
taylor(function,n, c)

arr = np.linspace(c-c, c+c, 100)
y=sym.lambdify(x, function)(arr)
y_2=sym.lambdify(x, taylorPolynomial)(arr)
plt.plot(arr,y , label='Function', color = "blue")
plt.plot(arr, y_2, label='Taylor series', color = "red")
plt.legend()