import pandas as pd

aed_df = pd.read_parquet("data/aed_locations.parquet.gzip")
ambulance_df = pd.read_parquet("data/ambulance_locations.parquet.gzip")
interventions1_df = pd.read_parquet("data/interventions1.parquet")

print(aed_df)
aed_df.dropna(inplace=True)
print(aed_df)

print(ambulance_df)
ambulance_df.dropna(inplace=True)
print(ambulance_df)

print(interventions1_df)
interventions1_df.dropna(inplace=True)
print(interventions1_df)
