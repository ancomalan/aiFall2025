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
k_values = [1, 5, 10, 20, 50]     # five values for k

# less neurons (more simple model can't learn complexities in data) leads to underfitting: poor performance on both training and testing sets 
# more neurons leads to overfitting on training data as model becomes overly complex 
# underfitting (high training & testing error for small k) and overfitting (low training error, high testing error for large k).
# m_values = [0,0,0,0,0]

er_train_k = []
er_test_k = []
for k in k_values: 
    model = MLPClassifier(hidden_layer_sizes=(k,k,k,k,k) ,max_iter=2000) # create new MLPClassifier model with 5 layers, each consisting of k neurons

    model.fit(sample_train, label_train) # train a MLP classification model 

    # evaluate training error 
    label_train_pred = model.predict(sample_train) 
    er_train = 1 - accuracy_score(label_train, label_train_pred)

    # evaluate testing error 
    label_test_pred = model.predict(sample_test) # predict unseen labels from unseen test data
    er_test = 1 - accuracy_score(label_test, label_test_pred)

    er_train_k.append(er_train)
    er_test_k.append(er_test)
   
plt.figure()
plt.plot(k_values,er_train_k, label='Training Error', marker="o")
plt.plot(k_values,er_test_k, label='Testing Error', marker="o")
plt.xlabel('k value') # need to change it to "m" value for figure 2
plt.ylabel('Classification Error')
plt.legend()
plt.show()


