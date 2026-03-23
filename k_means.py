from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# sample data
data = {
    'Income': [15, 16, 17, 40, 42, 43, 70, 72, 75],
    'Score': [39, 81, 6, 77, 40, 76, 6, 94, 3]
}

df = pd.DataFrame(data)

kmeans = KMeans(n_clusters=3)
df['Cluster'] = kmeans.fit_predict(df)

plt.scatter(df['Income'], df['Score'], c=df['Cluster'])
plt.xlabel("Income")
plt.ylabel("Score")
plt.title("Customer Segmentation")
plt.show()