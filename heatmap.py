import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


aed = pd.read_csv("aed_geocoords.csv", index_col=0)

aed.dropna(subset=["lon", "lat"], inplace=True)


aed = aed[aed["lon"] < 10]

sns.kdeplot(
    data=aed[["lon", "lat"]],
    x="lon",
    y="lat",
    cmap="twilight",
    fill=True,
    thresh=0,
    bw_adjust=0.1,
    levels=100,
)

# Add labels and title
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Heatmap of Latitude and Longitude")


plt.show()

# plt.scatter(aed["lon"], aed["lat"], s=2)


intv = pd.read_csv("ant_interventions.csv", index_col=0)
intv = intv[["Longitude permanence", "Latitude permanence"]]
intv.rename(
    columns={"Longitude permanence": "lon", "Latitude permanence": "lat"}, inplace=True
)

intv.dropna(subset=["lon", "lat"], inplace=True)

print(intv)

sns.kdeplot(
    data=intv[["lon", "lat"]],
    x="lon",
    y="lat",
    cmap="magma",
    fill=False,
    thresh=0,
    levels=100,
)

plt.show()
