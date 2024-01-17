import pandas as pd 
import numpy as np 
import matplotlib.pyplot as pyplot
import seaborn as sns 

df = pd.read_csv("Cars.csv", sep=";")

# print(f"Shape of Dataset -> {df.shape}")

print(df.head())

print(df.info())