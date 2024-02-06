import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

csv_path = './III - Ilmaennustus/Tallinn-Harku-2004-2023.csv'
df = pd.read_csv(csv_path)
print(df.columns)

df['Kell (UTC)'] = df['Kell (UTC)'].str.replace('.', ':')

# Combine 'Aasta', 'Kuu', 'Päev' and 'Kell (UTC)' into a datetime
df['Date Time'] = pd.to_datetime(df['Aasta'].astype(str) + df['Kuu'].astype(str).str.zfill(2) + df['Päev'].astype(str).str.zfill(2) + df['Kell (UTC)'], format='%Y%m%d%H:%M')

# Remove the 'Date Time' column
df = df.drop(['Aasta', 'Kuu', 'Päev', 'Date Time'], axis=1)

print(df.describe().transpose())