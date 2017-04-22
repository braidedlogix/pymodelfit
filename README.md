# pymodelfit
Python3, mostly-working, version of pymodelfit

This version requires traits/traitsui/pyface/chaco/kiva/enable versions for python 3. Also needs scipy/numpy.

If the pre-requisites are installed, the folder of this pure python program can be directly dropped into or removed from the python site-packages directory, or it can be placed into a program path, or be placed in the PYTHON_PATH.

Under windows, the package has some glitches with the number entry boxes. The active text box and mouse cursor are out of sync occasionally, but can be resynced by pressing the tab key a few times.

Under Linux Mint 18.1, which uses gcc version 5.4, there is a problem with the colorbar inducing a seg fault in the wx/agg backend used under kiva.


Original:

Author: Erik Tollerud
Documentation: PyModelFit package documentation
Home Page: http://packages.python.org/PyModelFit/
License: Apache License 2.0 
