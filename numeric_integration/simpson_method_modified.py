from sympy import lambdify, sympify
from sympy.abc import x
from scipy.integrate import quad
from numpy import linspace
from numpy.random import randint


def Simpsons_method(function:str, initial_point:int, end_point:int)->str:
    def find_polynomial(x1, x2, x3, y1, y2, y3):
        a = (x1*(y3-y2) + x2*(y1-y3) + x3*(y2-y1))/((x1-x2)*(x1-x3)*(x2-x3))
        b = ((y2-y1)/(x2-x1)) - a*(x1+x2)
        c = y1 - a*x1**2 - b*x1
        return lambdify(x, sympify('{}*x**2 + {}*x + {}'.format(a, b, c)))
    n = randint(5, 50)
    function = lambdify(x, function)
    if n % 2 != 0:
        n += 1
    x_values = linspace(initial_point, end_point, n+1)
    dx = (end_point-initial_point)/n
    Area = 0
    for i in range(0, len(x_values)-2, 2):
        x_1, x_2, x_3 = x_values[i], x_values[i+1], x_values[i+2] 
        pol_func = find_polynomial(x_1, x_2, x_3, function(x_1), function(x_2), function(x_3))
        Area += quad(pol_func ,x_1, x_3)[0]
        
    return str(Area)   

# def Simpsons_method_graph(function,initial_point,end_point):
#     array = np.linspace(initial_point, end_point, 50)
#     function = sym.lambdify(x, function)
#     plt.plot(array, function(array), color='black')
#     n = randint(5, 50)
#     if n % 2 != 0:
#         n += 1
#     x_values = np.linspace(initial_point, end_point, n+1)
#     Area = 0
#     def find_polynomial(x1, x2, x3, y1, y2, y3):
#       a = (x1*(y3-y2) + x2*(y1-y3) + x3*(y2-y1))/((x1-x2)*(x1-x3)*(x2-x3))
#       b = ((y2-y1)/(x2-x1)) - a*(x1+x2)
#       c = y1 - a*x1**2 - b*x1
#       return sym.lambdify(x, sym.sympify('{}*x**2 + {}*x + {}'.format(a, b, c)))

#     for i in range(0, len(x_values)-2, 2):
#       x_1, x_2, x_3 = x_values[i], x_values[i+1], x_values[i+2]
#       pol_func = find_polynomial(x_1, x_2, x_3, function(x_1), function(x_2), function(x_3))
#       Area += quad(pol_func ,x_1, x_3)[0]
#       array = np.linspace(x_values[i], x_values[i+2], 50)
#       plt.fill_between(array, pol_func(array)) 
#       plt.savefig('Simpson_Method_Graph.png')
    
     
# Simpsons_method_graph("e^x", 0, 2)