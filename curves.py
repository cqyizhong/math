import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.figure(1)
x = np.linspace(1, 200, 400)
y=1000*(2.0-169.0/x)
y[x<84.5] = 0
y[x>169]=1000
plt.plot(x, y)
plt.show()
