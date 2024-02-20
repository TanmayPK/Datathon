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

centers = {"Brussels":[50.846667, 4.3525], "Antwerp":[51.217778, 4.400278],
           "Charleroi":[50.4, 4.433333], "Namen":[50.466667, 4.866667],
           "Luik":[50.639722, 5.570556], "Arlon":[49.683333, 5.816667]}

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
"""
for city_name, city_center in centers.items():
    radiuses = np.linspace(0.125,10,20)
    mean_distances = np.zeros(radiuses.shape)
    for i in range(len(radiuses)):
        mean_distances[i] = compute_mean_aed_distance(city_center, radiuses[i], intv)
    plt.plot(radiuses, mean_distances, label=city_name)
    print(city_name)
plt.legend()
plt.xlabel("Radius")
plt.ylabel("Mean AED-distance")
plt.show()

mean_distances = np.zeros(len(centers))
c=0
for city_name, city_center in centers.items():
    radius = 0.3
    mean_distances[c] = compute_mean_aed_distance(city_center, radius, intv)
    c+=1
    
plt.bar(range(len(mean_distances)), mean_distances, align='center')
plt.xticks(range(len(centers)), list(centers.keys()))
plt.ylabel("Mean Distance from AED")
plt.title("Mean distance from AED in case of incident in City Center")
plt.show()
print(city_name)

"""
radius = 1000
center=centers["Brussels"]
print(len(intv))
intv["distance_from_center"] = np.sqrt( (intv["lat_km"] - center[0])**2 + (intv["lon_km"] - center[1])**2 )
intv = intv[intv['distance_from_center'] < radius]
print(len(intv))

plt.hist(intv["log_min_distance_to_aed"], bins=100)
plt.show()

intv["log_min_distance_to_aed"] = intv["log_min_distance_to_aed"].clip(
    lower=float(input("lower clip value : ")), upper=float(input("upper clip value : "))
)

plt.scatter(
    intv["lon"], intv["lat"], c=intv["log_min_distance_to_aed"], cmap="magma", s=5
)
plt.show()

print(intv["min_distance_to_aed"].mean())

