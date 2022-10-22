


import tushare as ts

import numpy as np
import matplotlib.pyplot as plt

data=ts.get_k_data('600519')
plt.plot(data['high'])
plt.show()

