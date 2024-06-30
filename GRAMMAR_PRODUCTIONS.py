import builder as B
import production_class_representation as pcr
import visitor as V

function_caLL = [

]

strings = [
    
]

booleans = [
    
]

IN = [
       
]

For = [
        
]

conditional = [
        
]

While = [

]

function = [    

]

types = [

]

protocols = [
    
]

vector = [

]

variable = [
    
    pcr.variable({  "derivation": ["A",["F", "=" , "high_level" ]] , "identifier": "var" , "definition_node?": False ,"builder": B.re_asigment , "visitor": V.var } ) ,
    
]

expression_block = [
    
    # B -> { E
    pcr.block({  "derivation": ["B",[ "{", "E" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block } ) ,
    
    # B -> BB
    pcr.block({  "derivation": ["B",[ "B", "B" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block   } ) ,
    
    # B -> BE
    pcr.block({  "derivation": ["B",[ "B", "E" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block   } ) ,
    
    # high_level -> B }  ;
    pcr.block({  "derivation": ["high_level",[ "B", "}" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # E-> B }    
    pcr.block({  "derivation": ["E",[ "B", "}" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # E -> high_level ;
    pcr.ASTNode({ "derivation": ["E",["high_level",";" ]] , "identifier": "E-> X ;" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
]

let = [

    # A -> let F = X
    pcr.let({  "derivation": ["A",["let","F", "=" , "high_level" ]] , "identifier": "let" , "definition_node?": True ,"builder": B.let , "visitor": V.let } ) ,
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
    pcr.variable({ "derivation": ["F",["int"]] , "identifier": "var" ,"definition_node?": False , "builder": B.var  , "visitor": V.var } ),
    
    # high_level -> X
    pcr.ASTNode({  "derivation": ["high_level",["X" ]] , "identifier": "E-> A" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # high_level -> A
    pcr.ASTNode({  "derivation": ["high_level",["A" ]] , "identifier": "E-> A" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    pcr.ASTNode({  "derivation": ["high_level",[ "(", "high_level",")" ]] , "identifier": "E-> X ;" , "definition_node?": False ,"builder": B.brackets , "visitor": V.brackets } ) ,

]

non_terminals = [
    
        "E",
        "X",
        "F",
        "T",
        "A",
        "B",
        "high_level",
                           
]

terminals= [
            
            "let",
            "=",
            ";",
            "+",
            "-",
            "*",
            "/",
            "int" ,
            "(" ,
            ")" ,
            "{",
            "}",
            "$" , 
            
        ]

grammar =[ 
          
        numbers, let, variable,expression_block,
        For , IN  , booleans   , 
        vector , protocols , types , function , While , conditional , 
        strings , function_caLL
        
        ]