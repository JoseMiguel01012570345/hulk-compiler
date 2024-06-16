def plus(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]

def minus(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]
    
def multiplier(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]

def divition(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]
    
def var(token_list):
    return [ ( "name" , token_list[0] ) ]
    
def brackets(token_list):
    return [("expression",token_list[1])]

def replacement(token_list):
    return [( "replacement" , token_list[0])]

