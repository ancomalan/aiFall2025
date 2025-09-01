#Alan Vo
#OU Fall 2025 
#AI - Homework 1


# Problem: Implement the Breadth-First Search (BFS), Depth-First Search (DFS) 
# and Greedy Best-First Search (GBFS) algorithms on the graph from Figure 1 in hw1.pdf.


# Instructions:
# 1. Represent the graph from Figure 1 in any format (e.g. adjacency matrix, adjacency list).
# 2. Each function should take in the starting node as a string. Assume the search is being performed on
#    the graph from Figure 1.
#    It should return a list of all node labels (strings) that were expanded in the order they where expanded.
#    If there is a tie for which node is expanded next, expand the one that comes first in the alphabet.
# 3. You should only modify the graph representation and the function body below where indicated.
# 4. Do not modify the function signature or provided test cases. You may add helper functions. 
# 5. Upload the completed homework to Gradescope, it must be named 'hw1.py'.

# Examples:
#     The test cases below call each search function on node 'S' and node 'A'
# -----------------------------
   
   
#represent Figure 1 graph as an adjacency matrix called G, using 2D list
#elements accessed by [row][column]
#nodes not connected are represented by -1 
#nodes connecting to themselves represented by 0
G = [
        # A  B  C  D  E  F  G  H  I  J  K  L  M  N  P  Q  S
        [ 0, 4,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1 ], #A
        [ 4, 0, 2,-1,-1, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1 ], #B
        [-1, 2, 0,-1,-1,-1,-1, 4,-1,-1,-1,-1,-1,-1,-1,-1, 3 ], #C
        [-1,-1,-1, 0,-1,-1,-1,-1,-1,-1,-1, 8,-1,-1,-1,-1, 2 ], #D
        [ 1,-1,-1,-1, 0, 3,-1,-1, 6,-1,-1,-1,-1,-1,-1,-1,-1 ], #E
        [-1, 2,-1,-1, 3, 0,-1,-1,-1, 6, 4,-1,-1,-1,-1,-1,-1 ], #F
        [-1,-1,-1,-1,-1,-1, 0,-1,-1,-1,-1,-1, 4, 4,-1, 10,-1], #G
        [-1,-1, 4,-1,-1,-1,-1, 0,-1,-1, 3, 7,-1,-1,-1,-1,-1 ], #H
        [-1,-1,-1,-1, 6,-1,-1,-1, 0, 1,-1,-1, 5,-1,-1,-1,-1 ], #I
        [-1,-1,-1,-1,-1, 6,-1,-1, 1, 0, 3,-1,-1, 3,-1,-1,-1 ], #J
        [-1,-1,-1,-1,-1, 4,-1, 3,-1, 3, 0, 9,-1,-1, 3,-1,-1 ], #K
        [-1,-1,-1, 8,-1,-1,-1, 7,-1,-1, 9, 0,-1,-1,-1, 10,-1], #L
        [-1,-1,-1,-1,-1,-1, 4,-1, 5,-1,-1,-1, 0,-1,-1,-1,-1 ], #M
        [-1,-1,-1,-1,-1,-1, 4,-1,-1, 3,-1,-1,-1, 0, 2,-1,-1 ], #N
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 3,-1,-1, 2, 0,-1,-1 ], #P
        [-1,-1,-1,-1,-1,-1, 10,-1,-1,-1,-1,10,-1,-1,-1,0,-1 ], #Q
        [-1,-1, 3, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0 ]  #S
    ]

#dictionaries for converting between node labels (strings) and integers
stringToInt = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'P':14, 'Q':15, 'S':16
}
intToString = {
    0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14: 'P', 15: 'Q', 16:'S'
}

#helper function that returns node label list from given node index list
def convert_indices_to_string(indices_list):
    updated_list = []
    #loop through all elements in list and update them based on the intToString dictionary
    for index in indices_list: 
        updated_list.append(intToString[index])
    return updated_list
    

def BFS(start: str) -> list:
    start_node = stringToInt[start] #convert starting node to int (to index into adjacency matrix)
    goal_node = 6 #int representation of node 'G'
    queue = [] #implement queue using list
    visited = [] #contains order in which nodes have been reached/discovered 
    expanded = [] #contains order in which nodes were expanded/explored

    queue.append(start_node) #add start node to queue
    visited.append(start_node)#add to visited list

    while (len(queue) != 0):
        node = queue.pop(0) #pop current node from queue
        expanded.append(node) #node is about to be expanded below
        
        num_elements_in_row = len(G[node]) #gets number of elements in this node's row in adjacency matrix
        #i represents index of other nodes
        #add adjacent nodes that have not been visited 
        for i in range(num_elements_in_row):
            if (G[node][i] > 0 and i not in visited):
                #check if 'G' is discovered during expansion
                if (i == goal_node):
                    expanded.append(i)
                    return convert_indices_to_string(expanded) #early termination after finding goal
                else:
                    queue.append(i)
                    visited.append(i)
                    
    return convert_indices_to_string(expanded)
    


def DFS(start: str) -> list:
    # START: Your code here
    return []
    # END: Your code here


def GBFS(start: str) -> list:
    # START: Your code here
    return []
    # END: Your code here



# test cases - DO NOT MODIFY THESE
def run_tests():
    # Test case 1: BFS starting from node 'A'
    assert BFS('A') == ['A', 'B', 'E', 'C', 'F', 'I', 'H', 'S', 'J', 'K', 'M', 'G'], "Test case 1 failed"
    
    # Test case 2: BFS starting from node 'S'
    assert BFS('S') == ['S', 'C', 'D', 'B', 'H', 'L', 'A', 'F', 'K', 'Q', 'G'], "Test case 2 failed"

    # Test case 3: DFS starting from node 'A'
    assert DFS('A') == ['A', 'B', 'C', 'H', 'K', 'F', 'E', 'I', 'J', 'N', 'G'], "Test case 3 failed"
    
    # Test case 4: DFS starting from node 'S'
    assert DFS('S') == ['S', 'C', 'B', 'A', 'E', 'F', 'J', 'I', 'M', 'G'], "Test case 4 failed"

    # Test case 5: GBFS starting from node 'A'
    assert GBFS('A') == ['A', 'B', 'F', 'J', 'N', 'G'], "Test case 5 failed"
    
    # Test case 6: GBFS starting from node 'S'
    assert GBFS('S') == ['S', 'C', 'B', 'F', 'J', 'N', 'G'], "Test case 6 failed"


    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
