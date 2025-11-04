#
# Template for Task 1: Linear Regression 
#
import numpy as np
import matplotlib.pyplot as plt

# --- Your Task --- #
# import libraries as needed 
# .......
# --- end of task --- #

# -------------------------------------
# load data 
data = np.loadtxt('crimerate.csv', delimiter=',')
[n,p] = np.shape(data) #n = number of rows, p = number of columns
# 75% for training, 25% for testing 
num_train = int(0.75*n) #amount of training data 
num_test = int(0.25*n) #amount of testing data
sample_train = data[0:num_train,0:-1]
label_train = data[0:num_train,-1]
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]
# -------------------------------------

# --- Your Task --- #
# pick a proper number of iterations 
num_iter = 1000
# randomly initialize your w 
w = np.zeros(p-1) #there are p columns in our dataset so we have p-1 features. Thus, we need p-1 zeroes to account for each feature
bias = 0 #intialize bias to 0 
alpha = 0.001 #let learning rate (alpha) be 0.001, since learning rate is generally set really low
# --- end of task --- #

er_test = []


#gradient descent: slowly adjust weights in direction of less error
#find line that gives us lowest possible mean squared error (MSE)
#take partial derivative with respect to w and bias (gives direction of steepest ascent WRT w and bias)
#go opposite direction of gradient 

print("w shape: ", w.shape)
print("sample_train shape: ", sample_train.shape)

# --- Your Task --- #
# implement the iterative learning algorithm for w
# at the end of each iteration, evaluate the updated w 
for iter in range(num_iter): 
    #get predictions for sample train data all at once, by computing dot product of weight vector and sample_train with the bias
    #w shape: (100, ) which is a 1D numpy array with 100 elements
    #sample_train shape: (1494, 100)
    #therefore dimensions of dot product of sample_train and w: (1494, ) since inner dimensions cancel
    y_pred = np.dot(sample_train, w) + bias #has prediction for each sample in dataset

    #calculate partial derivative with respect to w and bias (gradients): Formulae from AssemblyAI YouTube video
    #can subtract label_train from y_pred to get errors because they have same shape
    #compute dot product of sample_train and (y_pred - label_train)
    #however, sample train has shape 1494 x 100, so we need to transpose to get new dimensions = 100 x 1494 
    gradient_w = (1 / num_train) * (2 * np.dot(sample_train.T, (y_pred - label_train))) #compute dot product to get gradient_w shape: (100, ) 
    gradient_bias = (1 / num_train ) * (2 * np.sum (y_pred - label_train))

    # update w and bias
    w = w - alpha * gradient_w   #w = w - learningRate(direction of steepest ascent = partial derivative with respect to w)
    bias = bias - alpha * gradient_bias

    ## evaluate testing error of the updated w 
    # we should measure mean-square-error here
    label_test_pred = np.dot(sample_test, w) + bias #predict label_test with unseen sample_test data 
    er = np.mean((label_test - label_test_pred) ** 2) #average all squared differences to get value that represents error across all samples
    er_test.append(er)
# --- end of task --- #
    
plt.figure()     
plt.plot(er_test)
plt.xlabel('Iteration')
plt.ylabel('Mean Squared Error')
plt.show()


