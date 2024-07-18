"""
Designed for plotting v1 datasets
"""

import pandas as pd
import mpl_scatter_density
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

dNBR3Y = pd.read_csv("D:/Research/Masters/8_RStudio/Input Data/ERA5/total/dNBR_total_3y.csv")

white_viridis = LinearSegmentedColormap.from_list('white_viridis', [
    (0, '#ffffff'),
    (1e-20, '#440053'),
    (0.2, '#404388'),
    (0.4, '#2a788e'),
    (0.6, '#21a784'),
    (0.8, '#78d151'),
    (1, '#fde624'),
], N=256)


print(dNBR3Y.isnull().sum().sum())
print(dNBR3Y.eq(0).sum().sum())

x = dNBR3Y["dNBR"]
y = dNBR3Y["mNBR"]


def using_mpl_scatter_density(fig, x, y):
    ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
    ax.set_xlabel("dNBR")
    ax.set_ylabel("Max Vegetation")
    density = ax.scatter_density(x, y, cmap=white_viridis)
    fig.colorbar(density, label='Number of points per pixel')


fig = plt.figure()
using_mpl_scatter_density(fig, x, y)
plt.show()

