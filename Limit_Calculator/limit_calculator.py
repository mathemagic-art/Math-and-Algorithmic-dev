import sympy as sp


def limit_calculator(function: str, symbol : str, limit: str) -> str:
    
    symbol = sp.Symbol(symbol)
    function = sp.sympify(function.replace('e', 'E'))
    
    if limit[-1] in ['+', '-']:        
        sign = limit[-1]
        limit = int(limit[:-1])
        ans = str(sp.limit(function, symbol, limit, sign))
    else:
        if limit.isdigit():
            limit = int(limit)
        ans = str(sp.limit(function, symbol, limit))
    
    
    return ans

# ./testcases.txt there are some inputs use them
# print(limit_calculator("1/x", 'x', '0+'))
    



