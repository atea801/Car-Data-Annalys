import pandas as pd 
# import numpy as np 
# import matplotlib.pyplot as pyplot
# import seaborn as sns 

'''
DATA PREPARATION
'''

df = pd.read_csv("Cars.csv", sep=";")

# print(f"Shape of Dataset -> {df.shape}")

print(df.head())
#onremarque que les float sont avec des ',' et non des '.'

print(df.info())

#on remarque que des collonnes tel que MPG, displacement, horsepower, acceleration contiennent des objets et non des floats

for col in ['MPG', 'Displacement', 'Horsepower', 'Acceleration']:
    #on va remplacer les ',' par des '.'
    df[col] = df[col].str.replace(',', '.')
    print(df[['MPG', 'Displacement','Horsepower', 'Acceleration']])
    df[col] = df[col].astype(float)

df.info()