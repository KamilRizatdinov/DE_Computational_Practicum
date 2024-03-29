import pandas as pd
from error_workers.base_error import BaseError

class TotalError(BaseError):
    @staticmethod
    def calculate(local_errors, n0, nmax):
        total_errors = [max(map(abs, error)) for _, error in local_errors]
        grid_cells = range(n0, nmax + 1)

        return (grid_cells, total_errors)
