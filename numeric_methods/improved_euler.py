import pandas as pd
from numeric_methods.base_solution import BaseSolution

class ImprovedEuler(BaseSolution):
    @staticmethod
    def solve(x0, y0, xmax, n, func):
        h = (xmax - x0) / n
        data = {'xi': [x0] * n, 'yi': [y0] * n}
        df = pd.DataFrame(data)

        for i in range(1, n):
            df.loc[i, 'xi'] = df.loc[i-1, 'xi'] + h
            df.loc[i, 'yi'] = df.loc[i-1, 'yi'] + h * func(df.loc[i-1, 'xi'] + h/2, 
                    df.loc[i-1, 'yi'] +  h/2 * func(df.loc[i-1, 'xi'], df.loc[i-1, 'yi']))

        return (df['xi'].tolist(), df['yi'].tolist())

