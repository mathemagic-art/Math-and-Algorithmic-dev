import random
from sympy import sympify


def generateDifferentiation(level=2):

    # dependencies
    problem = ''
    types = {
        'Trigonometric': ['sin', 'cos', 'tan', 'cot', 'sec'],
        'Exponential': ['e'],
        'Logarithmic': ['ln']
    }
    operators = ["+", "-", "*", "/"]
    random_operator = random.choice(operators)

    # layouts
    def polynomial():
        coeff = random.randint(1, 5)
        power = random.randint(2, 5)
        problem = "{}*x**{}".format(coeff, power)
        return problem

    def trigonometric():
        coeff_1 = random.randint(1, 5)
        coeff_2 = random.randint(1, 5)
        func_type = list(types.keys())[0]
        func = random.choice(types[func_type])
        problem = "({}*{}*({}*x))".format(coeff_1, func, coeff_2)
        return problem

    # logic
    if level == 1:
        problem += "({}){}({})".format(polynomial(),
                                       random_operator, polynomial())

    if level == 2:
        problem += "({}){}({})".format(trigonometric(),
                                       random_operator, trigonometric())

    if level == 3:
        coeff_1 = random.randint(1, 5)
        coeff_2 = random.randint(1, 5)
        coeff_3 = random.randint(1, 5)
        power_1 = random.randint(1, 5)
        func_type = random.choice(list(types.keys())[1:])
        func = types[func_type][0]

        if func == 'e':
            problem += "{}*{}**({}*x**{}{}{})".format(
                polynomial(), func, coeff_2, power_1, random_operator, coeff_3)
        else:
            problem += "{}*{}*({}){}{}".format(
                coeff_1, func, polynomial(), random_operator, trigonometric())

    return problem


print(generateDifferentiation(3))
