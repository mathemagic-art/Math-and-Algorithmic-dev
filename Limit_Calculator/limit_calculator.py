from sympy import sympify, Symbol, limit
import sys 
sys.path.append('parse_and_output')
from parse_and_output import parseFunc, outputFunc

def limit_calculator(function: str, symbol : str, approach: str) -> str:
    
    symbol = Symbol(symbol)
    function = parseFunc(function)
    
    if approach[-1] in ['+', '-']:        
        sign = approach[-1]
        approach = int(approach[:-1])
        ans = str("{:.5f}".format(sympify(limit(function, symbol, approach)).evalf()))
    else:
        if approach.isdigit():
            approach = int(approach)
        ans = str("{:.5f}".format(sympify(limit(function, symbol, approach)).evalf()))
    
    
    return ans

# ./testcases.txt there are some inputs use them
# print(limit_calculator("1/x", 'x', '0+'))
print(limit_calculator("e^x", 'x', '34'))



    



