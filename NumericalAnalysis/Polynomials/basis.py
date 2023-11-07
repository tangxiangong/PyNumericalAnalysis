import numpy as np
import fractions
from typing import Union


class Polynomial(object):
    """多项式类"""

    def __init__(self, coe, roots=None):
        """
        初始化
        :param coe: 多项式系数, 按照幂次降序排列
        :param roots:  多项式的根, 默认为 `None`
        """
        coe = np.asarray(coe)
        assert coe.ndim == 1 and coe.size >= 1
        n = coe.size - 1
        if roots is not None:
            roots = np.asarray(roots)
            assert roots.ndim == 1 and roots.size == n
        self._coe = coe
        self._roots = roots
        if n >= 1:
            assert coe[0] != 0
        if n == 0 and coe[0] == 0:
            self._degree = -1
        else:
            self._degree = n

    def __repr__(self):
        n = self._degree
        var = "x"
        coe = self._coe
        if n <= 0:
            return f"{coe[0]}"
        if n == 1:
            s = f"{coe[0]}{var}" if abs(coe[0]) != 1 else (f"{var}" if coe[0] == 1 else f"-{var}")
        else:
            s = f"{coe[0]}{var}^{n}" if abs(coe[0]) != 1 else (f"{var}^{n}" if coe[0] == 1 else f"-{var}^{n}")
        for k in range(1, n - 1):
            if coe[k] == 0:
                continue
            if coe[k] > 0:
                s += "+"
            s += f"{var}^{n - k}" if abs(coe[k]) == 1 else f"{coe[k]}{var}^{n - k}"
        if n > 1 and coe[n - 1] != 0:
            s += f"+{coe[n - 1]}{var}" if coe[n - 1] > 0 else f"{coe[n - 1]}{var}"
        if coe[-1] != 0:
            s += f"+{coe[-1]}" if coe[-1] > 0 else f"{coe[-1]}"
        return s

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rmul__(self, other):
        if isinstance(other, Union[int, float, fractions.Fraction]):
            return Polynomial(other*self._coe, self._roots)
        else:
            return self.__mul__(other)

    def __mul__(self, other):
        pass

    def __call__(self, x):
        if self._roots is None:
            return evaluate(self, x)
        else:
            return q_evaluate(self, x)

    @property
    def coe(self):
        return self._coe

    @property
    def roots(self):
        return self._roots

    @property
    def derivative(self):
        return 0

    @property
    def degree(self):
        return self._degree

    def is_zero(self):
        return self._coe[0] == 0

    @classmethod
    def zero(cls):
        return Polynomial([0])


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
    value = coe[0]
    for root in roots:
        value *= (x - root)
    return value


if __name__ == "__main__":
    poly = Polynomial([1, 0, 3])
    print(fractions.Fraction(1, 2)*poly)
