#
# Template for Task 4: kNN Classification 
#
import numpy as np
import matplotlib.pyplot as plt

# --- Your Task --- #
# import libraries as needed 
from collections import Counter #idea from AssemblyAI to implement getting label with majority vote
# --- end of task --- #

# -------------------------------------
# load data 
data = np.loadtxt('diabetes.csv', delimiter=',')
[n,p] = np.shape(data)
# 75% for training, 25% for testing 
num_train = int(0.75*n)
num_test = int(0.25*n)
sample_train = data[0:num_train,0:-1]
label_train = data[0:num_train,-1]
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]
# -------------------------------------


# --- Your Task --- #
# pick five values of k by yourself 
k_values = [1,3,5,7,9] #odd values of k prevents ties in majority voting 
# --- end of task --- #

#function computes distance between two points
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a-b) ** 2))

#function computes distance from a point to all other points in dataset
def get_distances(unseen_point, sample_train):
    distances = np.array([euclidean_distance(unseen_point, sample) for sample in sample_train]) #get distance from each point in sample_train and store in this list
    return distances 

#function gets the k closest points and returns label with majority vote
def kNN(k, distances, label_train): 
    sorted_indices = np.argsort(distances)#get the indexes of k closest data points by using np.argsort(), which returns indices of array in sorted, ascending order 
    k_indices = sorted_indices[0: k] #get first k indices, using array slicing (includes start index, but excludes end index) 
    training_labels = label_train[k_indices] #get class labels for k closest neighbors 
    
    #create a counter object on the training labels to find label with majority vote
    counter = Counter(training_labels)
    result = counter.most_common(1) #returns list containing one tuple (most common element and its count)
    majority_label = result[0][0] #we need to access tuple (first element in list), then label (first element in tuple)
    return majority_label


#NOTES: 
#Given data point, calculate distance from this point to all other data points in dataset
#get the closest k points 
#get average of k nearest neighbors (regression) or get label with majority vote (classification)

er_test = []
for k in k_values: 
    # --- Your Task --- #
    # implement the kNN classification method 
    predictions = [] #stores the predicted label for each data point in sample_test (used to evaluate classification error later)

    # predict for each data point in sample_test
    for idx in range(num_test): 
        unseen_point = sample_test[idx] #get data point from sample_test
        distances = get_distances(unseen_point,sample_train)#calculate unseen points euclidean distance to each point in sample_train
        predicted_label = kNN(k,distances,label_train) #get predicted class label for this unseen point 
        predictions.append(predicted_label)

    #convert predictions list to numpy array to check classification error 
    predictions = np.array(predictions)

    #compute accuracy (number of correct predictions)/total number of predictions
    accuracy = np.sum(predictions == label_test) / num_test #get number of correct predictions using np.sum
    # store classification error on testing data here 
    er = 1 - accuracy
    er_test.append(er)
# --- end of task --- #
    
plt.figure()    
plt.plot(k_values, er_test, marker='.')
plt.xlabel('k')
plt.ylabel('Classification Error')
plt.show()


