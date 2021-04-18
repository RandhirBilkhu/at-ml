import pandas as pd


df = pd.read_csv("winequality-red.csv")

quality_mapping ={
    4:0,
    5:1,
    6:2,
    3:3,
    7:4,
    8:5
}

df.loc[:, "quality"] = df.quality.map(quality_mapping)

df = df.sample(frac=1).reset_index(drop=True)

df_train = df.head(1000)
df_tesr = df.tail(599)