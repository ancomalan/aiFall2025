"""
-policy is function mapping state s to its action 
-set of actions forms one policy
-slide 10: equation gives expected total reward starting from one specific state s and following policy pi (tells you how valuable that state really is)
-optimal policy maximizes expected utility at every state
first visit Monte Carlo is used to estimate utility of each nonterminal state based on policy 
"""

import numpy as np # for random choice with probabilities

# represent grid world policy: dictionary mapping a non-terminal state (coordinate) to an action based on figure 1
policy = {
    (1,1): 'R', 
    (1,2): 'U', 
    (1,3): 'L', 
    (2,1): 'U', 
    (2,3): 'D',
    (3,1): 'L',
    (3,2): 'L',
    (3,3): 'R',
    (4,1): 'L'
}

rock = (2,2) # account for rock at (2,2)
terminal_states = {(4,2): -1, (4,3): 1} # account for terminal states and their rewards 


# dictionary representing stochastic moves: for move (key), values are all possible probabilities for moving in certain direction based on figure 1
# i.e., if we move up: 60% move up, 20% move left, 10% move right, and 10% move down
# represent values as a list of tuples (move, probability)
stochastic_moves = {
    'U': [('U', 0.6), ('L', 0.2), ('R', 0.1), ('D', 0.1)],
    'D': [('D', 0.6), ('L', 0.1), ('R', 0.2), ('U', 0.1)],
    'L': [('L', 0.6), ('D', 0.2), ('U', 0.1), ('R', 0.1)],
    'R': [('R', 0.6), ('U', 0.2), ('D', 0.1), ('L', 0.1)]
}

# function checks for walls (state is outside grid boundaries)
def hits_wall(state):
    x, y = state # unpack x, y from tuple 
    # for coordinate (x,y), if x value goes below 1 or above 4, then hit left and right walls
    # for coordinate (x,y), if y value goes below 1 or above 3, then hit top and bottom walls 
    if x < 1 or x > 4 or y < 1 or y > 3:
        return True 
    return False # otherwise return False
    
 

#function returns actual move accounting for randomness
def get_actual_move(intended_move):
    moves_and_probs = stochastic_moves[intended_move] # get probabilities of moving in certain directions based on intended move (list of tuples)
    moves = [] # store all possible moves inside this list (L,R,U,D)
    probs = [] # stores probabilities for each possible move at the same index in possible_moves
    for tuple in moves_and_probs: 
        move, prob = tuple # extract move and associated probability 
        moves.append(move)
        probs.append(prob)

    # select random move with given probability using np.random.choice 
    actual_move = np.random.choice(a=moves, size=1, p=probs)[0]
    return actual_move 


# function returns next state afer applying a stochastic move 
def move (state):
    intended_move = policy[state] # use policy to get intended move for current state 
    actual_move = get_actual_move(intended_move) # get actual move 
    x, y = state # extract current x, y coordinates 

    #get new coordinates if we performed move 
    if actual_move == 'U': 
        x_new = x 
        y_new = y + 1 # add 1 to y  
    elif actual_move == 'D':
        x_new = x
        y_new = y - 1 # subtract 1 from y 
    elif actual_move == 'L':
        x_new = x - 1 # subtract 1 from x 
        y_new = y
    else: 
        x_new = x + 1 # move right (increase x by 1)
        y_new = y
    new_state = (x_new, y_new) # store new coordinates into tuple

    #check to see if they hit the wall or rock, and if they do return the old coordinates (stay in current state!)
    if (hits_wall(new_state) or new_state == rock):
        return state 
    else:
        return new_state #return new state 

# function estimates utility of a non-terminal state based on policy and stochastic move in figure 1 (performs 10 experiments for certain state)
def first_visit_MC(state, num_trials):
    experiment_results = [] # store results of all 10000 episodes/experiments/trials
    for _ in range (num_trials):
        current_state = state # stores original state
        gamma = 0.8 # discount rate (determines how much future rewards are worth compared to immediate rewards)
        reward = -0.04 # reward at each non-terminal state
        expected_utility = 0 # running total of cumulative discounted rewards collected by following policy from current state: U(state)
        iteration = 0 # used to update discount rate after every iteration
        
        #keep going until we reach a terminal state (check for membership in python dictionary by looking at keys)
        while current_state not in terminal_states:
            expected_utility += (gamma ** iteration) * reward # update expected utility when entering this state
            current_state = move(current_state) # move to next state 
            iteration += 1 # increment iteration so we can update gamma
        expected_utility += (gamma ** iteration) * terminal_states[current_state] # finally, account for terminal state reward 
        experiment_results.append(expected_utility) # add result for this experiment 
    
    # after running 10 experiments, compute average of results, returning final utility estimate for current state
    return np.mean(experiment_results)



# perform 10 experiments for each non-terminal state, and print results!
# loop through each state in policy dictionary (all keys)
for state in policy.keys():
    print("Utility estimate for state ", state, ": ", first_visit_MC(state, 10000))