from math import exp, sin, cos

class BaseSolution():
    @staticmethod
    def constant(x, y):
        #return exp(-4*x) * (0.25 + 1/(y - x - 2))
        return y*exp(x) - exp(2*x)
        # return y / (x**2 * exp(-3/x))
        # return (y - sin(x)) / cos(x)

    @staticmethod
    def solve(*args):
        return None
