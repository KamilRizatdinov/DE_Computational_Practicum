import pandas as pd
from numeric_methods.base_solution import BaseSolution

class Exact(BaseSolution):
    @staticmethod
    def solve(x0, y0, xmax, n, solution):
        h = (xmax - x0) / n
        data = {'xi': [x0] * n, 'yi': [y0] * n}
        df = pd.DataFrame(data)

        for i in range(1, n):
            df.loc[i, 'xi'] = df.loc[i-1, 'xi'] + h
            df.loc[i, 'yi'] = solution(df.loc[i, 'xi'], x0, y0)

        return (df['xi'].tolist(), df['yi'].tolist())

