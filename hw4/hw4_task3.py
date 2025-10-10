import numpy as np
import matplotlib.pyplot as plt

# --- Your Task --- #
# import necessary library 
# if you need more libraries, just import them
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error #for evaluating validation error for each alpha value
# ......
# --- end of task --- #

# load a data set for regression
# in array "data", each row represents a community 
# each column represents an attribute of community 
# last column is the continuous label of crime rate in the community
data = np.loadtxt('crimerate.csv', delimiter=',', skiprows=1)
[n,p] = np.shape(data) #n=rows and p=columns

# always use last 25% data for testing 
num_test = int(0.25*n)
sample_test = data[n-num_test:,0:-1] #get attribute columns using array slicing
label_test = data[n-num_test:,-1] #get last column containing label

# --- Your Task --- #
# now, pick the percentage of data used for training 
# remember we should be able to observe overfitting with this pick 
# note: maximum percentage is 0.75 
per = 0.2 #overfitting occurs when model is trained on a small portion of data (so choose small percentage of data) 
num_train = int(n*per) #amount of training data (number of rows) 
sample_train = data[0:num_train,0:-1] #contains data from all attribute columns of training set
label_train = data[0:num_train,-1] #contains label data of training set
# --- end of task --- #


# --- Your Task --- #
# We will use a regression model called Ridge. 
# This model has a hyper-parameter alpha. Larger alpha means simpler model. 
# Pick 5 candidate values for alpha (in ascending order)
# Remember we should aim to observe both overfitting and underfitting from these values 
# Suggestion: the first value should be very small and the last should be large 
alpha_vec = [0.00001, 0.01, 10, 100, 100000]
# --- end of task --- #

# er_train_alpha = []
# er_test_alpha = []
er_valid_alpha = [] #stores averaged k-fold cross validation error for each candidate alpha value
for alpha in alpha_vec: 
    validation_errors_unaveraged = [] #stores (unaveraged) k-fold cross validation errors for each alpha

    # pick ridge model, set its hyperparameter 
    model = Ridge(alpha = alpha)
    
    # --- Your Task --- #
    # now implement k-fold cross validation 
    # on the training set (which means splitting 
    # training set into k-folds) to get the 
    # validation error for each candidate alpha value 
    # store it in "er_valid"
    #----------------------------NOTES------------------------------------------
    #K-fold cross validation used when you do NOT have lot of data
    #take data and break into k even sized chunks (1...k)
    #validate on one of those chunks, and train on remaining trunks
    #do this repeatedly until you do this over all data
    #all data is used for training and validation (but only one piece at a time)
    #report average test set results over all these k-folds
    k = 5     #let k = 5
    for i in range(1, k+1):
        #get validation set
        validation_set_start = int((i-1) * num_train/k) #get row that validation set starts at (algorithm from textbook)
        validation_set_end = int(i * num_train/k) #get row that validation set ends at (algorithm from textbook)
        validation_sample_test = sample_train[validation_set_start:validation_set_end, :] #get all attribute columns . Predicting on this is used to evaluate validation error. 
        validation_label_test = label_train[validation_set_start:validation_set_end] #get all values in label column for validation set. Will be used as a comparison to the predicted value.
        
        #get training sets
        #if validation set is first chunk, all remaining rows after are used for training
        if (validation_set_start == 0):
            sample_training = sample_train[validation_set_end:num_train, :] 
            label_training = label_train[validation_set_end:num_train] 
        #if our validation is the last chunk, all rows before are used for training
        elif (validation_set_end == num_train):
            sample_training = sample_train[0:validation_set_start, :]
            label_training = label_train[0:validation_set_start]
        #if our validation set in between training sets, get training sets before and after the validation set and concatenate them
        else:
            sample_training = np.concatenate((sample_train[0:validation_set_start, :], sample_train[validation_set_end: num_train, :]), axis=0) #axis=0 means row-wise concatenation
            label_training = np.concatenate((label_train[0:validation_set_start], label_train[validation_set_end: num_train]), axis=0)
        
        #train model 
        model.fit(sample_training, label_training)

        #evaluate validation error for current fold
        validation_label_test_pred = model.predict(validation_sample_test) #after training model, predict validation_label_test from unseen validation_sample_test
        validation_error_current_fold = mean_squared_error(validation_label_test,validation_label_test_pred)#get MSE for current iteration
        validation_errors_unaveraged.append(validation_error_current_fold)#append to unaveraged validation error list 
    
    #get average validation error over all folds for current alpha and append to list
    er_valid = np.average(validation_errors_unaveraged)
    er_valid_alpha.append(er_valid)
    # --- end of task --- #

# Now you should have obtained a validation error for each alpha value 
# In the homework, you just need to report these values
print("Alpha Candidates: ", alpha_vec)
print ("Validation Errors: ", er_valid_alpha)
# The following practice is only for your own learning purpose.
# Compare the candidate values and pick the alpha that gives the smallest error 
# set it to "alpha_opt"
alpha_opt = 10
# now retrain your model on the entire training set using alpha_opt 
# then evaluate your model on the testing set 
model = Ridge(alpha = alpha_opt)

model.fit(sample_train, label_train)

#evaluate training error
label_train_predict = model.predict(sample_train)
er_train = mean_squared_error(label_train, label_train_predict)

#evaluate testing error
label_test_pred = model.predict(sample_test)
er_test = mean_squared_error(label_test, label_test_pred)

print ("Training error for model with optimal alpha: ", er_train)
print ("Testing error for model with optimal alpha: ", er_test)
    
