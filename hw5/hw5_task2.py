#
# Template for Task 2: Logistic Regression 
#
import numpy as np
import matplotlib.pyplot as plt
# --- Your Task --- #
# import libraries as needed 
# .......
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
# pick a proper number of iterations 
num_iter = 10000
# randomly initialize your w 
w = np.zeros(p-1) #since dataset has p columns, then we have p-1 features (last column is label) and thus need p-1 zeros for each feature
bias = 0 #initialize bias to 0 
alpha = 0.1 # learning rate should generally be set to something small
# --- end of task --- #

er_test = []

print("w (weights) shape: ", w.shape)
print("sample_train shape: ", sample_train.shape)

# --- Your Task --- #
# implement the iterative learning algorithm for w
# at the end of each iteration, evaluate the updated w 
for iter in range(num_iter): 
    #get predictions for each sample all at once using matrix
    #compute dot product of sample_train and w (inner dimensions cancel) 
    #np.exp(x) returns e^x
    y_pred = 1 / (1 + np.exp(-1 * (np.dot(sample_train, w) + bias))) #y_pred has shape: (576, )

    #perform gradient descent (calculate gradient)
    #formula for gradient_w and gradient_b from AssemblyAI YouTube video
    #we need to transpose sample_train to get new dimensions (8 x 576) in order to compute dot product with (y_pred-label_train)
    #gradient shape will be (8, ) which is a 1 dimensional numpy array with 8 elements
    gradient_w = (1 / num_train) * np.dot(sample_train.T, (y_pred - label_train))
    gradient_bias = (1 / num_train) * np.sum(y_pred - label_train)

    # update w and bias
    w = w - alpha * gradient_w
    bias = bias - alpha * gradient_bias

    # evaluate testing error of the updated w 
    # we should measure classification error here 
    label_test_pred = 1 / (1 + np.exp(-1 * (np.dot(sample_test, w) + bias))) #label_test_pred has shape: (576, ) (this variable stores probabilities for each sample)
    class_predictions = [0 if prob <= 0.5 else 1 for prob in label_test_pred] #set class label based on probability (if probability <= 0.5 then label is 0, otherwise label is 1)
    accuracy = np.sum(class_predictions == label_test) / num_test #compute accuracy: (np.sum gets number of correct predictions)/total number predictions
    er = 1 - accuracy # classification error = 1 - accuracy
    er_test.append(er)
# --- end of task --- #


plt.figure()    
plt.plot(er_test)
plt.xlabel('Iteration')
plt.ylabel('Classification Error')
plt.show()


