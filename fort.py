import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import math


intv = pd.read_csv("interventions_belgium_full_id_with_dist.csv", index_col=0)


intv["log_min_distance_to_aed"] = np.log(intv["min_distance_to_aed"])



center = [50.84746322583217, 4.35145816798301]
center[0] = center[0]*111.11111111111111
center[1] = center[1]*71.420845520726
radius = 5.




def lat_to_km(lat):
    return lat * 111.11111111111111


def lon_to_km(lon):
    return lon * 71.420845520726


intv["lat_km"] = intv['lat'] * 111.1111111111111111
intv["lon_km"] = intv['lon'] * 71.420845520726

intv["distance_from_center"] = np.sqrt( (intv["lat_km"] - center[0])**2 + (intv["lon_km"] - center[1])**2 )

intv = intv[intv['distance_from_center'] < radius]

plt.hist(intv["log_min_distance_to_aed"], bins=30)
plt.show()

intv["log_min_distance_to_aed"] = intv["log_min_distance_to_aed"].clip(
    lower=float(input("lower clip value : ")), upper=float(input("upper clip value : "))
)

plt.scatter(
    intv["lon"], intv["lat"], c=intv["log_min_distance_to_aed"], cmap="magma", s=5
)
plt.show()

print(intv["min_distance_to_aed"].mean())



