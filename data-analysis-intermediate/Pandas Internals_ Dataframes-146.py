## 1. Shared Indexes ##

import pandas as pd
fandango = pd.read_csv("fandango_score_comparison.csv")
print(fandango.head(2))
index = fandango.index
print(index)

## 2. Using Integer Indexes to Select Rows ##

fandango = pd.read_csv('fandango_score_comparison.csv')
first_last = fandango.iloc[[0,len(fandango)-1]]

## 3. Using Custom Indexes ##

fandango = pd.read_csv('fandango_score_comparison.csv')
fandango_films = fandango.set_index("FILM",inplace = False , drop = False)
print(fandango_films.head(5))

## 4. Using a Custom Index for Selection ##

movies = ["The Lazarus Effect (2015)","Gett: The Trial of Viviane Amsalem (2015)", "Mr. Holmes (2015)"]
best_movies_ever = fandango_films.loc[movies]

## 5. Apply() Logic Over the Columns in a Dataframe ##

import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))
print(deviations)


## 6. Apply() Logic Over Columns: Practice ##

double_df = float_df.apply(lambda x: x*2)
print(double_df.head(3))

halved_df = float_df.apply(lambda x: x/2)
print(halved_df.head(1))

## 7. Apply() Over Dataframe Rows ##

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
print(rt_mt_user)
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])

rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x),axis = 1)