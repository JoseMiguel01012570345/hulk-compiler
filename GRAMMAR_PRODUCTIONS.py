import builder as B
import production_class_representation as pcr
import visitor as V

# function_caLL = [
#     [ "",[ [] , [] ] ]
# ]

# strings = [
    
#     [ "",[ [] , [] ] ]
# ]

# expression_block = [
    
#     [ "",[ [] , [] ] ]
    
# ]

# booleans = [
    
#     [ "",[ [] , [] ] ]
# ]

# IN = [
    
#     [ "",[ [] , [] ] ]
       
# ]

# For = [
    
#     [ "",[ [] , [] ] ]  
    
# ]

# conditional = [
    
#     [ "",[ [] , [] ] ]
    
# ]

# While = [
    
#     [ "",[ [] , [] ] ]
# ]

# function = [    
 
#     [ "",[ [] , [] ] ]
# ]

# types = [
    
#     [ "",[ [] , [] ] ]
# ]

# protocols = [

#     [ "",[ [] , [] ] ]
    
# ]

# vector = [
    
#     [ "",[ [] , [] ] ]
# ]

variable = [
    
    pcr.variable({  "derivation": ["A",["F", "=" , "E" ]] , "identifier": "var" , "definition_node?": False ,"builder": B.re_asigment , "visitor": V.var } ) ,
    
]

let = [

    # A -> let F = X
    pcr.let({  "derivation": ["A",["let","F", "=" , "E" ]] , "identifier": "let" , "definition_node?": True ,"builder": B.let , "visitor": V.let } ) ,
]

numbers = [
    
    # X -> X + T
    pcr.plus({ "derivation" : ["X",["X","+","T"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
    
    # X -> X - T
    pcr.minus({ "derivation": ["X",["X","-","T"]] , "identifier": "-" ,"definition_node?": False ,"builder": B.minus , "visitor": V.binary_opt } ),
    
    # X -> T
    pcr.ASTNode({  "derivation": ["X",["T"]] , "identifier": "E->T" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ),
    
    # T-> T * F
    pcr.multiplication({ "derivation": ["T",["T","*","F"]] , "identifier": "*" , "definition_node?": False  , "builder": B.multiplier, "visitor": V.binary_opt } ),
    
    # T -> T / F
    pcr.divition({ "derivation": ["T",["T","/","F"]] , "identifier": "/" , "definition_node?": False  , "builder": B.divition, "visitor": V.binary_opt } ),
    
    # T -> F
    pcr.ASTNode({  "derivation": ["T",["F"]] , "identifier": "T->F" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ),
    
    # F -> i
    pcr.variable({ "derivation": ["F",["i"]] , "identifier": "var" ,"definition_node?": False , "builder": B.var  , "visitor": V.var } ),
    
    # F -> ( X )
    pcr.ASTNode({  "derivation": ["F",["(","X",")"]] , "identifier": "brackets" , "definition_node?": False ,"builder": B.brackets , "visitor": V.brackets } ),
    
    # E -> A
    pcr.ASTNode({  "derivation": ["E",["A" ]] , "identifier": "E-> A" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # E -> T ;
    pcr.ASTNode({  "derivation": ["E",["T",";" ]] , "identifier": "E-> T ;" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # E -> F ;
    pcr.ASTNode({  "derivation": ["E",["F",";" ]] , "identifier": "E-> F ;" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # E -> X ;
    pcr.ASTNode({  "derivation": ["E",["X",";" ]] , "identifier": "E-> X ;" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
]

non_terminals = [
    
        "E",
        "X",
        "F",
        "T",
        "A",
                           
]

terminals= [
            
            "let",
            "=",
            ";",
            "+",
            "-",
            "*",
            "/",
            "i" ,
            "(" ,
            ")" ,
            "$" , 
            
        ]

grammar =[ 
          numbers, let, variable,
        #  For , IN  , booleans  , expression_block , 
        #   vector , protocols , types , function , While , conditional , 
        #  strings , function_caLL
        ]