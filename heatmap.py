import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import RBFInterpolator, Rbf
import numpy as np

df = pd.read_csv("aed_geocoords.csv", index_col=0)

df.dropna(subset=["lon", "lat"], inplace=True)

df = df[["lon", "lat"]]

# df = df[df["lon"] < 10]

# df = df.head(50)

lon_min, lon_max = df["lon"].min(), df["lon"].max()
lat_min, lat_max = df["lat"].min(), df["lat"].max()

plt.scatter(df["lon"], df["lat"], s=2)

lon_obs = np.zeros((len(df), 2))
lon_obs[:, 0] = df["lon"].tolist()
lon_obs[:, 1] = df["lat"].tolist()

lat_obs = np.ones(len(df))


lon_grid = np.mgrid[2:7:1000j, 45:55:1000j]
lon_flat = lon_grid.reshape(2, -1).T

lat_flat = RBFInterpolator(
    lon_obs, lat_obs, kernel="linear", epsilon=1e-4, neighbors=3
)(lon_flat)
lat_grid = lat_flat.reshape(1000, 1000)

fig, ax = plt.subplots()
ax.pcolormesh(*lon_grid, lat_grid, vmin=-0.25, vmax=0.25, shading="gouraud")
p = ax.scatter(*lon_obs.T, c=lat_obs, s=2, ec="k", vmin=-0.25, vmax=0.25)
fig.colorbar(p)

plt.xlabel("longitude")
plt.ylabel("latitude")
# plt.grid(True)
plt.show()
