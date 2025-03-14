import numpy as np
import pandas as pd
import simpsom as sps
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('airline-safety - airline-safety.csv')

x = data.drop(columns=['airline', "avail_seat_km_per_week"], axis=1)

net = sps.SOMNet(20, 20, x.values, PBC=True)
net.train(train_algo='batch', start_learning_rate=0.01, epochs=10000)

nap = np.array((net.project(x.values)))

kmeans = KMeans(n_clusters=3, max_iter=300, random_state=0)
y_art = kmeans.fit(nap)

data["labels"] = y_art.labels_

print(data[data["labels"] == 0].head(5))
print(data[data["labels"] == 1].head(5))
print(data[data["labels"] == 2].head(5))

labels = kmeans.labels_
centers = kmeans.cluster_centers_

plt.scatter(nap[:,0], nap[:,1], c=labels, cmap='viridis')
plt.scatter(centers[:,0], centers[:,1], marker='o', s=200, c='red', edgecolor='black')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-Means Kümeleme')
plt.show()




