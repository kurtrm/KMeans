"""
make a basic k-means clustering algorithm.
"""
import numpy as np
import random


class KMeans:
    """
    Scratch KMeans clustering algorithm in Python with Numpy.
    """
    def __init__(self, k, max_iter=100):
        """
        Initialize KMeans with max_iter as 100.
        """
        self.k = k
        self.max_iter = max_iter
        self.centroids = None

    def fit(self, X):
        """
        Parameters
        ----------
        X: numpy array of data to cluster

        Returns
        -------
        dictionary of cluster assignments
        """
        starting_points = np.array(random.sample(X.tolist(), self.k))
        distances = np.zeros((len(starting_points), X.shape[0]))
        previous_assignments = np.zeros(len(X))
        for _ in range(self.max_iter):
            for idx, point in enumerate(X):
                diff = point - starting_points
                distances[:, idx] = np.linalg.norm(diff,
                                                   axis=1)
            assignments = np.argmin(distances, axis=0)
            for idx in range(self.k):
                starting_points[idx] = X[assignments == idx].mean(axis=0)
            if not (previous_assignments == assignments).all():
                previous_assignments = assignments
            else:
                break
        self.centroids = starting_points
        return assignments

    def _cluster_distances(self, X, assignments):
        """
        Calculate the SSE for each data point to its centroid.
        """
        arr = np.zeros(X.shape)
        for i, centroid in enumerate(self.centroids):
            arr[assignments == i] = centroid
        diff = arr - X
        return (diff**2).sum()
            
