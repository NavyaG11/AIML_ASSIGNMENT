from sklearn.cluster import KMeans
import numpy as np

data = np.array([
    [25, 20000],
    [30, 25000],
    [35, 30000],
    [40, 50000],
    [45, 60000]
])

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

print("Customer Groups:", kmeans.labels_)