import numpy as np


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
            self._degree = n - 1

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

    def __mul__(self, other):
        pass

    def __call__(self, x):
        pass

    @property
    def derivative(self):
        return 0

    @property
    def degree(self):
        return self._degree


if __name__ == "__main__":
    p = Polynomial([1, 2, 3])
    print(p)
