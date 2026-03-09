import numpy as np
from sklearn.mixture import GaussianMixture

# Sample dataset
X = np.array([[1],[2],[3],[10],[11],[12]])

# EM using Gaussian Mixture
gmm = GaussianMixture(n_components=2)

gmm.fit(X)

labels = gmm.predict(X)

print("Data Points:")
print(X.flatten())

print("\nCluster Labels:")
print(labels)
