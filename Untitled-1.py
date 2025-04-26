import pandas as pd
import numpy as np
df=pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/athletes.csv')
#print(df[['sport','name']])

#athletic=df.where(df['sport']== 'athletics')
#print(athletic.head())

print(df['nationality'].value_counts()[:30])

gold = df.groupby('nationality').sum()['gold']
silver = df.groupby('nationality').sum()['silver']
bronze = df.groupby('nationality').sum()['bronze']
total_medals = gold + silver + bronze
print(total_medals)
print(gold['USA'])