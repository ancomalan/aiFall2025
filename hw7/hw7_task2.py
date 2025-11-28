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
k_values = 10 # fix number of neurons per layer 
m_values = [1, 3, 5, 10, 20] # vary the number of layers (m)

# Underfitting refers to a model that can neither model the training data nor generalize to new data (high training and testing error)

er_train_m = []
er_test_m = []
for m in m_values: 
    layers = tuple(k_values for _ in range(m)) # create tuple representing the amount of hidden layers, each having 10 neurons
    model = MLPClassifier(hidden_layer_sizes=layers, max_iter=2000) # create MLP classification model with fixed number of neurons 
    model.fit(sample_train, label_train) # train a MLP classification model 
    
    # evaluate training error 
    label_train_pred = model.predict(sample_train)
    er_train = 1 - accuracy_score(label_train, label_train_pred)

    # evaluate testing error 
    label_test_pred = model.predict(sample_test)
    er_test = 1 - accuracy_score(label_test, label_test_pred)

    er_train_m.append(er_train)
    er_test_m.append(er_test)
   
plt.figure()
plt.plot(m_values,er_train_m, label='Training Error')
plt.plot(m_values,er_test_m, label='Testing Error')
plt.xlabel('m value') # need to change it to "m" value for figure 2
plt.ylabel('Classification Error')
plt.legend()
plt.show()

