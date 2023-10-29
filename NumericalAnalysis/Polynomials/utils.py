from basis import Polynomial


def evaluate(p: Polynomial, x):
    coe = p.coe
    n = p.degree
    if n <= 0:
        return coe[0]
    value = coe[0] * x + coe[1]
    for k in range(2, n+1):
        value = value * x + coe[k]
    return value


def q_evaluate(p: Polynomial, x):
    roots = p.roots
    coe = p.coe
    if x in roots:
        return 0
    value = 1
    for root in roots:
        value *= x - root
    return value

