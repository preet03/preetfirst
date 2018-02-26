import pandas as pd
import numpy as np
url="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv(url,header=None)
headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
df.columns=headers
df["symboling"]=df["symboling"]+1
df.dropna(subset=["price"], axis=0, inplace=True)
meann=df["normalized-losses"].mean()
df["normalized-losses"].replace(0,meann)
print(df.head(5))

