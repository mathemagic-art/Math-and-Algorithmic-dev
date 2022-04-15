from sympy import sympify, integrate, lambdify, E
from sympy.abc import x

def integration_calculator(function,variable,lower_bound='inf',upper_bound='inf'):
  # By default the limits are set to infinity and it will calculate the indefinite integral,
  # If the limits are given then it will return the definite integral
  """
    integrate(f, x) returns the indefinite integral 
    integrate(f, (x, a, b)) returns the definite integral 
  """
  if lower_bound == upper_bound and upper_bound=='inf': # Checking the conidtion for indefinte integral
    return integrate(function,variable) # given the indefinite integral
  else: # otherwise it is a definite integral
    return integrate(function, (variable, lower_bound, upper_bound)) # given the definite integral


def definite_integral_calculator(function, lower_bound, upper_bound):
  function = function.replace('e', 'E')
  function = function.replace('ln', 'log')
  a = lambdify(x, integrate(sympify(function))) #integrating and lammbdifying a given function
  return str(a(upper_bound)-a(lower_bound))

print(definite_integral_calculator('ln(x)', 3, 6))




