import pandas as pd

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=xml&starttime=2024-01-01&endtime=2025-01-02&minmagnitude=5"
df = pd.read_csv(url, sep="|")

print(df)

print(df.head())