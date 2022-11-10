**DEPRECATED** This was only to try something out. If you are interested in a cool project doing computer algebra, have a look at https://mathics.org/.


Mathpython
==========

Make some math with Python modules (Sympy, Numpy, Matplotlib) as a leightweight Maple/Mathematica/Sage replacement.

After Checkout, issue the following commands to get it to work:

```
python3.6 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
ipython profile create sympy
```

Then start the environment with `./cli`. The startup scripts in `profile_sympy/startup` will show some examples for usage and predefined globals.

Links
-----

  - http://docs.sympy.org/latest/tutorial/
  - https://matplotlib.org/examples/index.html
  - https://www.python-kurs.eu/numerisches_programmieren_in_Python.php (in German)
