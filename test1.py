from google.colab import files
uploaded = files.upload()

import streamlit as st
import pandas as pd
import cv2
from google.colab.patches import cv2_imshow

st.write("""
# My first app
Hello *world!*
""")

# import cv2
# import math
# import matplotlib.pyplot as plt

# img = cv2.imread('sample.jpg')

# img = cv2.cvtColor(img, cv2.COLOR_RGB2RGB)
# plt.imshow(img)

