pip3 install matplotlib

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x_values = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']
y_values = [100, 130, 80, 150, 140, 130]

plt.bar(x_values, y_values)
plt.plot()

plt.show()
