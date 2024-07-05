import builder as B
import production_class_representation as pcr
import visitor as V

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

function_caLL = [

    # high_level -> atom param
    pcr.function_call({ "derivation": [ "atom" , [ "atom" , "param" ]] , "identifier": "function_call" , "definition_node?": False , "builder": B.function_call , "visitor": V.function_call }),
    
]

types = [

    # atom -> type atom block
    pcr.type_({ "derivation": [ "atom" , ["type" , "label" , "block"]] , "identifier": "type" , "definition_node?": True , "builder": B.type , "visitor": V.type }),
    
    # type -> type atom param block
    pcr.type_({ "derivation": [ "atom" , ["type" , "label"  , "param" , "block"]] , "identifier": "type" , "definition_node?": True , "builder": B.type , "visitor": V.type }),
    
    # type -> type atom inherits atom block
    pcr.type_({ "derivation": [ "atom" , ["type" , "label"  , "inherits" , "atom" , "block"]] , "identifier": "type" , "definition_node?": True , "builder": B.type , "visitor": V.type }),
    
    # type -> type atom param inherits atom param block
    pcr.type_({ "derivation": [ "atom" , ["type" , "label" , "param"  , "inherits" , "atom" , "param" , "block"]] , "identifier": "type" , "definition_node?": True , "builder": B.type , "visitor": V.type }),
    
]

protocols = [
    
    # atom -> protocol atom block
    pcr.protocol({ "derivation": [ "atom" , ["protocol" , "label" , "block"]] , "identifier": "protocol" , "definition_node?": True , "builder": B.protocol , "visitor": V.protocol }),
    
    # atom -> protocol atom extends atom block
    pcr.protocol({ "derivation": [ "atom" , ["protocol" , "label" , "extends" , "atom" , "block"]] , "identifier": "protocol" , "definition_node?": True , "builder": B.protocol , "visitor": V.protocol }),
    
]

function = [    
    
    # exp -> function atom param exp
    pcr.def_function({ "derivation": [ "atom" , ["function" , "atom" , "param" , "block"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),
    
    pcr.def_function({ "derivation": [ "high_level" , ["function" , "atom" , "param" , "high_level"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),
    
    pcr.def_function({ "derivation": [ "exp" , ["function" , "atom" , "param" , "exp"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),

    # # exp -> atom param => exp
    pcr.def_function({ "derivation": [ "atom" , [ "atom" , "param" , "=>" , "block"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),
    
    pcr.def_function({ "derivation": [ "exp" , [ "atom" , "param" , "=>" , "exp"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),
    
    # # high_level -> atom param => high_level
    pcr.def_function({ "derivation": [ "high_level" , [ "atom" , "param" , "=>" , "high_level"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),

]

IN = [

    # exp -> structure in high_level
    pcr.in_({ "derivation": [ "high_level", [ "param", "in" , "high_level" ] ] , "identifier": "auto_call" , "definition_node?":False , "builder": B.in_ , "visitor": V.def_function }),
    
    # high_level -> high_level in high_level
    pcr.in_({ "derivation": [ "high_level", [ "high_level", "in" , "high_level" ] ] , "identifier": "auto_call" , "definition_node?":False , "builder": B.in_ , "visitor": V.def_function }),
    
]

params=[
    
    # structure -> structure , high_level
    pcr.params({ "derivation": [ "structure", [ "structure", "," , "high_level" ] ] , "identifier": "args" , "definition_node?":False , "builder": B.structure , "visitor": V.block }),
    
    # structure -> high_level
    pcr.params({ "derivation": [ "structure", [  "high_level" ] ] , "identifier": "." , "definition_node?":False , "builder": B.replacement , "visitor": V.replacement }),
    
    # structure -> high_level , high_level
    pcr.params({ "derivation": [ "structure", [ "high_level", "," , "high_level" ] ] , "identifier": "args" , "definition_node?":False , "builder": B.structure , "visitor": V.block }),
    
    # param -> ( structure )
    pcr.params({ "derivation": [ "param", [ "(" , "structure" ,")" ] ] , "identifier": "args" , "definition_node?":False , "builder": B.params , "visitor": V.replacement }),
    
    # param -> ( )
    pcr.params({ "derivation": [ "param", [ "(",")" ] ] , "identifier": "args" , "definition_node?":False , "builder": B.params , "visitor": V.replacement }),
    
]

variable = [
    
    # var_declaration -> atom = high_level
    pcr.binary_opt({  "derivation": ["high_level",["atom", "=" , "high_level" ]] , "identifier": "assigment" , "definition_node?": False ,"builder": B.assigment , "visitor": V.binary_opt } ) ,
    
    # var_declaration -> let atom = high_level
    pcr.binary_opt({  "derivation": ["high_level",["var_declaration", "=" , "high_level" ]] , "identifier": "assigment" , "definition_node?": False ,"builder": B.assigment , "visitor": V.binary_opt } ) ,
    
]

expression_block = [
    
    # block -> { exp
    pcr.block({  "derivation": ["block",[ "{", "exp" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block } ) ,
    
    # block -> block block
    pcr.block({  "derivation": ["block",[ "block", "block" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block   } ) ,
    
    # block -> block exp
    pcr.block({  "derivation": ["block",[ "block", "exp" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block   } ) ,
    
    pcr.ASTNode({  "derivation": ["block",[ "block", "}" ]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # exp -> high_level ;
    pcr.ASTNode({ "derivation": ["exp",["high_level",";" ]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
]

let = [

    pcr.let({  "derivation": ["var_declaration",["let","atom" ]] , "identifier": "let" , "definition_node?": True ,"builder": B.let , "visitor": V.var } ) ,
]

numbers = [
    
    # X -> X + T
    pcr.plus({ "derivation" : ["sum_minus",["sum_minus","+","div_mult"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
    
    # X -> X - T
    pcr.minus({ "derivation": ["sum_minus",["sum_minus","-","div_mult"]], "identifier": "-" ,"definition_node?": False ,"builder": B.minus , "visitor": V.binary_opt } ),
    
    # X -> T
    pcr.ASTNode({  "derivation": ["sum_minus",["div_mult"]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ),
    
    # T-> T * F
    pcr.multiplication({ "derivation": ["div_mult",["div_mult","*","atom"]] , "identifier": "*" , "definition_node?": False  , "builder": B.multiplier, "visitor": V.binary_opt } ),
    
    # T -> T / F
    pcr.divition({ "derivation": ["div_mult",["div_mult","/","atom"]] , "identifier": "/" , "definition_node?": False  , "builder": B.divition, "visitor": V.binary_opt } ),
    
    # T -> F
    pcr.ASTNode({  "derivation": ["div_mult",["atom"]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ),
    
    # atom -> int
    pcr.ASTNode({ "derivation": ["atom",["label"]] , "identifier": ".r" ,"definition_node?": False , "builder": B.replacement  , "visitor": V.replacement } ),
    
    pcr.variable({ "derivation": ["label",["int"]] , "identifier": "var" ,"definition_node?": False , "builder": B.var  , "visitor": V.var } ),
    
    # high_level -> sum_minus
    pcr.ASTNode({  "derivation": ["high_level",[ "sum_minus" ]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # atom -> ( high_level )
    pcr.ASTNode({  "derivation": ["atom",[ "(", "high_level",")" ]] , "identifier": "." , "definition_node?": False ,"builder": B.brackets , "visitor": V.replacement } ) ,


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
        "label"
                           
]
terminals= [
            
            "function",
            "inherits",
            "extends",
            "type",
            "protocol",
            "=>",
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
        vector , protocols , types , function , While , conditional
        , function_caLL
        
        ]