from sympy import lambdify
from sympy.abc import x

def rectangle_Method(function:str, initial_point:int, end_point:int, num_of_interval:int)->str:
  function = lambdify(x, function)
  dx = (end_point - initial_point)/num_of_interval
  total = 0.0
  for i in range (num_of_interval):
          total = total + function((initial_point + (i*dx)))
  Area = dx*total
  return str(Area) 


# def rectangle_method_graph(function, initial_point, end_point, num_of_interval):
#     X = np.linspace(initial_point,end_point,100)
#     x = np.linspace(initial_point,end_point,num_of_interval+1)
#     z = sym.symbols('x')
#     function = sym.lambdify(z, function)
#     Y = function(X)
#     plt.figure(figsize = (15,10))
#     plt.plot(X,Y, color='black', linewidth=2, markersize=50)

#     for i in range(num_of_interval):
#         init_point = [x[i],x[i],x[i+1],x[i+1]]
#         end_point = [0,function(x[i]),function(x[i]),0]
#         plt.fill_between(init_point,end_point, edgecolor='black')
#         plt.savefig('Rectangle_Method_Graph.png')

# rectangle_method_graph("e^x", 0, 2, 8)