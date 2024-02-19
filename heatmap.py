import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv("aed_geocoords.csv", index_col=0)

df.dropna(subset=["lon", "lat"], inplace=True)


df = df[df["lon"] < 10]

sns.kdeplot(
    data=df[["lon", "lat"]],
    x="lon",
    y="lat",
    cmap="twilight",
    fill=False,
    thresh=0,
    levels=100,
)

# Add labels and title
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Heatmap of Latitude and Longitude")


plt.show()

# plt.scatter(df["lon"], df["lat"], s=2)
