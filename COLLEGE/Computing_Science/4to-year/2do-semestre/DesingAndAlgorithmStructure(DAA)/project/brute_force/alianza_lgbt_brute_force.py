import random
import os
import copy

os.system('cls')


def enconde_input(num_colors , num_fab , num_robot ):
    

    '''<F,R,C> 
    

    F-> fabricants

    R -> robots

    C -> colors 
    

    '''

    if num_robot < num_colors or num_robot < num_fab:

        raise Exception('\033[1;31m robots number most execed number of fabricants and number of colors \033[0m')


    robots_list = { 

        i: { 'fab':[] , 'color':0  } for i in range(num_robot) 

        }


    fabs = [  i for i in range(num_fab)]

    colors = [ i for i in range(num_colors)]

    for r in range(num_robot):
        
        common_fabs = random.randint( 1, num_fab - 1 ) # a robot can have more than a fabricant piece

        count = 0
        list_r_fabs = []
        while common_fabs != count: # give common_fabs fabricants to a robot 
        
            r_fab = random.randint( 0 , num_fab )

            while r_fab not in fabs: # give a random fabricant , making sure all fabricants are involved
                r_fab = random.randint( 0 ,num_fab )

            if r_fab in list_r_fabs: continue # repited fabricants for a robots is not allowed

            list_r_fabs.append(r_fab)
            fabs.remove(r_fab)

            if len(fabs) ==0: fabs = [  i for i in range(num_fab)] # restart count after all fabricant consumed
            
            count += 1
        

        r_color = random.randint( 0, num_colors )

        while r_color not in colors: # add a color

            r_color = random.randint( 0 , num_colors )
            

        colors.remove(r_color)

        if len(colors) ==0: colors = [ i for i in range(num_colors)]
        
        robots_list[r] = { 'fab': list_r_fabs , 'color': r_color }

    print('robot list: ')

    for element in robots_list:
        print(element , robots_list[element])

    return robots_list 


def build_graph_init_(robots_list:list):
    
    
    for robot in robots_list:
        robots_list[robot] = [ robots_list[robot] , [ 0 for _ in range(len(robots_list)) ] ]


    colors=[]
    for robot1 in  robots_list:
        
        if robots_list[robot1][0]['color'] not in colors: # discover num colors
            colors.append(robots_list[robot1][0]['color'])
            
        for robot2 in robots_list:
            if any( [ True for element in robots_list[robot2][0]['fab'] if element in robots_list[robot1][0]['fab'] ]):
                robots_list[robot1][1][robot2] = 1
                robots_list[robot2][1][robot1] = 1
                    
    return robots_list , len(colors)

def check( graph:list , num_colors ):
    

    if len(graph) != num_colors : return False


    colors = []

    for robot in graph:


        if graph[robot][0]['color'] in colors: # check all colors to be diferents

            return False


        colors.append( graph[robot][0]['color'] )


        count = 0

        for edge in graph[robot][1]: # check the graph is dense

            count += edge
        

        if count < num_colors:

            return False


    return True


def build_graph( graph , combination ):

    robots_graph = { }

    for element in combination:
        
        robots_graph[element] = copy.deepcopy(graph[element])  
        robots_graph[element][1] = [ element1 for index,element1 in enumerate(graph[element][1]) if index in combination ]

    return robots_graph

def solve_using_brute_force( robot_list ):
    
    graph , num_colors = build_graph_init_(robots_list=robot_list)
    result = brute_force(graph=graph , num_colors=num_colors , num_robot=len(graph) )
    
    return result

def brute_force( graph:list , num_colors , num_robot , combination= [] , robot=0):
    

    '''

     we will build an induced grapgh using all cobinations of robots taken num_colors by num_colors

    of vertexes and verfiy if there is a multi-color aliance '''


    if num_colors == len(combination):

        # print( combination )

        new_graph = build_graph(graph, combination)

        r = check(new_graph, num_colors)
        if r:
            
            print('__________________________________________________')
            for i in new_graph:
                print(i,new_graph[i])
            return True
        
        return False

    if robot == num_robot: return False 

    new_combination = [ element for element in combination ]

    new_combination.append( robot )


    result = brute_force(graph, num_colors, num_robot , combination=new_combination , robot= robot + 1)

    if result: 

        return True
    

    result = brute_force(graph, num_colors, num_robot , combination=combination , robot= robot + 1 )

    if result: 

        return True
    

    return False
    


num_robot= 3
num_test_per_param = 15

# _________________________SET THE NUMBER OF TEST CASES_________

test_cases = []
num_test_cases = 1000

''' NOTE: THIS BRUTE FORCE IS O(C(n,k)) where C(n,k) is all combination of elements taken k by k  
        
    ABOUT INPUT: The input is a graph of the following shape:

        robots_graph = { 

        i: [ { 'fab':[...] , 'color': ci  } ,  

        [ 0 for j in range(num_robot) ] ] for i in range(num_robot) 

        }
    
    Every robot has a list where the first element is a dictionary , where 'fab' is the list of fabricants and 'color' , his color , 
    the second element is a list of his repective edges , where robot1 is linked to robot2 if share fabricants , if so , edge is weighted as 1
    and 0 otherwise    

 _____________________________________________________________
'''


leave = False
while not leave:

    num_robot += 1

    for num_colors in range( 2 , num_robot - 1):

        for num_fab in range(2 , num_robot - 1):
        
            result = False
            test = num_test_per_param
            while not result and test != 0: # generate random cases with the same params
                os.system('cls')
                num_colors = num_robot
                robot_list =  enconde_input(num_colors=num_colors, num_fab=num_fab, num_robot=num_robot )
                result = solve_using_brute_force( robot_list=robot_list )
                
                test -= 1
                my_robot_list = copy.deepcopy( robot_list )
                test_cases.append({'input': my_robot_list , 'output': result } )

                if len(test_cases) == num_test_cases:
                    leave = True
                    break
            
            if leave: break
        
        if leave: break
    

def your_fast_alg( input ) -> bool:
   
    '''
    your solution should be here
    '''
    return True


count_falls = 0
for index,sample in enumerate(test_cases):
    solution = your_fast_alg( input=sample['input'] )
    if not solution ==  sample:
        print( f'\033[1;31m test case --> {index} mismatch output \033[0m' )
        count_falls += 1

print( f'\33[1;32M PERFECT SCORE: 100% \033[0m' if count_falls == 0 else f'\033[1;31M BAD SOLUTION :( {count_falls/len(test_cases)}% wrong aswers \033[0m' )