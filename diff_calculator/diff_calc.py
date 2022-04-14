#Done by Aiha

from sympy import *


# We have to create a "symbol" called x, as you will have any (a,h or y variables) you should write 'var = Symbol ('var')' and ect
def Differentiating_Calculator(f: str):
    x = Symbol('x') #these are variables
    f = f.replace('e', 'E')
    f = sympify(f) #this is input (be careful with writing the power of exp, because here we dont use usal (**) but just take in breakets 
    f_prime = f.diff(x)  
    f = lambdify(x, f) #idetifiying respect to which variable we are taking variable
    #print in the space (f_prime) it will give the answer
    return f_prime
