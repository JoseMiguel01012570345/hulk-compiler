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
        return [ ( "name" , token_list[0].Text ) , ( 'anoted_type' , None ) ]
    else:
        
        literal = ( "literal" , True )
        
        if token_list[0].Text == "e":
            return [ ("id","literal") , ("value", math.e  ) , ("node_type" ,"type_Number")  , literal]
        
        if token_list[0].Text == "PI":
            return [ ("id","literal") , ("value", math.pi  ) , ("node_type" ,"type_Number") , literal ]
        
        return [ ("id","literal") , ("value", token_list[0].Text  ) , ("node_type" ,f'type_{token_list[0].Type.name}' ) , literal ]
        
def brackets(token_list):
    return [("replacement",token_list[1])]

def replacement(token_list,index=0):
    return [( "replacement" , token_list[index])]

def let(token_list):
    return [ ( "name",token_list[1].name ) , ('anoted_type' , token_list[1].anoted_type) ]

def assigment(token_list):    
    return [ ( "left_node" , token_list[0] ) , ("right_node", token_list[-1] ) ] 

def block(token_list):
    
    expressions = []
    for exp in token_list:
        if exp.__dict__.__contains__('id'):
            if exp.__dict__.__contains__('expressions'):
                expressions.extend(exp.expressions)
                continue
            expressions.append(exp)
    
    return [ ( "expressions" , expressions  )  ]    
        
def def_function(token_list):
    
    name = None
    args = None
    body = ( 'body' , None )
    if token_list[-1].__dict__.__contains__("id"):
        body =     body = ("body" , token_list[-1])
        
    node_type = ('node_type' , 'type_Object')
    
    for index,items in enumerate(token_list):
        
        if not items.__dict__.__contains__('id'):
            continue
        
        if items.id == 'var' and index > 2 and token_list[ index - 2].__dict__.__contains__("id") and token_list[ index - 2].id == 'args':
            node_type = ( "node_type" , items.name )
        elif items.id == "var":
            name= ("name" , items.name) 
        elif items.id == "args":
            args =  ("args" , items)
        
    return [ name , args, node_type , body ]
    
def type(token_list):
    
    if len(token_list) == 3:
        return [("name",token_list[1].name ) , ( "body", token_list[-1] )]
    
    if len(token_list) == 4:
        return [("name",token_list[1].name) , ( "constructor", token_list[2] ) ,( "body", token_list[-1] )]
        
    if len(token_list) == 5:
        return [("name",token_list[1].name) , ( "parent_name", token_list[3].name ) ,( "body", token_list[-1] )]
    
    token_list[5].parent_constructor = True
    return [("name",token_list[1].name) , ( "constructor", token_list[2] ) ,( "parent_name", token_list[4].name ) , ("base" , token_list[5]), ("body",token_list[-1]) ]

def protocol(token_list):
    
    if len(token_list) == 3:
        return [ ( "name" , token_list[1].name ) , ( "body", token_list[-1] ) ]
    
    return [ ( "name" , token_list[1].name ) , ("parent_name",token_list[3].name ) , ( "body", token_list[-1] ) ]

def in_(token_list):
    counter.auto_call_count += 1
    
    args = None
    for index,item in enumerate(token_list):
        if item.__dict__.__contains__('Text') and item.Text == 'in':
            parse_args = token_list[:index]
            
            if len(parse_args) == 2:
                parse_args[-1].expressions.append(parse_args[0])
                args = parse_args[-1]
            elif len(token_list) == 1:
                args = parse_args
            break
    
    return [ ("name" , f"anonymous{counter.auto_call_count}") , ( "args" ,args ) , ( "body" , token_list[2] ) ]

def structure(token_list):
    
    if token_list[0].id == "args":
        
        token_list[0].expressions.append(token_list[-1])
        
        return [ ("expressions", token_list[0].expressions ) ]
    
    return [ ("expressions", [ token_list[0] , token_list[2] ] ) ]

def params(token_list):

    if len(token_list) == 3:
        if token_list[1].__dict__.__contains__('expressions'):
            return [( "expressions" , token_list[1].expressions)]
        return [( "expressions" , [token_list[1]])]
    else:
        return [("expressions",[])]

def function_call(token_list):
    return [( "name" , token_list[0].name ) , ( "args",token_list[1] )]
    
def for_while(token_list):
    return [ ( "condition" , token_list[2]) , ("body", token_list[-1]) ]

def if_elif(token_list):
    return [ ("condition" , token_list[2]) , ("body",token_list[-1]) ]

def else_(token_list):
    return [("body",token_list[-1]) ]

def conditional(token_list):
    return [ ( "expressions" , token_list ) ]

def unary_opt(token_list):

    if hasattr(token_list[0],"id"):
        return [ ( "node" , token_list[0] ) ]
    else:
        return [ ( "node" , token_list[1] ) ]

def anoted_type( token_list ):
    token_list[0].node_type = token_list[-1].name
    return [ ( 'anoted_type' , token_list[-1].name ) , ( 'name' , token_list[0].name ) ]

def vector_gen( token_list ):
    return [ ( 'generator' , token_list[1] ) , ( 'variable' , token_list[3] ) , ( 'iterator' , token_list[-2] ) ]

class counter:
    auto_call_count = 0
