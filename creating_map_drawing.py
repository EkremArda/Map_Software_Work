import matplotlib.pyplot as plt
import numpy as np
XY_list = [(-4, 14), (2, 15), (3, 16), (4, 17), (5, 18), (6, 19), (7, 20), (8, 21), (9, 22), (10, 23), (11, 24), (12, 25), (13, 26)]
xler = [x[0] for x in XY_list]
yler = [y[1] for y in XY_list]
plt.plot(xler, yler)
