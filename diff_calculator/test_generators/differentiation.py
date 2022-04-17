import random
from sympy import sympify


def genDifferentiationProblem(diff_lvl=2):

    # dependencies
    problem = ''
    types = {
        'Logarithmic': ['ln'],
        'Trigonometric': ['sin', 'cos', 'tan', 'cot', 'sec'],
        'Exponential': ['e']
    }
    power = random.randint(2, 5)

    if diff_lvl == 1:
        coeff1 = random.randint(2, 10)
        problem += "{}*x^{}".format(coeff1, power)

    if diff_lvl == 2:
        coeff1 = random.randint(2, 10)
        coeff2 = random.randint(2, 10)
        coeff3 = random.randint(2, 10)
        power2 = random.randint(2, 4)
        power3 = random.randint(1, 3)

        problem += "{}*x^{}+{}*x^{}+{}*x^{}".format(coeff1, power, coeff2, power2, coeff3, power3)

    if diff_lvl == 3:
        coeff1 = random.randint(1, 5)
        func_type = random.choices(list(types.keys()), weights=(1, 3, 1))[0]
        func = random.choice(types[func_type])
        if func == 'e':
            problem += "{}^{}*x+{}".format(func, coeff1, genDifferentiationProblem(1))
        else:
            problem += "{}*{}(x)+{}".format(coeff1, func, genDifferentiationProblem(1))

    if diff_lvl == 4:
        func_type = random.choices(list(types.keys()), weights=(2, 4, 2))[0]
        func = random.choice(types[func_type])
        problem += "{}({})".format(func, genDifferentiationProblem(1))

    if diff_lvl == 5:
        operator = random.choice(('/', '*'))
        problem = "({}){}({})".format(genDifferentiationProblem(2), operator, genDifferentiationProblem(3))

    return sympify(problem)

print(genDifferentiationProblem(2))
