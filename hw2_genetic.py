#Alan Vo 
#OU Fall 2025
#AI - Homework 2 (genetic algorithm)

import math #for Euler's number 
import pandas as pd 

#evolutionary search generates w' with proper probability
#chromosome = collection of genes (individuals)
#populations = collections of individuals




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

#fitness function (higher fitness value corresponds to w with smaller er(w))
def fitness_function(w, dataframe): 
   return math.e ** (-1 * er(w, dataframe)) 

#function for generating probabilities of individuals/chromosomes using normalization
#proportionate fitness selection (roulette wheel): p(selecting individual i) =  fitness of individual i/sum of fitness of all members of population
def normalization(fitness_values):
   probabilities = [] #stores probabilities for parent selection proportional to each fitness value
   #for each fitness value, convert to probability and add to above list
   for value in fitness_values:  
      probability_selection = value / sum(fitness_values)
      probabilities.append(probability_selection)
   return probabilities #return list




#returns the best individual in the population, according to fitness
def genetic_algorithm(population, dataframe):
   #loop forever until we find a goal or run out of time
   fitness_values = [fitness_function(w, dataframe) for w in population] #list of corresponding fitness values for each individual in population (using list comprehension)
   probabilities = normalization(fitness_values) #convert fitness values to probabilites using normalization (for parent selection)
   new_population = [] #stores children formed from crossover and mutation
   


   #selection of parents based on probabilities proportional to their fitness values 
   #^do this twice and get individuals to mutate

   



#MAIN FUNCTION
dataframe = pd.read_csv('CreditCard.csv') #read csv file and store it as a dataframe
dataframe.replace(to_replace={'M': 1, 'F': 0, 'Y': 1, 'N': 0}, inplace=True) #encode 'M','Y' to 1, and 'F','N' to 0, (inplace=True modifies original dataframe)
dataframe.dropna(inplace=True)#remove line 142 in csv file that is missing gender attribute

initial_population = [[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[1,-1,1,-1,1,-1]] #create initial population (each w is a chromosome)
genetic_algorithm(initial_population, dataframe) #pass fitness function as argument

#print optimal w and optimal er(w)
#plot results 






