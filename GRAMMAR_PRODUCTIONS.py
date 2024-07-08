import builder as B
import production_class_representation as pcr
import visitor as V

For = [

    # atom -> for param block
    pcr.for_({  "derivation": [ "atom" , [ "for" , "param" , "block" ]] , "identifier": "for" , "definition_node?": False , "builder": B.for_while , "visitor": V.for_while }),
    
    # exp -> for param exp
    pcr.for_({  "derivation": [ "atom" , [ "for" , "param" , "exp" ]] , "identifier": "for" , "definition_node?": False , "builder": B.for_while , "visitor": V.for_while }),
    
    # atom -> for param high_level
    pcr.for_({  "derivation": [ "atom" , [ "for" , "param" , "high_level" ]] , "identifier": "for" , "definition_node?": False , "builder": B.for_while , "visitor": V.for_while }),
      
]

conditional = [

    # if_high_level -> if param high_level
    pcr.if_({  "derivation": [ "if_high_level" , [ "if" , "param" , "high_level" ]] , "identifier": "if" , "definition_node?": False , "builder": B.if_elif , "visitor": V.if_else }),
    
    # if_exp -> if param exp
    pcr.if_({  "derivation": [ "if_exp" , [ "if" , "param" , "exp" ]] , "identifier": "if" , "definition_node?": False , "builder": B.if_elif , "visitor": V.if_else }),
    
    # if_exp -> if param exp
    pcr.if_({  "derivation": [ "if_exp" , [ "if" , "param" , "block" ]] , "identifier": "if" , "definition_node?": False , "builder": B.if_elif , "visitor": V.if_else }),
    
    # elif_high_level -> elif param high_level
    pcr.elif_({  "derivation": [ "elif_high_level" , [ "elif" , "param" , "high_level" ]] , "identifier": "elif" , "definition_node?": False , "builder": B.if_elif , "visitor": V.if_else }),
    
    # elif_exp -> elif param exp
    pcr.elif_({  "derivation": [ "elif_exp" , [ "elif" , "param" , "exp" ]] , "identifier": "elif" , "definition_node?": False , "builder": B.if_elif , "visitor": V.if_else }),
    
    # elif_exp -> elif param exp
    pcr.elif_({  "derivation": [ "elif_exp" , [ "elif" , "param" , "block" ]] , "identifier": "elif" , "definition_node?": False , "builder": B.if_elif , "visitor": V.if_else }),
    
    # else_high_level -> else high_level
    pcr.else_({  "derivation": [ "else_high_level" , [ "else" , "high_level" ]] , "identifier": "else" , "definition_node?": False , "builder": B.else_ , "visitor": V.else_ }),
    
    # else_exp -> else exp
    pcr.else_({  "derivation": [ "else_exp" , [ "else" , "exp" ]] , "identifier": "else" , "definition_node?": False , "builder": B.else_ , "visitor": V.else_ }),
    
    # else_exp -> else block
    pcr.else_({  "derivation": [ "else_exp" , [ "else" , "block" ]] , "identifier": "else" , "definition_node?": False , "builder": B.else_ , "visitor": V.else_ }),

    # atom -> if high_level else_high_level
    pcr.block({  "derivation": [ "atom" , [ "if_high_level" , "else_high_level" ]] , "identifier": "conditional_block" , "definition_node?": False , "builder": B.conditional , "visitor": V.conditional }),
    
    # atom -> if_high_level elif_high_level else_high_level
    pcr.block({  "derivation": [ "atom" , [ "if_high_level" , "elif_high_level" , "else_high_level" ]] , "identifier": "conditional_block" , "definition_node?": False , "builder": B.conditional , "visitor": V.conditional }),
    
    # exp -> if_exp else_exp
    pcr.block({  "derivation": [ "exp" , [ "if_exp" , "else_exp" ]] , "identifier": "conditional_block" , "definition_node?": False , "builder": B.conditional , "visitor": V.conditional }),
    
    # exp -> if_exp elif_exp else_exp
    pcr.block({  "derivation": [ "exp" , [ "if_exp" , "elif_exp" , "else_exp" ]] , "identifier": "conditional_block" , "definition_node?": False , "builder": B.conditional , "visitor": V.conditional }),
        
]

While = [

    # atom -> while param block
    pcr.while_({  "derivation": [ "atom" , [ "while" , "param" , "block" ]] , "identifier": "while" , "definition_node?": False , "builder": B.for_while , "visitor": V.for_while }),
    
    # exp -> while param exp
    pcr.while_({  "derivation": [ "exp" , [ "while" , "param" , "exp" ]] , "identifier": "while" , "definition_node?": False , "builder": B.for_while , "visitor": V.for_while }),
    
    # atom -> while param high_level
    pcr.while_({  "derivation": [ "atom" , [ "while" , "param" , "high_level" ]] , "identifier": "while" , "definition_node?": False , "builder": B.for_while , "visitor": V.for_while }),

]

