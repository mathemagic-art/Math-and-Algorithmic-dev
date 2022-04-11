import sympy as sp
import numpy as np
from random import randint as rd



#  class since we are going to generate problems for different topics
class TestGenerator:


    def __init__(self, topic: str):
        
        self.topic = topic # topic: (linear eq, defined integral and etc)
        self.x = sp.Symbol('x')
        self.equation = ""

    #  depending on the topic this func will run the function that we need
    def __generate(self):

        pass 
    # it is function for linear eq. just demo
    def linear_equation(self):

        operation = ['-', '+', '*', '/']

        length = rd(3,5)
        used_x = True
        for i in range(length):
            
            if i < (length - 1): 
                self.equation += str(rd(2,10)) + operation[rd(0,3)]

                if len(self.equation) >= 3 and used_x:
                    self.equation += 'x'
                    used_x = False

            else: self.equation += str(rd(2,10))
        
        return "function itself: ", self.equation, " simplified: ", sp.simplify(self.equation, doit = False)


t = TestGenerator('l').linear_equation() # just to run this code! it will be removed from final version of code.
print(t)






