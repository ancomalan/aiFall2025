#Alan Vo 
#OU Fall 2025 
#AI - Homework 2 (hill climbing local search)

import pandas as pd 
import matplotlib.pyplot as plt

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

#finds w with smallest approximation error 
def find_best(errors):
   smallest_error = errors[0]#initially set first element as smallest 
   best_index = 0 #index in neighbor_results array corresponding to smallest approximation error value (initially set to 0)
   for i in range (1, len(errors)):
      #if current error is smaller, update to smallest
      if errors[i] < smallest_error: 
         smallest_error = errors[i]
         best_index = i 
   return smallest_error, best_index

#function for hill climbing local search 
def hill_climbing_local_search(initial_w, dataframe):
   current_w = initial_w 
   current_error = er(current_w, dataframe)#get approximation error for current/initial state 
   y_values = [current_error]#y axis for plot containing smallest er(w) after every round of search (has current error initially)
   
   while True:
      neighbors = generate_neighbors(current_w) #generate six adjacent neighbors
      neighbor_errors = [er(w,dataframe) for w in neighbors] #for each neighbor, compute approximation errors and store them all in this list using list comprehension
      smallest_error, index = find_best(neighbor_errors) #get smallest error and index of corresponding neighbor 
   
      #if no neighbor has a lower approximation error, algorithm ends
      if smallest_error >= current_error: 
         return current_error, current_w, y_values
      else:
         current_error = smallest_error    #set current state to smallest_error 
         current_w = neighbors[index]    #otherwise, set smallest w as current w 
         y_values.append(current_error)#append to list storing y values for later display
  


dataframe = pd.read_csv('CreditCard.csv') #read csv file and store it as a dataframe
dataframe.replace(to_replace={'M': 1, 'F': 0, 'Y': 1, 'N': 0}, inplace=True) #encode 'M','Y' to 1, and 'F','N' to 0, (inplace=True modifies original dataframe)

w = [-1,-1,-1,-1,-1,-1] #start with a random, intial state for w 
optimal_error, optimal_w, y_values = hill_climbing_local_search(w, dataframe)#call hill climbing local search function using initial w

#print optimal w and er(w)
print("Optimal w = ", optimal_w)
print("Optimal er(w) = ", optimal_error)

#plot results 
plt.title('Hill Climbing Local Search')
plt.plot(y_values, marker='o') #matplotlib automatically generates x values 
plt.ylabel('er(w)')
plt.xlabel('Round of search')
plt.show()
      




