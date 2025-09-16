#Alan Vo 
#OU Fall 2025 
#AI - Homework 2 (hill climbing local search)

import pandas as pd 

#function approximating linear relation between attributes of applicant x and their application result
def f(x_attributes, w):
   return (x_attributes[0] * w[0]) + (x_attributes[1] * w[1]) + (x_attributes[2] * w[2]) + (x_attributes[3]* w[3]) + (x_attributes[4]* w[4]) + (x_attributes[5]* w[5]) 
    
#function calculating approximation error 
def er(w, dataframe):
   summation = 0 #running total for (f(x) - y)^2 where x is applicant i and y is corresponding result
   #loop through each row of the dataset (each person)
   #iterrows returns a tuple containing row index and Series object containing values for that row
   for index, row in dataframe.iterrows():   
      y = row['CreditApprove']#get application result for applicant i
      attributes = [row['Gender'], row['CarOwner'], row['PropertyOwner'], row['#Children'], row['WorkPhone'], row['Email_ID']] #store attribute values for applicant i in list (Gender - Email_ID)
      summation += pow((f(attributes, w) - y), 2) #call linear relation approximation function above
   return (1 / len(dataframe)) * summation

#generates adjacent neighbors to current w (differ by exactly one element)      
def generate_neighbors(w):
   all_neighbors = [] #store all adjacent neighbors (2d array)
   #loop 6 times, each time flipping bit at index i
   for i in range (len(w)):
      neighbor = w.copy()#make a copy of current w
      neighbor[i] *= -1 #flip value at index in copy list
      all_neighbors.append(neighbor)#add to list of neighbors
   return (all_neighbors)   


dataframe = pd.read_csv('CreditCard.csv') #read csv file and store it as a dataframe
dataframe.replace(to_replace={'M': 1, 'F': 0, 'Y': 1, 'N': 0}, inplace=True) #encode 'M','Y' to 1, and 'F','N' to 0, (inplace=True modifies original dataframe)
dataframe.dropna(inplace=True)#remove line 142 in csv file that is missing gender attribute


#implement hill climbing local search
initial_w = [-1,-1,-1,-1,-1,-1] #start with a random solution for w 
current = er(initial_w, dataframe)#get approximation error for current/initial state 
print(generate_neighbors(initial_w))

# while True:

#generate six neighbors and compute each of their approximation errors

#if no neighbor has a lower approximation error, return current

#set current state to be neighbor with lowest e(r) 

