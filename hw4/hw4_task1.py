import numpy as np
import matplotlib.pyplot as plt

# --- Your Task --- #
# import necessary library 
# if you need more libraries, just import them
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error #for data evaluation
# ......
# --- end of task --- #


# load a data set for regression
# in array "data", each row represents a community 
# each column represents an attribute of community 
# last column is the continuous label of crime rate in the community
data = np.loadtxt('crimerate.csv', delimiter=',', skiprows=1)
[n,p] = np.shape(data) #returns number of rows and columns as a tuple

# always use last 25% data for testing 
num_test = int(0.25*n)
sample_test = data[n-num_test:,0:-1] #starting from last 25% of data, get all attribute columns (features)
label_test = data[n-num_test:,-1] #starting from last 25% of data, get values in target column

# --- Your Task --- #
# now, vary the percentage of data used for training 
# pick 8 values for array "num_train_per" e.g., 0.5 means using 50% of the available data for training 
# You should aim to observe overiftting (and normal performance) from these 8 values 
# Note: maximum percentage is 0.75
num_train_per = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.65, 0.75]
# --- end of task --- #

er_train_per = []
er_test_per = []

for per in num_train_per: 

    # create training data and label 
    num_train = int(n*per)
    sample_train = data[0:num_train,0:-1]
    label_train = data[0:num_train,-1]
    
    # we will use linear regression model 
    model = LinearRegression()
    
    # --- Your Task --- #
    # now, training your model using training data 
    # (sample_train, label_train)
    # ......
    # ......
    model.fit(sample_train, label_train) #compares each set of features with target 
    # now, evaluate training error (MSE) of your model 
    # store it in "er_train"
    # ......
    label_train_pred = model.predict(sample_train) #predict label_train given sample_train
    er_train = mean_squared_error(label_train, label_train_pred) #compare actual value versus what model gave us 
    er_train_per.append(er_train)
    
    # now, evaluate testing error (MSE) of your model 
    # store it in "er_test"
    # ......
    label_test_pred = model.predict(sample_test) #predict label_test from unseen sample_test data to evaluate model's performance
    er_test = mean_squared_error(label_test, label_test_pred) #evaluate model on data it has never seen before 
    er_test_per.append(er_test)
    # --- end of task --- #
    
plt.plot(num_train_per,er_train_per, label='Training Error')
plt.plot(num_train_per,er_test_per, label='Testing Error')
plt.xlabel('Percentage of Training Data')
plt.ylabel('Prediction Error (MSE)')
plt.legend()
plt.show()


