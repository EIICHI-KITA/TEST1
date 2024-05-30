# pip install matplotlib
# !pip install -q matplotlib
# import matplotlib.pyplot as plt

from pathlib import Path
import colorsys
from typing import Tuple, List
from dataclasses import dataclass

# from geopandas.plotting import _plot_polygon_collection, _plot_linestring_collection
# from geopandas import GeoDataFrame
import numpy as np
# from matplotlib.colors import ListedColormap, cnames, to_rgb
# from matplotlib.pyplot import subplots, Rectangle
# import matplotlib.font_manager as fm
# from matplotlib.patches import Ellipse
# import matplotlib.patheffects as PathEffects

# from prettymapp.settings import STREETS_WIDTH

x_values = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']
y_values = [100, 130, 80, 150, 140, 130]

plt.bar(x_values, y_values)
plt.plot()

plt.show()
