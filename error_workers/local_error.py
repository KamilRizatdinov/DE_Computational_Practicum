import pandas as pd
from error_workers.base_error import BaseError

class LocalError(BaseError):
    @staticmethod
    def calculate(exact_points, method_points):
        exact_x, exact_y = exact_points
        method_x, method_y = method_points

        df = pd.DataFrame({'x': exact_x, 'exact_y': exact_y, 'method_y': method_y})

        for i in range(len(df.index)):
            df['error'] = abs(df['exact_y'] - df['method_y'])

        return (df['x'].tolist(), df['error'].tolist())

