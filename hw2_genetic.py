#Alan Vo 
#OU Fall 2025
#AI - Homework 2 (genetic algorithm)

#chromosome = collection of genes (individual)
#populations = collections of individuals

import math #for Euler's number 
import pandas as pd #for csv preprocessing 
import numpy as np #for selection of parents based on probability
import random #for mutation and simulating probability
import matplotlib.pyplot as plt #for plotting


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
#proportionate fitness selection: probability(selecting individual i) =  fitness of individual i/sum of fitness of all members of population
def normalization(fitness_values):
   probabilities = [] #stores probabilities for parent selection proportional to each fitness value in corresponding index
   fitness_sum = sum(fitness_values) #sum of fitness values for all members of population
   #for each fitness value, convert to probability and add to above list
   for value in fitness_values:  
      probability_selection = value / fitness_sum
      probabilities.append(probability_selection)
   return probabilities #return list

#returns two parents that were selected based on probabilities proportional to their fitness values 
def select_parents(population, probabilities): 
   population_indices = [i for i in range(len(population))] #indices representing each individual (w) in population, because np.random.choices needs a to be 1-D array
   parent_indices = np.random.choice(a=population_indices, size=2, p=probabilities) #returns list containing two selected parent indexes based on given probabilities
   return population[parent_indices[0]], population[parent_indices[1]]#return actual value of w for each parent index
 
def reproduce(parent_1, parent_2):
   n = len (parent_1) #number of genes in each w (e.g. w = [1,1,1,1,1,1] has 6 genes)
   crossover_point = 3   #crossover point is the middle of w (first three elements of one w is recombined with the last elements of another w')
   #specify a range of indexes, which returns a new list with those specified items
   parent_1_contribution = parent_1[0:crossover_point]#get first three elements of parent 1 (indices 0-2, 3 NOT included)
   parent_2_contribution = parent_2[crossover_point: n] #get last three elements of parent 2  (indices 3-5, 6 NOT included)
   child = parent_1_contribution + parent_2_contribution #perform crossover operation
   return child

#each location in each string is subject to random mutation with a small independent probability
def mutate(child):
   mutated_child = child.copy() #will be returned 
   mutation_rate = 0.05
   #simulate chance of mutation for each bit by generating a random number between 0 and 1
   for i in range(len(child)):
      if random.random() < mutation_rate: 
         mutated_child[i] *= -1 #flip value at index
   return mutated_child

#function calculates fitness values of population, returns best individual, their er(w), and parent selection probabilities
#also updates 
def evaluate(population, dataframe, best_w_errors):
   fitness_values = [fitness_function(w, dataframe) for w in population] #list of corresponding fitness values for each individual in population (using list comprehension)
   probabilities = normalization(fitness_values) #convert fitness values to probabilites using normalization (for parent selection)
   best_w_index = fitness_values.index(max(fitness_values)) #get index of best individual in population (highest fitness value) 
   best_w = population[best_w_index]#use index to access best w in population with smallest er(w) that will be copied into the next generation (elitism)
   smallest_error = er(best_w, dataframe) #get smallest error during this generation from best w 
   best_w_errors.append(smallest_error) #update list containing best individual's er(w) for each round of generation
   return best_w, smallest_error, probabilities
   
#function creates random initial population of w's of a given size
def generate_population(size):
   available_numbers = [1,-1] #possible genes to choose from for each individual w
   population = []

   #repeat for each individual in population
   for i in range(size):
      w = [] 
      #populate each w with 6 genes
      for j in range(6):
         w.append(random.choice(available_numbers))
      population.append(w) #add individual to population
   return population
         


#returns the best individual in the population, according to fitness
def genetic_algorithm(dataframe):
   population = generate_population(3) #randomly generate a population with specified size 
   best_w_errors = [] #contains smallest er(w) from best individual  of each round of generation (for plotting) 
   best_w, smallest_error, probabilities = evaluate(population, dataframe, best_w_errors) #evaluate the initial population
   goal = 1.2 #based on best error found from hill climbing local search 
   max_number_generations = 200 #for looping until enough time has elapsed

   #loop forever until we find a goal (some individual is fit enough) or enough time has passed
   while smallest_error > goal and max_number_generations > 0: 
      max_number_generations -= 1 
      new_generation = [] #stores children formed from crossover/mutation. 
      new_generation.append(best_w)#elitism (copy best individual from previous round of generation into the next generation)
      #number offspring in new generation = size of current population
      #generate remaining offspring for new generation
      for i in range(1, len(population)):
         parent_1, parent_2 = select_parents(population, probabilities) #select parents
         child = reproduce(parent_1, parent_2) #crossover to produce new child
         mutated_child = mutate(child) #mutate child
         new_generation.append(mutated_child)#add child to new population
      population = new_generation #update new generation of children to be current population
      best_w, smallest_error, probabilities = evaluate(population, dataframe, best_w_errors) #revaluate population
   return best_w, smallest_error, best_w_errors



#MAIN FUNCTION
dataframe = pd.read_csv('CreditCard.csv') #read csv file and store it as a dataframe
dataframe.replace(to_replace={'M': 1, 'F': 0, 'Y': 1, 'N': 0}, inplace=True) #encode 'M','Y' to 1, and 'F','N' to 0, (inplace=True modifies original dataframe)
best_w, smallest_error, y_values = genetic_algorithm(dataframe) 

#print optimal w and er(w)
print("Optimal w = ", best_w)
print("Optimal er(w) = ", smallest_error)

#plot results 
plt.title('Genetic Algorithm')
plt.plot(y_values, marker='o') #matplotlib automatically generates x values 
plt.ylabel('er(w)')
plt.xlabel('Round of generation')
plt.show()





