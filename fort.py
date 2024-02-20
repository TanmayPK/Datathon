import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import math


intv = pd.read_csv("interventions_belgium_full_id_with_dist.csv", index_col=0)


def lat_to_km(lat):
    return lat * 111.11111111111111


def lon_to_km(lon):
    return lon * 71.420845520726


intv["distance_from_center"] = intv.apply(
    lambda row: math.dist((row["lon"], row["lat"]), (50, 50)), axis=1
)

circle = np.sqrt()
