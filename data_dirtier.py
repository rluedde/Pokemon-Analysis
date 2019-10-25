import pandas as pd
import random

data = pd.read_csv("pokemon_data.csv")

cells_to_affect = int(len(data) * .05) 
# how many cells per column are going to have 
# values removed 
columns_to_affect =["Speed","Sp. Def","HP"] 
# the colums that are going to be affected 

# removes cells_to_affect cells per column in columns_to_affect
for column in columns_to_affect:
    indices_to_change = random.sample(range(len(data)),cells_to_affect)
    for index in indices_to_change:
        data.at[index,column] = None

data.to_csv("dirty.csv",index = False)

# MAKE SURE THAT THERE ARE cells_to_affect CELLS ER COLUMN THAT ACTULALYH GOT AFFECTED