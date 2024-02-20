import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


intv = pd.read_csv("interventions_belgium_full_id_with_dist.csv", index_col=0)
intv.dropna(subset=["lon", "lat"], inplace=True)

tqdm.pandas()
intv["log_min_distance_to_aed"] = np.log(intv["min_distance_to_aed"])

intv["log_min_distance_to_aed"] = intv["log_min_distance_to_aed"].clip(
    lower=-10, upper=-2.5
)

intv = intv[intv["lat"] >= 49]

plt.scatter(
    intv["lon"], intv["lat"], c=intv["log_min_distance_to_aed"], cmap="magma", s=5
)
plt.show()
plt.savefig("distance_aed_interventions.png")
