from ..lexer import EnumsTokensDefinition
TokenType,Type =   EnumsTokensDefinition.TokenType , EnumsTokensDefinition.Type
import math
'''

NOTE: every builder must return a list in where it specify the properties of the node

'''

def binary_opt(token_list):
    return [ ( "left_node" , token_list[0] ) , ( "right_node" , token_list[2] ) ]

def var(token_list):
    
    if token_list[0].Type.name == "Variable":
        return [ ( "name" , token_list[0].Text ) ]
    else:
        
        literal = ( "literal" , True )
        
        if token_list[0].Text == "e":
            return [ ("id","literal") , ("value", math.e  ) , ("type_" ,"Number")  , literal]
        
        if token_list[0].Text == "PI":
            return [ ("id","literal") , ("value", math.pi  ) , ("type_" ,"Number") , literal ]
        
        return [ ("id","literal") , ("value", token_list[0].Text  ) , ("type_" ,token_list[0].Type.name ) , literal ]
        
def brackets(token_list):
    return [("replacement",token_list[1])]

def replacement(token_list,index=0):
    return [( "replacement" , token_list[index])]

def let(token_list):
    return [ ( "name",token_list[1] ) ]

def assigment(token_list):    
    return [ ( "left_node" , token_list[0] ) , ("right_node", token_list[-1] ) ] 

def block(token_list):
    
    if len(token_list) == 1:
        return [ ( "expressions" , [ token_list[0] ] ) ]
        
    if not token_list[0].__dict__.__contains__("id"):
        
        if not token_list[1].__dict__.__contains__("id"):
            return [ ( "expressions" , [ ] ) ]
             
        return [ ( "expressions" , [ token_list[1] ] ) ]
    
    elif not  token_list[-1].__dict__.__contains__("id")  :     
        return [("expressions", token_list[0].expressions )]
    
    else:
        token_list[0].expressions.append(token_list[-1])
        return [ ( "expressions" , token_list[0].expressions  )  ]    
        
def def_function(token_list):
    
    if not token_list[0].__dict__.__contains__("id"):
        return [ ("name" , token_list[1].name ) , ( "args" , token_list[-2] ) , ( "body", token_list[-1] ) ]
    
    if token_list[0].__dict__.__contains__("id"):
        return [ ("name" , token_list[0] ) , ( "args" , token_list[-3] ) , ( "body", token_list[-1] ) ]

def type(token_list):
    
    if len(token_list) == 3:
        return [("name",token_list[1].name ) , ( "body", token_list[-1] )]
    
    if len(token_list) == 4:
        return [("name",token_list[1].name) , ( "constructor", token_list[2] ) ,( "body", token_list[-1] )]
        
    if len(token_list) == 5:
        return [("name",token_list[1].name) , ( "parent_name", token_list[3].name ) ,( "body", token_list[-1] )]
    
    return [("name",token_list[1].name) , ( "constructor", token_list[2] ) ,( "parent_name", token_list[4].name ) , ("base" , token_list[5]), ("body",token_list[-1]) ]

def protocol(token_list):
    
    if len(token_list) == 3:
        return [ ( "name" , token_list[1].name ) , ( "body", token_list[-1] ) ]
    
    return [ ( "name" , token_list[1].name ) , ("parent_name",token_list[3].name ) , ( "body", token_list[-1] ) ]

def in_(token_list):
    return [ ( "expressions" , token_list[0] ) , ( "body" , token_list[2] ) ]

def structure(token_list):
    
    if token_list[0].id == "structure":
        
        token_list[0].expressions.append(token_list[-1])
        
        return [ ("expressions", token_list[0].expressions ) ]
    
    return [ ("expressions", [ token_list[0] , token_list[2] ] ) ]

def params(token_list):

    if len(token_list) == 3:
        return [( "expressions" , token_list[1].expressions)]
    else:
        return [("expressions",[])]

def function_call(token_list):
    return [( "name" , token_list[0].name ) , ( "args",token_list[1] )]
    
def for_while(token_list):
    return [ ( "condition" , token_list[1]) , ("body", token_list[2]) ]

def if_elif(token_list):
    return [ ("condition" , token_list[1]) , ("body",token_list[-1]) ]

def else_(token_list):
    return [("body",token_list[-1]) ]

def conditional(token_list):
    return [ ( "expressions" , token_list ) ]

def unary_opt(token_list):

    if hasattr(token_list[0],"id"):
        return [ ( "node" , token_list[0] ) ]
    else:
        return [ ( "node" , token_list[1] ) ]

