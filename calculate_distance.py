import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist, cityblock
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from tqdm import tqdm


aed = pd.read_csv("aed_geocoords.csv", index_col=0)
intv = pd.read_csv("interventions_belgium_full_id.csv", index_col=0)


aed.dropna(subset=["lon", "lat"], inplace=True)
aed = aed[aed["lon"] < 10]
aed["coord"] = list(zip(aed["lon"], aed["lat"]))


intv = intv[["Longitude intervention", "Latitude intervention"]]
intv.rename(
    columns={"Longitude intervention": "lon", "Latitude intervention": "lat"},
    inplace=True,
)
intv.dropna(subset=["lon", "lat"], inplace=True)

# intv = intv.iloc[:500]


def get_closest_aed(row):
    intv_coord = np.array([[row["lon"], row["lat"]]])
    aed_coords = aed["coord"].values
    aed_coords = np.array([np.array([x, y]) for x, y in aed_coords])

    distance_to_aeds = cdist(aed_coords, intv_coord, "cityblock")
    min_distance_to_aed = np.min(distance_to_aeds)

    closest_aed = aed_coords[np.where(distance_to_aeds == min_distance_to_aed)[0]][0]

    return closest_aed[0], closest_aed[1], min_distance_to_aed


tqdm.pandas()
intv[["closest_aed_lon", "closest_aed_lat", "min_distance_to_aed"]] = (
    intv.progress_apply(get_closest_aed, axis=1, result_type="expand")
)

intv.to_csv("interventions_belgium_full_id_with_dist.csv")

# intv[intv["min_distance_to_aed"] > 0.01] = 0.01

# print(intv)

# plt.scatter(intv["lon"], intv["lat"], color="red", s=2)
# plt.scatter(
#     intv["closest_aed_lon"],
#     intv["closest_aed_lat"],
#     c=intv["min_distance_to_aed"],
#     cmap="ocean",
#     s=5,
# )
# plt.show()
