import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import math

intv_raw = pd.read_csv("interventions_belgium_full_id.csv", index_col=0)
intv = pd.read_csv("interventions_belgium_full_id_with_dist.csv", index_col=0)
intv = intv.merge(intv_raw, left_index=True, right_index=True)

intv = intv[intv["AED need level"] >= 2]

intv["log_min_distance_to_aed"] = np.log(intv["min_distance_to_aed"])

centers = {"brussels":[50.846667, 4.3525], "antwerp":[51.217778, 4.400278],
           "charleroi":[50.4, 4.433333], "namen":[50.466667, 4.866667],
           "luik":[50.639722, 5.570556], "arlon":[49.683333, 5.816667],
           "waver":[50.716667, 4.6 ]}

for city_name, city_center in centers.items():
    centers[city_name][0] = centers[city_name][0]*111.11111111111111
    centers[city_name][1] = centers[city_name][1]*71.420845520726





def lat_to_km(lat):
    return lat * 111.11111111111111


def lon_to_km(lon):
    return lon * 71.420845520726


intv["lat_km"] = intv['lat'] * 111.1111111111111111
intv["lon_km"] = intv['lon'] * 71.420845520726

def compute_mean_aed_distance(center, radius, f_intv):
    f_intv["distance_from_center"] = np.sqrt( (f_intv["lat_km"] - center[0])**2 + (f_intv["lon_km"] - center[1])**2 )
    new_f_intv = f_intv[f_intv['distance_from_center'] < radius]
    if len(new_f_intv) != 0:
        return new_f_intv["min_distance_to_aed"].mean()
    else:
        return 0

for city_name, city_center in centers.items():
    radiuses = np.linspace(0.125,10,2000)
    mean_distances = np.zeros(radiuses.shape)
    for i in range(len(radiuses)):
        mean_distances[i] = compute_mean_aed_distance(city_center, radiuses[i], intv)
    plt.plot(radiuses, mean_distances, label=city_name)
    print(city_name)
plt.legend()
plt.xlabel("Radius")
plt.ylabel("Mean AED-distance")
plt.show()

"""
intv["log_min_distance_to_aed"] = intv["log_min_distance_to_aed"].clip(
    lower=float(input("lower clip value : ")), upper=float(input("upper clip value : "))
)

plt.scatter(
    intv["lon"], intv["lat"], c=intv["log_min_distance_to_aed"], cmap="magma", s=5
)
plt.show()

print(intv["min_distance_to_aed"].mean())

"""