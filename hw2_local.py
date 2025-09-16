#Alan Vo 
#OU Fall 2025 
#AI - Homework 2 (hill climbing local search)

import pandas as pd 

dataframe = pd.read_csv('CreditCard.csv') #read csv file and store it as a dataframe
dataframe.replace(to_replace={'M': 1, 'F': 0, 'Y': 1, 'N': 0}, inplace=True) #encode 'M','Y' to 1, and 'F','N' to 0, (inplace=True modifies original dataframe)




#function approximating linear relation between attributes of applicants and their application result
def f(x_attributes, w):
   #have to get values of all attributes in table (gender...email)
   return (w[0]) + (w[1]) + (w[2]) + (w[3]) + (w[4]) + (w[5]) 
    

#function calculating approximation error 
def er(w):
   #loop through each row of the dataset (each person) and
   for i in range(len(dataframe)):
      pass




initial_w = [-1,-1,-1,-1,-1,-1] #start with a random solution for w 

 #get approximation error for current/initial state 


# while True:

#generate six neighbors and compute each of their approximation errors

#if no neighbor has a lower approximation error, return current

#set current state to be neighbor with lowest e(r) 

