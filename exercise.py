import pandas as pd
import numpy as np
import matplotlib as plt
#%matplotlib inline

df = pd.read_csv("train_u6lujuX_CVtuZ9i.csv") #Reading the dataset in a dataframe using Pandas

print("file loaded.")
print(df.head(10))
print(df.describe())
print(df['Property_Area'].value_counts())

df['ApplicantIncome'].hist(bins=50)