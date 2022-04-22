import random
import sympy as sp

# This code is (for now) based on derivatives equation generator and derivative calculator, 
# because generating integrals requires also checking whether this integral exists or not. 
# The code will be updated and improved over time until achieving no dependency on any other generators or calculators.

def genIndefiniteIntegrals(diff_lvl=3): # 2, 3 or 4 difficulty level is preferred
    
    # Using derivative eq generator to generate an equation
    def genDifferentiationProblem(diff_lvl):

        problem = ''
        types = {
            'Logarithmic': ['ln'],
            'Trigonometric': ['sin', 'cos', 'tan'],
            'Exponential': ['e']
        }
        power = random.randint(2, 5)

        if diff_lvl == 1:
            coeff1 = random.randint(2, 10)
            problem += "{}*x^{}".format(coeff1, power)

        elif diff_lvl == 2:
            coeff1 = random.randint(2, 10)
            coeff2 = random.randint(2, 10)
            coeff3 = random.randint(2, 10)
            power2 = random.randint(2, 4)
            power3 = random.randint(1, 3)

            problem += "{}*x^{}+{}*x^{}+{}*x^{}".format(coeff1, power, coeff2, power2, coeff3, power3)

        elif diff_lvl == 3:
            coeff1 = random.randint(1, 5)
            func_type = random.choices(list(types.keys()), weights=(1, 3, 1))[0]
            func = random.choice(types[func_type])
            if func == 'e':
                problem += "{}^{}*x+{}".format(func, coeff1, genDifferentiationProblem(1))
            else:
                problem += "{}*{}(x)+{}".format(coeff1, func, genDifferentiationProblem(1))

        elif diff_lvl == 4:
            func_type = random.choices(list(types.keys()), weights=(2, 4, 2))[0]
            func = random.choice(types[func_type])
            problem += "{}({})".format(func, genDifferentiationProblem(1))

        elif diff_lvl == 5:
            operator = random.choice(('/', '*'))
            problem = "({}){}({})".format(genDifferentiationProblem(1), operator, genDifferentiationProblem(2))
        
        else:
            operator = random.choice(('/', '*'))
            problem = "({}){}({})".format(genDifferentiationProblem(1), operator, genDifferentiationProblem(4))

        return sp.sympify(problem)
       
    
    # Using derivative calc to check existence of antiderivative
    def Differentiating_Calculator(f: str):
        x = sp.Symbol('x')
        f = f.replace('e', 'E')
        f = sp.sympify(f)
        f_prime = f.diff(x)  
        f = sp.lambdify(x, f)
        return f_prime
    
    
    inp = str(genDifferentiationProblem(diff_lvl))
    std = ['2*x**2', '1/(sqrt(1-x**2))','1/(sqrt(1+x**2))', '1/(sqrt(x**2 - 1))','1/(1+x**2)', '1/(1-x**2)']
    
    # If antiderivative exists return the equation (that can be integrated), if not or in case of error, return equation from db
    try:
        return Differentiating_Calculator(inp)
    except:
        pass
    try:
        return Differentiating_Calculator(inp)
    except:
        return sp.sympify(random.choice((std)))

# How to use:     
# genIndefiniteIntegrals(3) ---- generate Indefinite integral with difficulty level 3 (1-5)(easy - hard)
