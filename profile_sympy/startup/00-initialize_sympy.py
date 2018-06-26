from __future__ import division
from sympy import *

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

init_printing()

import matplotlib.pyplot as plotter
import numpy as np

print("""
	+------------------------------------+
	| GLOBAL IMPORTS                     |
	|                                    |
	| plotter       Matplotlib plotter   |
	| np            Numpy module         |
	+------------------------------------+
""")
print("""
	PRE-DEFINED SYMBOLS

	x, y, z, t = symbols('x y z t')
	k, m, n = symbols('k m n', integer=True)
	f, g, h = symbols('f g h', cls=Function)
""")
