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
    bw_adjust=0.2,
    levels=100,
)

# plt.scatter(aed["lon"], aed["lat"], s=2)

# Add labels and title
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Heatmap of Latitude and Longitude")


plt.show()


intv = pd.read_csv("interventions_belgium.csv", index_col=0)
intv["Latitude intervention"] = intv.index
intv = intv[intv["AED need level"] >= 2]
intv = intv[["Longitude intervention", "Latitude intervention"]]
intv.rename(
    columns={"Longitude intervention": "lon", "Latitude intervention": "lat"},
    inplace=True,
)

intv.dropna(subset=["lon", "lat"], inplace=True)

# plt.scatter(intv["lon"], intv["lat"], s=2)

sns.kdeplot(
    data=intv[["lon", "lat"]],
    x="lon",
    y="lat",
    cmap="twilight",
    fill=True,
    thresh=0,
    bw_adjust=0.2,
    levels=100,
)

plt.show()
