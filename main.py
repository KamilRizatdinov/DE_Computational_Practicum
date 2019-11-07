from math import exp, cos, tan, sin
import matplotlib
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import ttk 

from error_workers.local_error import LocalError
from error_workers.total_error import TotalError
from numeric_methods.base_solution import BaseSolution
from numeric_methods.euler import Euler
from numeric_methods.improved_euler import ImprovedEuler 
from numeric_methods.runge_kutta import RungeKutta 
from numeric_methods.exact import Exact 

root = Tk()
root.title("DE Assignment")
matplotlib.use('TkAgg')

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

x_initial = DoubleVar()
y_initial = DoubleVar()
x_final = DoubleVar()
n_approximation = IntVar()
n_initial = IntVar()
n_final = IntVar()

text = Label(mainframe, text="" \
        "This program is created by student of " \
        "Innopolis University Kamil Rizatdinov" \
        "\n It is solver of y' = 2e^x-y")
text.grid(columnspan=2, pady=10)

text = Label(mainframe, text="Approximation methods and local error:")
text.grid(row=1, columnspan=2, pady=10)

x_initial_text = Label(mainframe, text='x0 ')
x_initial_text.grid(row=2, sticky=E)
x_initial_entry = ttk.Entry(mainframe, width=10, textvariable=x_initial)
x_initial_entry.grid(column=1, row=2, sticky=W)

y_initial_text = Label(mainframe, text='y0')
y_initial_text.grid(row=3, sticky=E)
y_initial_entry = ttk.Entry(mainframe, width=10, textvariable=y_initial)
y_initial_entry.grid(column=1, row=3, sticky=W)

x_final_text = Label(mainframe, text='X ')
x_final_text.grid(row=4, sticky=E)
x_final_entry = ttk.Entry(mainframe, width=10, textvariable=x_final)
x_final_entry.grid(column=1, row=4, sticky=W)

n_text = Label(mainframe, text='N ')
n_text.grid(row=5, sticky=E)
n_approximation_entry = ttk.Entry(mainframe, width=10, textvariable=n_approximation)
n_approximation_entry.grid(column=1, row=5, sticky=W)

text = Label(mainframe, text="Total error:")
text.grid(row=6, columnspan=2, pady=10)

n_initial_text = Label(mainframe, text='n0 ')
n_initial_text.grid(row=7, sticky=E)
n_initial_entry = ttk.Entry(mainframe, width=10, textvariable=n_initial)
n_initial_entry.grid(column=1, row=7, sticky=W)

n_final_text = Label(mainframe, text='n max ')
n_final_text.grid(row=8, sticky=E)
n_final_entry = ttk.Entry(mainframe, width=10, textvariable=n_final)
n_final_entry.grid(column=1, row=8, sticky=W)


def diffeq(x, y):
    #return 5 - x**2 - y**2 + 2*x*y
    return 2*exp(x)-y
    # return (3*y+2*x*y)/x**2
    # return 1 / cos(x) - y * tan(x)


def exact_solution(x, x0, y0):
    #return 1/(BaseSolution.constant(x0, y0) * exp(4*x) - 0.25) + x + 2
    return (exp(2*x) + BaseSolution.constant(x0, y0)) / exp(x)
    # return BaseSolution.constant(x0, y0) * exp(-3/x) * x**2
    # return (tan(x) + BaseSolution.constant(x0, y0)) / (1/cos(x))


def func(x_initial, y_initial, x_final, n_approximation, n_initial, n_final):
    exact_points = Exact.solve(x_initial, y_initial, x_final, n_approximation, exact_solution)
    euler_points = Euler.solve(x_initial, y_initial, x_final, n_approximation, diffeq)
    improved_euler_points = ImprovedEuler.solve(x_initial, y_initial, x_final, n_approximation, diffeq)
    runge_kutta_points = RungeKutta.solve(x_initial, y_initial, x_final, n_approximation, diffeq)

    euler_local_error_points = LocalError.calculate(exact_points, euler_points)
    improved_euler_local_error_points = LocalError.calculate(exact_points, improved_euler_points)
    runge_kutta_local_error_points = LocalError.calculate(exact_points, runge_kutta_points)

    plt.figure()

    plt.subplot(1, 3, 1)
    plt.plot(*euler_points, label='Euler')
    plt.plot(*improved_euler_points, label='Improved Euler')
    plt.plot(*runge_kutta_points, label='Runge Kutta')
    plt.plot(*exact_points, label='Exact Solution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Functions')
    plt.grid()
    plt.legend(loc='best')

    plt.subplot(1, 3, 2)
    plt.plot(*euler_local_error_points, label='Euler')
    plt.plot(*improved_euler_local_error_points, label='Improved Euler')
    plt.plot(*runge_kutta_local_error_points, label='Runge Kutta')
    plt.title('Local Errors')
    plt.xlabel('x')
    plt.ylabel('Error')
    plt.grid()
    plt.legend(loc='best')

    if n_initial and n_final:
        euler_local_errors = []
        improved_euler_local_errors = []
        runge_kutta_local_errors = []

        for i in range(n_initial, n_final + 1):
            exact_points = Exact.solve(x_initial, y_initial, x_final, i, exact_solution)
            euler_points = Euler.solve(x_initial, y_initial, x_final, i, diffeq)
            improved_euler_points = ImprovedEuler.solve(x_initial, y_initial, x_final, i, diffeq)
            runge_kutta_points = RungeKutta.solve(x_initial, y_initial, x_final, i, diffeq)

            euler_local_error_points = LocalError.calculate(exact_points, euler_points)
            improved_euler_local_error_points = LocalError.calculate(exact_points, improved_euler_points)
            runge_kutta_local_error_points = LocalError.calculate(exact_points, runge_kutta_points)

            euler_local_errors.append(euler_local_error_points)
            improved_euler_local_errors.append(improved_euler_local_error_points)
            runge_kutta_local_errors.append(runge_kutta_local_error_points)

        euler_total_error_points = TotalError.calculate(euler_local_errors, n_initial, n_final)
        improved_euler_total_error_points = TotalError.calculate(improved_euler_local_errors, n_initial, n_final)
        runge_kutta_total_error_points = TotalError.calculate(runge_kutta_local_errors, n_initial, n_final)

        plt.subplot(1, 3, 3)
        plt.plot(*euler_total_error_points, label='Euler')
        plt.plot(*improved_euler_total_error_points, label='Improved Euler')
        plt.plot(*runge_kutta_total_error_points, label='Runge Kutta')
        plt.xlabel('N') 
        plt.ylabel('Error')
        plt.title('Total Errors')
        plt.grid()
        plt.legend(loc='best')

    plt.show()

ttk.Button(mainframe, 
        text="Plot", 
        command=lambda: func(x_initial.get(), 
            y_initial.get(), 
            x_final.get(), 
            n_approximation.get(), 
            n_initial.get(), 
            n_final.get())).grid(columnspan=2, row=9, pady=10)

root.mainloop()
