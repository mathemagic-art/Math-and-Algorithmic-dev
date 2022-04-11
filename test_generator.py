import random, time
from sympy import sympify

operators = ['+', '-', '*', '/']
addsub = ['+', '-']
muldiv = ['*', '/']


def Diffs():
    x = 'x'
    coefficient1 = random.randint(-10, 30)
    coefficient2 = random.randint(-10, 30)
    coefficient3 = random.randint(-10, 40)
    coefficient4 = random.randint(-10, 40)
    coefficient5 = random.randint(-10, 40)
    power = random.randint(-5, 5)

    monomial = "{}*{}^{}".format(coefficient1, x, power)
    monomial2 = "({}*({}^{})){}{}".format(coefficient1, x, power,random.choice(muldiv), coefficient2)

    binomial = "{}*({}^{}){}({})".format(coefficient1, x, power, random.choice(addsub), coefficient2)
    binomial2 = "({}*({}^{}){}({})){}({})".format(coefficient1, x, power, random.choice(addsub), coefficient2, random.choice(muldiv), coefficient2)


    trinomial = "{}*{}^{}{}{}*{}^{}{}{}".format(coefficient1, x, power, random.choice(addsub), coefficient2, x, power,
                                              random.choice(addsub), coefficient3)
    trinomial2 = "({}*{}^{}{}{}*{}^{}{}{}){}{}*{}^{}{}{}".format(coefficient1, x, power, random.choice(addsub), coefficient2, x, power,
                                              random.choice(addsub), coefficient3, random.choice(muldiv), coefficient4, x, power, random.choice(operators), coefficient5)

    layout1 = "{}*{}^{}{}{}".format(coefficient1, x, power, random.choice(operators), coefficient2)
    layout2 = "{}*{}^{}{}{}".format(coefficient1, x, power, random.choice(operators), coefficient2)

    layouts = [monomial, monomial2]

    result = random.choice(layouts)

    return result

test = Diffs()

print(test)
print(sympify(test))
