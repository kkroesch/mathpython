
def f(x):
    return 2*x

def g(x):
    return - Rational(1,2) * x

linear_example = """
        f(x)

        g(x)

        lin = [(f(i), g(i)) for i in range(10)]

        plotter.plot(lin)
        plotter.show()

        f(x) + g(x)
"""

print("    EXAMPLE: Linear Functions")
print(linear_example)