vector = [

]

function_caLL = [

    # high_level -> atom param
    pcr.function_call({ "derivation": [ "call" , [ "label" , "param" ]] , "identifier": "function_call" , "definition_node?": False , "builder": B.function_call , "visitor": V.function_call }),
    
    pcr.ASTNode({ "derivation": [ "atom" , [ "call" ]] , "identifier": "." , "definition_node?": False , "builder": B.replacement , "visitor": V.replacement }),

]

types = [

    # atom -> type atom block
    pcr.type_({ "derivation": [ "atom" , ["type" , "label" , "block"]] , "identifier": "type" , "definition_node?": True , "builder": B.type , "visitor": V.type }),
    
    # type -> type atom param block
    pcr.type_({ "derivation": [ "atom" , ["type" , "label"  , "param" , "block"]] , "identifier": "type" , "definition_node?": True , "builder": B.type , "visitor": V.type }),
    
    # type -> type atom inherits atom block
    pcr.type_({ "derivation": [ "atom" , ["type" , "label"  , "inherits" , "label" , "block"]] , "identifier": "type" , "definition_node?": True , "builder": B.type , "visitor": V.type }),
    
    # type -> type atom param inherits atom param block
    pcr.type_({ "derivation": [ "atom" , ["type" , "label" , "param"  , "inherits" , "label" , "param" , "block"]] , "identifier": "type" , "definition_node?": True , "builder": B.type , "visitor": V.type }),
    
]

protocols = [
    
    # atom -> protocol atom block
    pcr.protocol({ "derivation": [ "atom" , ["protocol" , "label" , "block"]] , "identifier": "protocol" , "definition_node?": True , "builder": B.protocol , "visitor": V.protocol }),
    
    # atom -> protocol atom extends atom block
    pcr.protocol({ "derivation": [ "atom" , ["protocol" , "label" , "extends" , "label" , "block"]] , "identifier": "protocol" , "definition_node?": True , "builder": B.protocol , "visitor": V.protocol }),
    
]

