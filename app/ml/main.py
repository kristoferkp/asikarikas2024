import pandas as pd
import tensorflow as tf
import pandas as pd
import tensorflow as tf
import numpy as np
import json

# Load the df
df = pd.read_csv('input.csv')

df = df.rename(columns={'Õhutemperatuur °C': 'temperature', 'Date Time': 'date', 'Tunni keskmine summaarne kiirgus W/m²' : 'radiation','Õhurõhk merepinna kõrgusel hPa' : 'pressure','Õhurõhk jaama kõrgusel hPa': 'pressure2','Tunni sademete summa mm' : 'precip','Suhteline õhuniiskus %' : 'humidity','Tunni miinimum õhutemperatuur °C' : 'tempmin','Tunni maksimum õhutemperatuur °C': 'tempmax','10 minuti keskmine tuule suund °' : 'winddir', '10 minuti keskmine tuule kiirus m/s' : 'windspeed', 'Tunni maksimum tuule kiirus m/s': 'windmax'})

date_time = pd.to_datetime(df['Aasta'].astype(str) + df['Kuu'].astype(str).str.zfill(2) + df['Päev'].astype(str).str.zfill(2) + df['Kell (UTC)'], format='%Y%m%d%H:%M')
df = df.drop(['Aasta', 'Kuu', 'Päev', 'Kell (UTC)'], axis=1)

df.dropna(inplace=True)
df.describe().transpose()

wv = df['windspeed']
bad_wv = wv == -9999.0
wv[bad_wv] = 0.0

max_wv = df['windmax']
bad_max_wv = max_wv == -9999.0
max_wv[bad_max_wv] = 0.0
wv = df.pop('windspeed')
max_wv = df.pop('windmax')

# Convert to radians.
wd_rad = df.pop('winddir')*np.pi / 180

# Calculate the wind x and y components.
df['Wx'] = wv*np.cos(wd_rad)
df['Wy'] = wv*np.sin(wd_rad)

# Calculate the max wind x and y components.
df['max Wx'] = max_wv*np.cos(wd_rad)
df['max Wy'] = max_wv*np.sin(wd_rad)

timestamp_s = date_time.map(pd.Timestamp.timestamp)

day = 24*60*60
year = (365.2425)*day

df['Day sin'] = np.sin(timestamp_s * (2 * np.pi / day))
df['Day cos'] = np.cos(timestamp_s * (2 * np.pi / day))
df['Year sin'] = np.sin(timestamp_s * (2 * np.pi / year))
df['Year cos'] = np.cos(timestamp_s * (2 * np.pi / year))


multi_lstm_model = tf.keras.models.load_model('multi_lstm_model.keras')
multi_lstm_model.summary()

mean = df.mean()
std = df.std()

#test_df = (df - mean) / std
test_df = df

reshaped_data = test_df.values.reshape(-1, 24, 16)

# Now you can use this reshaped data for prediction
predictions = multi_lstm_model.predict(reshaped_data)


# Print the temperature reading

elem = ['Õhutemperatuur °C', 'Date Time', 'Tunni keskmine summaarne kiirgus W/m²','Õhurõhk merepinna kõrgusel hPa','Õhurõhk jaama kõrgusel hPa','Tunni sademete summa mm' ,'Suhteline õhuniiskus %' ,'Tunni miinimum õhutemperatuur °C' ,'Tunni maksimum õhutemperatuur °C', 'Wx', 'Wy', 'Tunni maksimum tuule kiirus m/s', 'Day sin', 'Day cos', 'Year sin', 'Year cos']
andmed = {}
for f in range(16):
    andmed[elem[f]] = []

for i in predictions[1]:
    for f in range(16):
        andmed[elem[f]].append(i[f])

temp = [std.temperature*i+mean.temperature for i in andmed['Õhutemperatuur °C']]

with open('../src/components/data.json', 'w') as f:
    json.dump(temp, f)
