#
# Template for Task 3: Kmeans Clustering
#
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# --- Your Task --- #
# import libraries as needed 
from mpl_toolkits import mplot3d #for 3d scatter plot
# --- end of task --- #

# -------------------------------------
# load data 
# note we do not need label 
data = np.loadtxt('crimerate.csv', delimiter=',')
[n,p] = np.shape(data) # n samples, and p features 
sample = data[:,0:-1] #all features, no label
# -------------------------------------

# --- Your Task --- #
# pick a proper number of clusters 
k = 3
# --- end of task --- #

#computes distance between centroid and data point 
def euclidean_distance(centroid, point): 
     return np.sqrt(np.sum((centroid - point) ** 2))

#function calculates distance from datapoint from each centroid, returning the index of the centroid in initial_centroid_indexes
def get_closest_centroid(centroids, point): 
     #call euclidean_distance for each centroid and store inside list 
     distances = np.array([euclidean_distance(point, centroid) for centroid in centroids])
     return np.argmin(distances) #return the index of the cluster that the datapoint belongs to (index of minimum value)

#function returns updated centroids (sets center to mean of cluster)
def update_centroids(centroids, label_cluster, sample): 
     new_centroids = []
     #update each centroid 
     for idx in range(len(centroids)): 
          data = sample[label_cluster == idx] #get data points belonging to that cluster (filter numpy array using conditional)
          new_centroids.append(np.mean(data, axis=0))#compute new cluster by taking the mean for each feature across all points using axis=0
     return np.array(new_centroids)
#NOTES:
#1. initialize clusters randomly 
#2. update cluster labels (assign each data point to nearest centroid)
#3. Update centroid (set center to mean of cluster)
#use euclidean distance to get distance between two feature vectors
#stop algorithm when no more change or when we have reached max iterations

# --- Your Task --- #
# implement the Kmeans clustering algorithm 
label_cluster = np.zeros(n,dtype=int) #np array contains cluster label for each point (initially all 0)
# you need to first randomly initialize k cluster centers 
initial_centroid_indexes = np.random.choice(n, k, False) # choose k random samples from all samples (with no replacement), where n is number of samples
centroids = np.array([sample[idx] for idx in initial_centroid_indexes]) #store each centroid (vector) in numpy array


# then start a loop 
max_iters = 100
for _ in range(max_iters):
     #for each point, use euclidean distance to find closest cluster center to that point 
     #compute distance from point to each of the cluster centers 
     for idx in range(n):
          data_point = sample[idx]
          closest_centroid_idx = get_closest_centroid(centroids, data_point)

          # when clustering is done, 
          # store the clustering label in `label_cluster' 
          # cluster index starts from 0 e.g., 
          # label_cluster[0] = 1 means the 1st point assigned to cluster 1
          # label_cluster[1] = 0 means the 2nd point assigned to cluster 0
          # label_cluster[2] = 2 means the 3rd point assigned to cluster 2
          label_cluster[idx] = closest_centroid_idx #assign data point to closest cluster 
     
     new_centroids = update_centroids(centroids, label_cluster, sample) #update centroids (Center of each cluster) by taking mean of all points assigned to that cluster
     #if there is little difference between new_centroids and old_centroids, we can break since it has converged
     if np.allclose(new_centroids, centroids):
          break
     #otherwise, reinitialize old centroids with the new centroids and proceed with the algorithm 
     else: 
          centroids = new_centroids
# --- end of task --- #


# the following code plot your clustering result in a 2D space
pca = PCA(n_components=2)
pca.fit(sample)
sample_pca = pca.transform(sample)
idx = []
colors = ['blue','red','green','m']
for i in range(k):
     idx = np.where(label_cluster == i)
     plt.scatter(sample_pca[idx,0],sample_pca[idx,1],color=colors[i],facecolors='none')
plt.show()


#plotting clustering result in a 3D space
pca = PCA(n_components=3) #reduce data to 3 dimensions
pca.fit(sample)
sample_pca = pca.transform(sample)
idx = [] #stores indices of points in each cluster
colors = ['blue','red','green','m']
ax = plt.axes(projection='3d')
for i in range(k):
     idx = np.where(label_cluster == i)
     ax.scatter(sample_pca[idx,0],sample_pca[idx,1],sample_pca[idx, 2], color=colors[i],facecolors='none')
plt.show()