import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from datetime import datetime

data = pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/athletes.csv')

now = pd.Timestamp(datetime.now())
data['dob'] = pd.to_datetime(data['dob'], errors='coerce')
data['dob'] = data['dob'].where(data['dob'] < now, data['dob'] - pd.DateOffset(years=100))

data['age'] = data['dob'].apply(lambda x: (now - x).days // 365 if pd.notnull(x) else None)

data['height'] = data['height'].fillna(0)
data['age'] = data['age'].fillna(0)
data = data[data['height'] > 0]
data = data[data['age'] > 0]

female = data[data['sex'] == 'female']

fig = plt.figure()
legend = []
sports = ['hockey', 'boxing', 'cycling']

for sport in sports:
    plt.scatter(
        female['height'][female['sport'] == sport],
        female['age'][female['sport'] == sport]
    )
    legend.append(sport)

plt.legend(legend, loc=2, numpoints=3)
plt.title('Female Height and Age Relation in Sports')
plt.xlabel('Height')
plt.ylabel('Age')
plt.show
fig.savefig("height_age.png")