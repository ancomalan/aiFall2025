import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

data = np.loadtxt('diabetes.csv', delimiter=',', skiprows=1)
[n,p] = np.shape(data)

# training data 
num_train = int(0.5*n)
sample_train = data[0:num_train,0:-1]
label_train = data[0:num_train,-1]
# testing data 
num_test = int(0.5*n)
sample_test = data[n-num_test:,0:-1]
label_test = data[n-num_test:,-1]

# ----------------------- #
# --- Hyper-Parameter --- #
# ----------------------- #
k = 10 # fix number of neurons per layer
m = 3 # fix number of layers
layers = tuple(k for _ in range(m)) # create tuple representing number of neurons per layer


model = MLPClassifier(activation='relu', hidden_layer_sizes=layers, max_iter=5000) # create new MLP model with 
model.fit(sample_train, label_train) # train a MLP classification model 

    
# evaluate training error 
label_train_pred = model.predict(sample_train)# make prediction on training data 
er_train = 1 - accuracy_score(label_train, label_train_pred)

#evaluate testing error
label_test_pred = model.predict(sample_test) # predict unseen test labels from unseen test samples
er_test = 1 - accuracy_score(label_test, label_test_pred)
   
print ("Training Error: ", er_train)
print ("Testing Error: ", er_test)


