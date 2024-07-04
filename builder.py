from EnumsTokensDefinition import TokenType,Type
import production_class_representation as pcr

'''

NOTE: every builder must return a list in where it specify the properties of the node

'''

def plus(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]

def minus(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]
    
def multiplier(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]

def divition(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]

def var(token_list):
    
    if token_list[0].Type == TokenType.Variable:
        return [ ( "name" , token_list[0].Text ) , ("value", None ) ]
    else:
        return literal(token_list)
    
def brackets(token_list):
    return [("expression",token_list[1])]

def replacement(token_list):
    return [( "replacement" , token_list[0])]

def let(token_list):
    return [ ( "name",token_list[1].name ) , ( "value" , token_list[-1] ) ]

def literal(token_list):
    return [ ( "value" , token_list[0].Text) , ( "id" , "literal" ) ]

def re_asigment(token_list):    
    return [ ( "name" , token_list[0].name ) , ("value", token_list[-1] ) ] 

def block(token_list):
    
    if not  token_list[0].__dict__.__contains__("id")  :
        return [ ( "expressions" , [token_list[1]] ) ]
    else:
        token_list[0].expressions.append(token_list[-1])
        
        return [ ( "expressions" , token_list[0].expressions  )  ]
        
def def_function(token_list):
    return [ ( "args" , token_list[-2] ) , ( "body", token_list[-1] ) ]

def type(token_list):
    
    if len(token_list) == 3:
        return [("name",token_list[1].name ) , ( "body", token_list[-1] )]
    
    if len(token_list) == 4:
        return [("name",token_list[1].name) , ( "args", token_list[2] ) ,( "body", token_list[-1] )]
        
    if len(token_list) == 5:
        return [("name",token_list[1].name) , ( "inheritence_name", token_list[3].name ) ,( "body", token_list[-1] )]
    
    return [("name",token_list[1].name) , ( "args", token_list[3] ) ,( "inheritence_name", token_list[4].name ) , ("inheritence_args" , token_list[5]), ("body",token_list[-1]) ]

def protocol(token_list):
    
    if len(token_list) == 3:
        return [ ( "name" , token_list[1].name ) , ( "body", token_list[-1] ) ]
    
    return [ ( "name" , token_list[1].name ) , ("inheritence_name",token_list[3].name) , ( "body", token_list[-1] ) ]

def in_(token_list):
    return [ ( "args" , token_list[0] ) , ( "body" , token_list[2] ) ]

def structure(token_list):
    
    if token_list[0].id == "structure":
        
        token_list[0].expressions.append(token_list[-1])
        
        return [ ("expressions", token_list[0].expressions ) ]
    
    return [ ("expressions", [ token_list[0] , token_list[2] ] ) ]

def params(token_list):
    if len(token_list) == 3:
        return [( "replacement" , token_list[1])]
    else:
        return [("replacement",None)]

def function_call(token_list):
    return [( "name" , token_list[0].name ) , ( "args",token_list[1] )]
    
    