import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

intv = pd.read_csv("interventions_belgium_full_id.csv", index_col=0)
print(intv.columns)
intv = intv[intv["waiting_time"]<120]
print(f'Intervention mean waiting time : {intv[intv["AED need level"]>=0]["waiting_time"].mean()}')
plt.hist(intv["waiting_time"], bins=100, range=[0,120])
plt.show()

print(f'Intervention mean waiting time : {intv[intv["AED need level"]>=3]["waiting_time"].mean()}')