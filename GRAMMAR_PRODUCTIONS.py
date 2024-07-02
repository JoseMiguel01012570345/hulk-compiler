import builder as B
import production_class_representation as pcr
import visitor as V

function_caLL = [

]

strings = [
    
]

booleans = [
    
]


For = [
        
]

conditional = [
        
]

While = [

]



vector = [

]

types = [

]

protocols = [
    
]

function = [    

    pcr.def_function({ "derivation": [ "func" , ["function" , "atom" , "param" , "exp"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),
    
    pcr.def_function({ "derivation": [ "func" , [ "atom" , "param" , "=>" , "exp"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),
    
    pcr.def_function({ "derivation": [ "exp" , ["func"]] , "identifier": "exp" , "definition_node?": False , "builder": B.replacement , "visitor": V.replacement }),

]

IN = [

    # high_level -> structure in high_level
    # pcr.def_function({ "derivation": [ "high_level", [ "structure" , "in" , "high_level" ] ] , "identifier": "def_function" , "definition_node?":False , "builder": B.in_ , "visitor": V.def_function }),
    
    # exp -> structure in exp
    pcr.def_function({ "derivation": [ "high_level", [ "param", "in" , "high_level" ] ] , "identifier": "def_function" , "definition_node?":False , "builder": B.in_ , "visitor": V.def_function }),
    
]

params=[
    
    # structure -> high_level , high_level
    pcr.params({ "derivation": [ "structure", [ "structure", "," , "high_level" ] ] , "identifier": "structure" , "definition_node?":False , "builder": B.structure , "visitor": V.structure }),
    
    pcr.params({ "derivation": [ "structure", [ "high_level", "," , "high_level" ] ] , "identifier": "structure" , "definition_node?":False , "builder": B.structure , "visitor": V.structure }),
    
    # structure ->  high_level
    # pcr.params({ "derivation": [ "structure", [ "high_level" ] ] , "identifier": "structure" , "definition_node?":False , "builder": B.replacement , "visitor": V.replacement }),
    
    # param -> ( structure )
    pcr.params({ "derivation": [ "param", [ "(" , "structure" ,")" ] ] , "identifier": "structure" , "definition_node?":False , "builder": B.params , "visitor": V.replacement }),
    
]

variable = [
    
    pcr.variable({  "derivation": ["var_declaration",["atom", "=" , "high_level" ]] , "identifier": "var" , "definition_node?": False ,"builder": B.re_asigment , "visitor": V.var } ) ,
    
]

expression_block = [
    
    # B -> { E
    pcr.block({  "derivation": ["block",[ "{", "exp" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block } ) ,
    
    # B -> BB
    pcr.block({  "derivation": ["block",[ "block", "block" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block   } ) ,
    
    # B -> BE
    pcr.block({  "derivation": ["block",[ "block", "exp" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block   } ) ,
    
    # high_level -> B }  ;
    pcr.block({  "derivation": ["high_level",[ "block", "}" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # E-> B }    
    pcr.block({  "derivation": ["exp",[ "block", "}" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # E -> high_level ;
    pcr.ASTNode({ "derivation": ["exp",["high_level",";" ]] , "identifier": "None" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
]

let = [

    # var_declaration -> let atom = high_level
    pcr.let({  "derivation": ["var_declaration",["let","atom", "=" , "high_level" ]] , "identifier": "let" , "definition_node?": True ,"builder": B.let , "visitor": V.let } ) ,
]

numbers = [
    
    # X -> X + T
    pcr.plus({ "derivation" : ["sum_minus",["sum_minus","+","div_mult"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
    
    # X -> X - T
    pcr.minus({ "derivation": ["sum_minus",["sum_minus","-","div_mult"]], "identifier": "-" ,"definition_node?": False ,"builder": B.minus , "visitor": V.binary_opt } ),
    
    # X -> T
    pcr.ASTNode({  "derivation": ["sum_minus",["div_mult"]] , "identifier": "E->T" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ),
    
    # T-> T * F
    pcr.multiplication({ "derivation": ["div_mult",["div_mult","*","atom"]] , "identifier": "*" , "definition_node?": False  , "builder": B.multiplier, "visitor": V.binary_opt } ),
    
    # T -> T / F
    pcr.divition({ "derivation": ["div_mult",["div_mult","/","atom"]] , "identifier": "/" , "definition_node?": False  , "builder": B.divition, "visitor": V.binary_opt } ),
    
    # T -> F
    pcr.ASTNode({  "derivation": ["div_mult",["atom"]] , "identifier": "T->F" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ),
    
    # F -> i
    pcr.variable({ "derivation": ["atom",["int"]] , "identifier": "var" ,"definition_node?": False , "builder": B.var  , "visitor": V.var } ),
    
    # high_level -> sum_minus
    pcr.ASTNode({  "derivation": ["high_level",[ "sum_minus" ]] , "identifier": "None" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # high_level -> var_declaration
    pcr.ASTNode({  "derivation": ["high_level",["var_declaration" ]] , "identifier": "None" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # atom -> ( high_level )
    pcr.ASTNode({  "derivation": ["atom",[ "(", "high_level",")" ]] , "identifier": "None" , "definition_node?": False ,"builder": B.brackets , "visitor": V.brackets } ) ,

]

non_terminals = [
    
        "exp",
        "sum_minus",
        "atom",
        "div_mult",
        "var_declaration",
        "block",
        "high_level",
        "structure",
        "param",
        "func",
        "hl_in"
                           
]
terminals= [
            
            "=>",
            "function",
            "in",
            "let",
            ",",
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
          
        numbers, let, variable,expression_block, params,
        For , IN  , booleans   , 
        vector , protocols , types , function , While , conditional , 
        strings , function_caLL
        
        ]