# pip install matplotlib
# !pip install -q matplotlib
# import matplotlib.pyplot as plt

from pathlib import Path
import colorsys
from typing import Tuple, List
from dataclasses import dataclass

import numpy as np

import matplotlib.pyplot as plt
import numpy as np

x_values = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']
y_values = [100, 130, 80, 150, 140, 130]

plt.bar(x_values, y_values)
plt.plot()

plt.show()
