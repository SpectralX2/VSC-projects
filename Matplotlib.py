import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

linear_data = np.array([1,2,3,4])
fig=plt.figure()
plt.plot(linear_data, '-o')
fig.savefig('line.png')

fig=plt.figure()
[5,2,7,8,2]
plt.bar([1,2,4,7,8],[5,2,7,8,2])
fig.savefig('bar.png')