import pandas as pd
from numeric_methods.base_solution import BaseSolution

class RungeKutta(BaseSolution):
    @staticmethod
    def solve(x0, y0, xmax, n, func):
        h = (xmax - x0) / n
        data = {'xi': [x0] * n, 'yi': [y0] * n}
        df = pd.DataFrame(data)

        for i in range(1, n+1):
            df.loc[i, 'xi'] = df.loc[i-1, 'xi'] + h
            k1 = func(df.loc[i-1, 'xi'], df.loc[i-1, 'yi'])
            k2 = func(df.loc[i-1, 'xi'] + h/2, df.loc[i-1, 'yi'] + h*k1/2)
            k3 = func(df.loc[i-1, 'xi'] + h/2, df.loc[i-1, 'yi'] + h*k2/2)
            k4 = func(df.loc[i-1, 'xi'] + h, df.loc[i-1, 'yi'] + h*k3)
            df.loc[i, 'yi'] =  df.loc[i-1, 'yi'] + (k1 + 2*k2 + 2*k3 + k4)*h/6

        return (df['xi'].tolist(), df['yi'].tolist())

