#
# Template for Task 6: Random Forest Classification 
#
import numpy as np
import matplotlib.pyplot as plt

# --- Your Task --- #
# import libraries as needed 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score #used to compute classification error 
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
# pick five values of m by yourself 
m_values = [1,50,100,150,500]
# --- end of task --- #

er_test = []
for m in m_values: 
    # --- Your Task --- #
    # implement the random forest classification method 
    # you can directly call "RandomForestClassifier" from the scikit learn library
    model = RandomForestClassifier(n_estimators=m) #create new RandomForestClassifier model (n_estimators hyperparameter corresponds to m or #trees)

    model.fit(sample_train, label_train) #train the model on training data 
  
    # store classification error on testing data here 
    label_test_pred = model.predict(sample_test) #make a prediction on label_test, using unseen sample_test
    er = 1 - accuracy_score(label_test, label_test_pred)
    er_test.append(er)
# --- end of task --- #
    
plt.figure()    
plt.plot(m_values, er_test)
plt.xlabel('m')
plt.ylabel('Classification Error')
plt.show()