function = [    
    
    # exp -> function atom param exp
    pcr.def_function({ "derivation": [ "atom" , ["function" , "label" , "param" , "block"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),
    
    pcr.def_function({ "derivation": [ "high_level" , ["function" , "label" , "param" , "high_level"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),
    
    pcr.def_function({ "derivation": [ "exp" , ["function" , "label" , "param" , "exp"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),

    # # exp -> atom param => exp
    pcr.def_function({ "derivation": [ "atom" , [ "label" , "param" , "=>" , "block"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),
    
    pcr.def_function({ "derivation": [ "exp" , [ "label" , "param" , "=>" , "exp"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),
    
    # # high_level -> atom param => high_level
    pcr.def_function({ "derivation": [ "high_level" , [ "label" , "param" , "=>" , "high_level"]] , "identifier": "def_function" , "definition_node?": True , "builder": B.def_function , "visitor": V.def_function }),

]

IN = [

    # exp -> structure in high_level
    pcr.in_({ "derivation": [ "high_level", [ "param", "in" , "high_level" ] ] , "identifier": "auto_call" , "definition_node?":False , "builder": B.in_ , "visitor": V.def_function }),
    
    # high_level -> high_level in high_level
    pcr.in_({ "derivation": [ "high_level", [ "high_level", "in" , "high_level" ] ] , "identifier": "auto_call" , "definition_node?":False , "builder": B.in_ , "visitor": V.def_function }),
    
    # high_level -> high_level in block
    pcr.in_({ "derivation": [ "high_level", [ "high_level", "in" , "block" ] ] , "identifier": "auto_call" , "definition_node?":False , "builder": B.in_ , "visitor": V.def_function }),
    
    # exp -> high_level in exp
    pcr.in_({ "derivation": [ "exp", [ "high_level", "in" , "exp" ] ] , "identifier": "auto_call" , "definition_node?":False , "builder": B.in_ , "visitor": V.def_function }),
    
    # exp -> structure in exp
    pcr.in_({ "derivation": [ "exp", [ "param", "in" , "exp" ] ] , "identifier": "auto_call" , "definition_node?":False , "builder": B.in_ , "visitor": V.def_function }),
    
]

params=[
    
    # structure -> structure , high_level
    pcr.params({ "derivation": [ "structure", [ "structure", "," , "high_level" ] ] , "identifier": "args" , "definition_node?":False , "builder": B.structure , "visitor": V.block }),
    
    # structure -> high_level
    pcr.params({ "derivation": [ "structure", [  "high_level" ] ] , "identifier": "." , "definition_node?":False , "builder": B.block , "visitor": V.block }),
    
    # structure -> high_level , high_level
    pcr.params({ "derivation": [ "structure", [ "high_level", "," , "high_level" ] ] , "identifier": "args" , "definition_node?":False , "builder": B.structure , "visitor": V.block }),
    
    # param -> ( structure )
    pcr.params({ "derivation": [ "param", [ "(" , "structure" ,")" ] ] , "identifier": "args" , "definition_node?":False , "builder": B.params , "visitor": V.block }),
    
    # param -> ( )
    pcr.params({ "derivation": [ "param", [ "(",")" ] ] , "identifier": "args" , "definition_node?":False , "builder": B.params , "visitor": V.block }),
    
]

variable = [
    
    # var_declaration -> atom = high_level
    pcr.assign({  "derivation": ["high_level",["label", "=" , "high_level" ]] , "identifier": "assigment" , "definition_node?": False ,"builder": B.assigment , "visitor": V.binary_opt } ) ,
    
    # var_declaration -> let atom = high_level
    pcr.assign({  "derivation": ["high_level",["var_declaration", "=" , "high_level" ]] , "identifier": "assigment" , "definition_node?": False ,"builder": B.assigment , "visitor": V.binary_opt } ) ,
    
    pcr.assign({  "derivation": ["high_level",["label", ":=" , "high_level" ]] , "identifier": "re_assigment" , "definition_node?": False ,"builder": B.assigment , "visitor": V.binary_opt } ) ,
    
]

expression_block = [
    
    # block -> { exp
    pcr.block({  "derivation": ["block",[ "{", "exp" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block } ) ,
    
    # block -> block block
    pcr.block({  "derivation": ["block",[ "block", "block" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block   } ) ,
    
    # block -> block exp
    pcr.block({  "derivation": ["block",[ "block", "exp" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block   } ) ,
    
    pcr.block({  "derivation": ["block",[ "block", "}" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block } ) ,
    
    pcr.block({  "derivation": ["block",[ "{", "}" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block } ) ,
    
    # exp -> high_level ;
    pcr.ASTNode({ "derivation": ["exp",["high_level",";" ]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
]

let = [

    pcr.let({  "derivation": ["var_declaration",["let","label" ]] , "identifier": "let" , "definition_node?": True ,"builder": B.let , "visitor": V.var } ) ,
]

unary_opt = [
    
    # high_level -> new call
    pcr.new({  "derivation": ["high_level",["new", "label" , "param" ]] , "identifier": "instance" , "definition_node?": False ,"builder": B.unary_opt , "visitor": V.unary_opt }),
    
    # bool -> ! high_level
    pcr.not_({  "derivation": ["bool",["!","bool" ]] , "identifier": "!" , "definition_node?": False ,"builder": B.unary_opt , "visitor": V.unary_opt }),
    
    # bool -> label ++
    pcr.plus_plus({  "derivation": ["high_level",["label","++" ]] , "identifier": "++" , "definition_node?": False ,"builder": B.unary_opt , "visitor": V.unary_opt }),
    
    pcr.minus_minus({  "derivation": ["high_level",["label","--" ]] , "identifier": "--" , "definition_node?": False ,"builder": B.unary_opt , "visitor": V.unary_opt }),
    
]

binary_opt = [
    
    # ---------------------------
    
    # bool -> high_level.label
    pcr.dot({ "derivation" : ["atom",["label", "." ,"label"]] , "identifier": "dot" ,"definition_node?": False ,"builder": B.binary_opt  , "visitor": V.binary_opt } ),
    
    # dot -> high_level . label param
    pcr.dot({ "derivation" : ["atom",["label", "." ,"call" ]] , "identifier": "dot" ,"definition_node?": False ,"builder": B.binary_opt  , "visitor": V.binary_opt } ),
    
    # 4 == a.b()    
    # ---------------------------
    
    # bool -> bool == concatenation
    pcr.equal({ "derivation" : ["bool",["concatenation","==","bool"]] , "identifier": "equal" ,"definition_node?": False ,"builder": B.binary_opt  , "visitor": V.binary_opt } ),
    
    # bool -> bool >= concatenation
    pcr.bigger_than({ "derivation" : ["bool",["concatenation",">=","bool"]] , "identifier": "or" ,"definition_node?": False ,"builder": B.binary_opt  , "visitor": V.binary_opt } ),
    
    # bool -> bool <= concatenation
    pcr.smaller_than({ "derivation" : ["bool",["concatenation","<=","bool"]] , "identifier": "or" ,"definition_node?": False ,"builder": B.binary_opt  , "visitor": V.binary_opt } ),
    
    # bool -> bool & concatenation
    pcr.and_({ "derivation" : ["bool",["concatenation","&","bool"]] , "identifier": "or" ,"definition_node?": False ,"builder": B.binary_opt  , "visitor": V.binary_opt } ),
    
    # bool -> bool | concatenation
    pcr.or_({ "derivation" : ["bool",["concatenation","|","bool"]] , "identifier": "or" ,"definition_node?": False ,"builder": B.binary_opt  , "visitor": V.binary_opt } ),
    
    pcr.ASTNode({ "derivation" : ["bool",["concatenation"]] , "identifier": "." ,"definition_node?": False ,"builder": B.replacement  , "visitor": V.replacement } ),
    
    # concatenation -> concatenation @ sum_minus
    pcr.concatenation({ "derivation" : ["concatenation",["concatenation","@","sum_minus"]] , "identifier": "@" ,"definition_node?": False ,"builder": B.binary_opt  , "visitor": V.binary_opt } ),
    
    # concatenation -> concatenation @@ sum_minus
    pcr.concatenation({ "derivation" : ["concatenation",["concatenation","@@","sum_minus"]] , "identifier": "@@" ,"definition_node?": False ,"builder": B.binary_opt  , "visitor": V.binary_opt } ),
    
    pcr.ASTNode({ "derivation" : ["concatenation",["sum_minus"]] , "identifier": "." ,"definition_node?": False ,"builder": B.replacement  , "visitor": V.replacement } ),
    
    # X -> X + T
    pcr.plus({ "derivation" : ["sum_minus",["sum_minus","+","div_mult"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.binary_opt  , "visitor": V.binary_opt } ),
    
    # X -> X - T
    pcr.minus({ "derivation": ["sum_minus",["sum_minus","-","div_mult"]], "identifier": "-" ,"definition_node?": False ,"builder": B.binary_opt , "visitor": V.binary_opt } ),
    
    # X -> T
    pcr.ASTNode({  "derivation": ["sum_minus",["div_mult"]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ),
    
    # T-> T * F
    pcr.multiplication({ "derivation": ["div_mult",["div_mult","*","pow"]] , "identifier": "*" , "definition_node?": False  , "builder": B.binary_opt, "visitor": V.binary_opt } ),
    
    # T -> T / F
    pcr.divition({ "derivation": ["div_mult",["div_mult","/","pow"]] , "identifier": "/" , "definition_node?": False  , "builder": B.binary_opt, "visitor": V.binary_opt } ),
    
    # div_mult -> pow
    pcr.ASTNode({  "derivation": ["div_mult",["pow"]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ),
    
    # T-> T ** F
    pcr.pow_({ "derivation": ["pow",["pow","**","atom"]] , "identifier": "**" , "definition_node?": False  , "builder": B.binary_opt, "visitor": V.binary_opt } ),
    
    # T-> T ^ F
    pcr.pow_({ "derivation": ["pow",["pow","^","atom"]] , "identifier": "^" , "definition_node?": False  , "builder": B.binary_opt, "visitor": V.binary_opt } ),
    
    # T-> T % F
    pcr.per_cent({ "derivation": ["pow",["pow","%","atom"]] , "identifier": "%" , "definition_node?": False  , "builder": B.binary_opt, "visitor": V.binary_opt } ),
    
    # T -> F
    pcr.ASTNode({  "derivation": ["pow",["atom"]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ),
    
    # atom -> int
    pcr.ASTNode({ "derivation": ["atom",["label"]] , "identifier": "." ,"definition_node?": False , "builder": B.replacement  , "visitor": V.replacement } ),
    
    # label -> int
    pcr.variable({ "derivation": ["label",["int"]] , "identifier": "var" ,"definition_node?": False , "builder": B.var  , "visitor": V.var } ),
    
    # high_level -> sum_minus
    pcr.ASTNode({  "derivation": ["high_level",[ "bool" ]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
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
        "label",
        "if_high_level",
        "if_exp",
        "elif_high_level",
        "elif_exp",
        "else_high_level",
        "else_exp",
        "concatenation",
        "pow",
        "bool",
        "call",
                    
]

terminals= [
    
            ".",
            "new",
            "!",
            "++",
            "--",
            "==",
            ">=",
            "<=",
            "|",
            "&",
            "%",
            "**",
            "^",
            ":=",
            "@",
            "@@",
            "if",
            "elif",
            "else",
            "for",
            "while",
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
          
        binary_opt,
        let,
        variable ,
        expression_block,
        params,
        For ,
        IN ,
        vector ,
        protocols ,
        types ,
        function ,
        While ,
        conditional,
        function_caLL ,
        unary_opt
        
        ]