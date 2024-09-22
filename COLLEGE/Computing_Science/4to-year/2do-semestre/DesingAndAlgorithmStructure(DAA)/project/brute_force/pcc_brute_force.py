import random 
import os
import copy

os.system('cls')
def enconde_input( matrix_lenght , min_weight , max_weight ):
    

    '''

    adyacenty matrix

    '''
    

    if min_weight < 0 or max_weight < 0:

        raise Exception( '\033[1;31m weights most remind non-negative integer \033[0m')


    matrix_row = {}

    for i in range(matrix_lenght):

        matrix_column = []

        for j in range(matrix_lenght):
            
            if i == j:
                weight = 0
            else:
                weight = random.randint( min_weight , max_weight )

            matrix_column.append(weight)
        

        matrix_row[i] = matrix_column

    print('graph:')
    for i in matrix_row:
        print(f'{i}: {matrix_row[i]}')


    return matrix_row


def brute_force( matrix:list ):
 

    ''' find min cost path between any two nodes using a DFS '''


    min_cost_min_streets = {}

    import time
    
    for source in range( len(matrix) ):
        
        list_min_streets = []

        for target in range( len(matrix) ):
            
            _  , min_streets_num , count = DFS(matrix, source, target , visited_nodes=[] )
            
            list_min_streets.append(min_streets_num)


        min_cost_min_streets[source] = list_min_streets

    print('min streets path: ')
    for i in min_cost_min_streets:
        print(f'{i}: {min_cost_min_streets[i]}')

    return min_cost_min_streets


def DFS( matrix , source , target , cost=0 , streets=0 , visited_nodes = [] , count=0 ):


    if target == source:

        if len(matrix) - 1 <= len(visited_nodes):
            count += 1

        return cost , streets , count

    visited_nodes.append( source )

    source_weights_connections = matrix[ source ] 

    min_cost = 1e305

    min_streets = 1e305

    for i in range(len(matrix)):
        

        if i in visited_nodes: continue
        
        i_weight = source_weights_connections[i]

        new_vistited_nodes = [ element for element in visited_nodes ]

        new_cost , new_streets , count = DFS(
                                    matrix=matrix,
                                    source=i ,
                                    target=target ,
                                    cost= cost + i_weight , 
                                    streets= streets + 1 , 
                                    visited_nodes=new_vistited_nodes , 
                                    count=count 
                                )


        if new_cost <= min_cost:

            if new_cost == min_cost:
                if new_streets < min_streets: 
                    min_streets = new_streets
            else:
                min_streets = new_streets
            
            min_cost = new_cost

    return min_cost , min_streets , count


num_test_per_param = 5

# _________________________SET THE NUMBER OF TEST CASES_________
test_cases = [] # { 'input': adyacency matrix , 'output': length streets per every two nodes }
num_test_cases = 1000

# NOTE: THIS BRUTE FORCE IS O(((N-1)!)^2)  , this is , all of the paths between every two vertex
# _____________________________________________________________

matrix_lenght = 2

leave = False
while not leave:

    matrix_lenght += 1

    for max_weight in range(1 , random.randint(0, 10) + 2 ):

        for min_weight in range( 0 , random.randint(0, max_weight - 1 ) + 1 ):
        
            test = num_test_per_param
            while test != 0: # generate random cases with the same params
                os.system('cls')
                graph = enconde_input(matrix_lenght=matrix_lenght, min_weight=min_weight, max_weight=max_weight)
                min_streets =  brute_force( graph )
                test -= 1
                my_graph = copy.deepcopy(graph)
                test_cases.append({'input': my_graph , 'output': min_streets } )

                if len(test_cases) == num_test_cases:
                    leave = True
                    break
            
            if leave: break
        
        if leave: break
        
    
    

