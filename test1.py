import cv2
import math
import matplotlib.pyplot as plt

img = cv2.imread('sample.jpg')

img = cv2.cvtColor(img, cv2.COLOR_RGB2RGB)
plt.imshow(img)

