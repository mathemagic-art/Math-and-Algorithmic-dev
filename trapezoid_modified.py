from sympy import lambdify
from sympy.abc import x

def Trapezoid(function:str,initial_point:int,end_point:int,number_interval:int) ->str:
  function = lambdify(x, function)
  dx = (end_point - initial_point)/number_interval
  A = 1/2 *(function(initial_point) + function(end_point))
  for i in range(1, number_interval):
      A = A + function(initial_point + i*dx)
  Area = dx * A
  return str(Area)




# def Trapezoid_graph(function,initial_point,end_point,number_interval):
#     X = np.linspace(initial_point,end_point,100)
#     x = np.linspace(initial_point,end_point,number_interval+1)
#     z = sym.symbols('x')
#     function = sym.lambdify(z, function)
#     Y = function(X)
#     plt.figure(figsize = (15,10))
#     plt.plot(X,Y, color='black', linewidth=2, markersize=50)

#     for i in range(number_interval):
#         initial_point = [x[i],x[i],x[i+1],x[i+1]]
#         end_point = [0,function(x[i]),function(x[i+1]),0]
#         plt.fill(initial_point,end_point,'lightblue', edgecolor='black',alpha=1)

#     plt.title('Area under the curve, Trapezoid method')
#     plt.savefig('image.png')
