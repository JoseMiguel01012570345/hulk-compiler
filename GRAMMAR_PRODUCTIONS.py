import builder as B
import production_class_representation as pcr
import visitor as V

<<<<<<< HEAD
<<<<<<< HEAD
function_caLL = [
<<<<<<< HEAD
    ["F",[ ["c","P"] , ["c","N" ] , ["c","T"] ] ],
    ["P",[["(","p",")"]]],
    ["T",[["F"]],],
    ["N",[["(",")"]]],
]

strings = [
    ["T", [ ["T","@","T"] ,["F","@","T"], ["T","@@","T"] , ["F","@@","T"]] ],
    ["E", [["T","@","E"] ,["F","@","E"],["T","@@","E"] , ["F","@@","E"] ] ],
    
    ["T", [ ["b","@","T"] ,["b","@","T"], ["b","@@","T"] , ["b","@@","T"]] ],
    ["E", [["b","@","E"] ,["b","@","E"],["b","@@","E"] , ["b","@@","E"] ] ],
    ["E", [["b","@","b"] ,["T","@","b"],["T","@@","b"] ] ]
]

expression_block = [
    ["O",[["E","E"], ["T","$2","O"] ,["O","E"],["O","B"],["O","$2","b"],["b","$2","E"],["M","E"],["E","M"],["O","M"],["M","O"]]],
    ['O',[["E","$2","M"],['M','$2','O']]],
    ["O",[["O","$2","E"],["E","$2","b"] , ["E","$2","O"],["O","$2"] , ["O",";"],["E","$2","E"],["b","$2","b"],[ 'O', '$2', 'M']]],
    ["b",[["{","O","}"],["{","E","}"],["{","B","}"],["{","}"],["b","$2"],["{","b","}"],["{","T","}"]]],
    ["B",[["b",";"]]],
    ["T",[["T","$2"]]],
    ["E",[["E","$2"],["B"]]],
    ["E",[["$2",";","$3"],["E",";"]]],
    ["O",[["M","$2"],["M","$2","M"],["M",";"],["M","M"]]],
    ["b",[["{","M","}"],]],
    
    ["E" , [["T",";"]]],
    ["T",  [["T" ,".","E"] , ["F" ,".","E"], ["T" ,".","T"] , ["F" ,".","T"] ]],
    ["E",  [["T" ,".","E"] ]],
    ["T",  [["b" ,".","E"] , ["b" ,".","E"], ["b" ,".","T"] , ["b" ,".","T"] ]],
    ["E",  [["b" ,".","E"] ]],
    ["T",  [["b" ,".","b"] , ["b" ,".","b"], ["b" ,".","b"] , ["b" ,".","b"] ]],
    ["E",  [["b" ,".","b"] ]],
    ["T",  [["T" ,".","b"] , ["T" ,".","b"], ["T" ,".","b"] , ["T" ,".","b"] ]],
    ["E",  [["T" ,".","b"] ]]
]

<<<<<<< HEAD
literals = [

<<<<<<< HEAD
    ["T" , [ ["let","T"] , ["T",":","T"]]],
    ["E" , [ ["let","E"] , ["T",":","E"]]],
    ["p" , [ ["T", ",","$2" ,"T" ] , ["T",",","$2","p"],['M',',','$2','M'] ,
            ['M',',','$2','T'] , ['T',',','$2','M'] ,['M',',','$2','p'],['p',',','$2','T']]],
    ["p" , [ ["E", ",","$2" ,"E" ] , ["E",",","$2","p"],['E',',','$2','M'] , ['M',',','$2','E'],
            ['E',',','$2','T'] , ['T',',','$2','E'],['p',',','$2','E']]],
    ["p" , [ ["b", ",","$2" ,"E" ] , ["b",",","$2","p"],['b',',','$2','M'] , ['M',',','$2','b'],
            ['E',',','$2','b'] , ['T',',','$2','b'],['b',',','$2','T'],['p',',','$2','b']]],
    ["T" , [ ["T",":=","T"] ]],
    ["T" , [ ["T",":=","b"] ]],
    ["E" , [ ["T",":=","E"] ]],
    ["T" , [ ["T","=","T"]  ]],
    ["T" , [ ["T","=","b"]  ]],
    ["E" , [  ["T","=","E"] ]],
    ["T" , [ ["T","as","T"] , ["F","as","T"] , ["T","as","E"] ]],
    ["E" , [ ["T","as","E"] ]],
    ["E", [["T",";","$2"]]],
    ["T", [["(","T",")"]]],
=======
#     [ "",[ [] , [] ] ]

# ]

=======
>>>>>>> 3c71142 (asigment and variable declaration , ok)
# booleans = [
=======

]
=======
>>>>>>> 927b086 (networkx for visualization)

strings = [
    
]

=======
>>>>>>> 401b67f (ast_reduction and grammar improved , grammar: added label non terminal)
booleans = [
>>>>>>> d3a2291 (blocks made)
    
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
    pcr.params({ "derivation": [ "structure", [  "high_level" ] ] , "identifier": "." , "definition_node?":False , "builder": B.replacement , "visitor": V.block }),
    
    # structure -> high_level , high_level
    pcr.params({ "derivation": [ "structure", [ "high_level", "," , "high_level" ] ] , "identifier": "args" , "definition_node?":False , "builder": B.structure , "visitor": V.block }),
    
    # param -> ( structure )
    pcr.params({ "derivation": [ "param", [ "(" , "structure" ,")" ] ] , "identifier": "args" , "definition_node?":False , "builder": B.params , "visitor": V.block }),
    
    # param -> ( )
    pcr.params({ "derivation": [ "param", [ "(",")" ] ] , "identifier": "args" , "definition_node?":False , "builder": B.params , "visitor": V.block }),
    
]

variable = [
    
    # var_declaration -> atom = high_level
    pcr.binary_opt({  "derivation": ["high_level",["label", "=" , "high_level" ]] , "identifier": "assigment" , "definition_node?": False ,"builder": B.assigment , "visitor": V.binary_opt } ) ,
    
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
    
    pcr.block({  "derivation": ["block",[ "block", "}" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block } ) ,
    
    # exp -> high_level ;
    pcr.ASTNode({ "derivation": ["exp",["high_level",";" ]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
]

let = [

    pcr.let({  "derivation": ["var_declaration",["let","label" ]] , "identifier": "let" , "definition_node?": True ,"builder": B.let , "visitor": V.var } ) ,
]

numbers = [
    
<<<<<<< HEAD
<<<<<<< HEAD
    # ( ["E",["E","+","T"]] , None ),
    # ( ["E",["E","-","T"]] , None ),
    # ( ["E",["T"]] , None ),
    
<<<<<<< HEAD
<<<<<<< HEAD
    # sum
<<<<<<< HEAD
    ["E" , [ "A", "+" , "A" ]],
    ["A" , [ "i" , "+" , "i" ]],
    ["A" , [ "A" , "+" , "i" ]],
    
    # # backets
    
    # ["E" , [ "(" , "A" , ")" ]],
    
    # ["E",["A"]]

    ["E",["(","E",")"]],
<<<<<<< HEAD
    ["E",["(","i",")"]],
>>>>>>> 9c513df (parser bug fixed at repeated states)
=======
    ["E",["(","A",")"]],
>>>>>>> 31c5d2d (moving out verbose info)

=======
    ["E" , [ "A" ]],
    ["E",["(","A",")"]],
    ["A",["(","A",")"]],
    ["A",["A","+","E"]],
    ["E",["A","*","E"]],
    ["A",["i"]],
=======
    ["T",["T","*","F"]],
    ["T",["T","/","F"]],
    ["T",["F"]],
    
    ["F",["(","E",")"]],
    ["F",["i"]]
>>>>>>> 4ea3226 (another fix to the parser, chose the first reduction)
    
<<<<<<< HEAD
>>>>>>> a54ff54 (first grammar made)
=======
    # ["E",["A","X","=","X"]],
    # ["A",["let"]],
    # ["X",["i"]],
=======
    # ( ["T",["T","*","F"]] , None ),
    # ( ["T",["T","/","F"]] , None ),
    # ( ["T",["F"]] , None ),
    
    # ( ["F",["(","E",")"]] , None ),
    # ( ["F",["i"]] , None )
    
=======
    # E -> E + T
>>>>>>> f0e66da (formated productions)
    pcr.plus({ "derivation" : ["E",["E","+","T"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
=======
    # X -> X + T
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    pcr.plus({ "derivation" : ["X",["X","+","T"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
>>>>>>> 3c71142 (asigment and variable declaration , ok)
=======
    pcr.plus({ "derivation" : ["X",["X","+","F"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
>>>>>>> cb6fe93 (fixes made to grammar)
=======
    pcr.plus({ "derivation" : ["X",["X","+","T"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
>>>>>>> c73392d (hidding blocks , ok)
=======
    pcr.plus({ "derivation" : ["sum_minus",["sum_minus","+","div_mult"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
>>>>>>> 12f9d30 (column and line showing when semantic error, done)
=======
    pcr.plus({ "derivation" : ["X",["X","+","T"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
>>>>>>> ce54e3f (error detected in parser, fixed)
=======
    pcr.plus({ "derivation" : ["sum_minus",["sum_minus","+","div_mult"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
>>>>>>> 359e6da (productions name changed)
    
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
    
<<<<<<< HEAD
    # F -> i
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    pcr.variable({ "derivation": ["F",["i"]] , "identifier": "var" ,"definition_node?": False , "builder": B.var  , "visitor": V.var } ),
<<<<<<< HEAD
    # F -> ( E )
    pcr.ASTNode({  "derivation": ["F",["(","E",")"]] , "identifier": "brackets" , "definition_node?": False ,"builder": B.brackets , "visitor": V.brackets } ),
>>>>>>> b1116a1 (AST almost integrated to parser)
=======
=======
    pcr.variable({ "derivation": ["F",["int"]] , "identifier": "var" ,"definition_node?": False , "builder": B.var  , "visitor": V.var } ),
>>>>>>> d3a2291 (blocks made)
=======
=======
    # atom -> int
<<<<<<< HEAD
>>>>>>> 00754c6 (high level expression can peform arithmetic operations)
    pcr.variable({ "derivation": ["atom",["int"]] , "identifier": "var" ,"definition_node?": False , "builder": B.var  , "visitor": V.var } ),
>>>>>>> 12f9d30 (column and line showing when semantic error, done)
=======
    pcr.variable({ "derivation": ["F",["int"]] , "identifier": "var" ,"definition_node?": False , "builder": B.var  , "visitor": V.var } ),
>>>>>>> ce54e3f (error detected in parser, fixed)
=======
    pcr.variable({ "derivation": ["atom",["int"]] , "identifier": "var" ,"definition_node?": False , "builder": B.var  , "visitor": V.var } ),
>>>>>>> 359e6da (productions name changed)
    
    # high_level -> sum_minus
    pcr.ASTNode({  "derivation": ["high_level",[ "sum_minus" ]] , "identifier": "None" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
<<<<<<< HEAD
<<<<<<< HEAD
    # E -> A
    pcr.ASTNode({  "derivation": ["exp",["var_declaration" ]] , "identifier": "E-> A" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # E -> T ;
    pcr.ASTNode({  "derivation": ["exp",["div_mult",";" ]] , "identifier": "E-> T ;" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # E -> F ;
    pcr.ASTNode({  "derivation": ["exp",["atom",";" ]] , "identifier": "E-> F ;" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
    # E -> X ;
<<<<<<< HEAD
    pcr.ASTNode({  "derivation": ["E",["X",";" ]] , "identifier": "E-> X ;" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
>>>>>>> 3c71142 (asigment and variable declaration , ok)
=======
    pcr.ASTNode({  "derivation": ["exp",["sum_minus",";" ]] , "identifier": "E-> X ;" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
>>>>>>> 12f9d30 (column and line showing when semantic error, done)
    
>>>>>>> 20b2c73 (perfect)
=======
    # high_level -> A
    pcr.ASTNode({  "derivation": ["high_level",["var_declaration" ]] , "identifier": "E-> A" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
=======
    # high_level -> var_declaration
    pcr.ASTNode({  "derivation": ["high_level",["var_declaration" ]] , "identifier": "None" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
>>>>>>> ee5f8ca (let-in made)
=======
    pcr.ASTNode({ "derivation": ["atom",["label"]] , "identifier": ".r" ,"definition_node?": False , "builder": B.replacement  , "visitor": V.replacement } ),
    
    pcr.variable({ "derivation": ["label",["int"]] , "identifier": "var" ,"definition_node?": False , "builder": B.var  , "visitor": V.var } ),
    
    # high_level -> sum_minus
    pcr.ASTNode({  "derivation": ["high_level",[ "sum_minus" ]] , "identifier": "." , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
>>>>>>> 401b67f (ast_reduction and grammar improved , grammar: added label non terminal)
    
    # atom -> ( high_level )
    pcr.ASTNode({  "derivation": ["atom",[ "(", "high_level",")" ]] , "identifier": "." , "definition_node?": False ,"builder": B.brackets , "visitor": V.replacement } ) ,

<<<<<<< HEAD
>>>>>>> ce54e3f (error detected in parser, fixed)
=======

>>>>>>> 00754c6 (high level expression can peform arithmetic operations)
]

booleans = [
    
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    ["T" , [["T","&","T"] , ["F","&","T"] ,  ["T","|","T"]  , ["F","|","T"]  , ["T","!=","T"] , ["F","!=","T"] , 
            ["T",">","T"] , ["F",">","T"]  , ["T","<","T"]  , ["F","<","T"]  , ["T","<=","T"] , ["F","<=","T"] ,
            ["T",">=","T"] ,["F",">=","T"] , ["T","==","T"] , ["F","==","T"] , 
            ["T","is","T"] , ["F","is","T"] ,['!','T'] ,      ['!','F']]],
    
    ["T" , [["b","&","T"] , ["b","&","T"] ,  ["b","|","T"]  , ["b","!=","T"] ,
            ["b",">","T"] , ["b",">","T"]  , ["b","<","T"]  , ["b","<=","T"],
            ["b",">=","T"] ,["b",">=","T"] , ["b","==","T"] , 
            ["b","is","T"] , ["b","is","T"] ,['!','b'] ]],
    
    ["E" , [["T","&","b"]  , ["T","|","b"]  , ["T","!=","b"] ,
            ["T",">","b"]  , ["T","<","b"]  , ["T","<=","b"] ,
            ["T",">=","b"] , ["T","==","b"] , 
            ["T","is","b"] ]],
    
    ["T" , [["b","&","b"] , ["b","&","b"] ,  ["b","|","b"]  , ["b","!=","b"] ,
            ["b",">","b"] , ["b",">","b"]  , ["b","<","b"]  , ["b","<=","b"],
            ["b",">=","b"] ,["b",">=","b"] , ["b","==","b"] , 
            ["b","is","b"] , ["b","is","b"] ,['!','b'] ]],
    
    ["E" , [["b","&","E"]  , ["b","|","E"]  , ["b","!=","E"] ,
            ["b",">","E"]  , ["b","<","E"]  , ["b","<=","E"] ,
            ["b",">=","E"] , ["b","==","E"] , 
            ["b","is","E"] ]],
    
    ["E" , [["T","&","E"]  , ["T","|","E"]  , ["T","!=","E"] ,
            ["T",">","E"]  , ["T","<","E"]  , ["T","<=","E"] ,
            ["T",">=","E"] , ["T","==","E"] , 
            ["T","is","E"] ]],
=======
        "T",
=======
        "A",
>>>>>>> 31c5d2d (moving out verbose info)
        "E",
                            
>>>>>>> 9c513df (parser bug fixed at repeated states)
=======
=======
>>>>>>> ce54e3f (error detected in parser, fixed)
        "E",
        "X",
        "F",
        "T",
        "A",
<<<<<<< HEAD
        "B"
=======
=======
>>>>>>> 359e6da (productions name changed)
        "exp",
        "sum_minus",
        "atom",
        "div_mult",
        "var_declaration",
<<<<<<< HEAD
        "block"
>>>>>>> 12f9d30 (column and line showing when semantic error, done)
=======
        "B",
=======
        "block",
>>>>>>> 359e6da (productions name changed)
        "high_level",
<<<<<<< HEAD
>>>>>>> ce54e3f (error detected in parser, fixed)
=======
        "structure",
        "param",
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        "func",
<<<<<<< HEAD
>>>>>>> e0c1daa (functions parsed)
=======
        "hl_in"
>>>>>>> ee5f8ca (let-in made)
=======
>>>>>>> 00754c6 (high level expression can peform arithmetic operations)
=======
        "function",
>>>>>>> 7f6df08 (adding functional programming)
=======
>>>>>>> 927b086 (networkx for visualization)
=======
        "label"
>>>>>>> 401b67f (ast_reduction and grammar improved , grammar: added label non terminal)
                           
>>>>>>> 4ea3226 (another fix to the parser, chose the first reduction)
]
<<<<<<< HEAD
<<<<<<< HEAD

<<<<<<< HEAD
numbers = [
    
    ["T" , [["T","+","T"] , ["T","+","T"] , ["T","-","T"],[ "T","*","T"], ["T","/","T"],["T","/","T"], ["T","^","T"], ["T","%","T"],["T","**","T"]]],
    ["T" , [["T","$2","+","T"] , ["T","$2","+","T"] , ["T","$2","-","T"],[ "T","$2","*","T"], ["T","$2","/","T"],["T","$2","/","T"], ["T","$2","^","T"], ["T","$2","%","T"],["T","$2","**","T"]]],
    ["E" , [["T","$2","+","E"] , ["T","$2","+","E"] , ["T","$2","-","E"],[ "T","$2","*","E"], ["T","$2","/","E"],["T","$2","/","E"], ["T","$2","^","E"], ["T","$2","%","E"],["T","$2","**","E"]]],
    ["E" , [["T","+","E"], ["F"+"E"],["T","-","E"],[ "T","*","E"], ["T","/","E"],["T","/","E"], ["T","^","E"], ["T","E"]]],
    ["T" , [ ["T","-=","T"] ,["T","+=","T"] ,["T","/=","T"] ,["T","*=","T"] , ["T","--"]  , ["T","++"]]],
    ["E" , [ ["T","-=","E"] ,["T","+=","E"] ,["T","/=","E"] ,["T","*=","E"] , ["E","--"] , ["E","++"],["E","**"],["E","**","E"]]],
    
    ["T" , [["b","+","T"] , ["b","+","T"] , ["b","-","T"],[ "b","*","T"], ["b","/","T"], ["b","^","T"], ["b","%","T"],["b","**","T"]]],
    ["T" , [["b","$2","+","T"] , ["b","$2","+","T"] , ["b","$2","-","T"],[ "b","$2","*","T"], ["b","$2","/","T"],["b","$2","/","T"], ["b","$2","^","T"], ["b","$2","%","T"],["b","$2","**","T"]]],
    ["E" , [["b","$2","+","E"] , ["b","$2","+","E"] , ["b","$2","-","E"],[ "b","$2","*","E"], ["b","$2","/","E"],["b","$2","/","E"], ["b","$2","^","E"], ["b","$2","%","E"],["b","$2","**","E"]]],
    ["E" , [["b","+","E"], ["F"+"E"],["b","-","E"],[ "b","*","E"], ["b","/","E"],["b","/","E"], ["b","^","E"]]],

<<<<<<< HEAD
]
=======
=======
=======
>>>>>>> e0c1daa (functions parsed)
=======

>>>>>>> b0043c9 (another bug in the parser fixed, ->fist set<-)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            "-",
>>>>>>> 31c5d2d (moving out verbose info)
=======
            
>>>>>>> a54ff54 (first grammar made)
=======
            "*",
>>>>>>> 5798f64 (another fix to the parser)
=======
            "%",
=======
>>>>>>> 20b2c73 (perfect)
            "-",
            "*",
            "/",
<<<<<<< HEAD
>>>>>>> 4ea3226 (another fix to the parser, chose the first reduction)
            "i" ,
=======
            "int" ,
>>>>>>> d3a2291 (blocks made)
            "(" ,
            ")" ,
            "{",
            "}",
            "$" , 
            
        ]
>>>>>>> 9c513df (parser bug fixed at repeated states)

<<<<<<< HEAD
IN = [
    
    ["p",[["p","$2"]]],
    ["T", [["T","in","T"] ,["T","$2","in","T"],["p","$2","in","T"],["p","$2","in","p"], ["p","in","T"] , ["p","in","p"]]],
    ["T", [["T","$2"]]],
    ["E", [["T","in","E"], ["T","$2","in","E"] ,["T","in","b"],["T","$2","in","b"] ,["p","$2","in","E"] ,["p","in","E"],["p","in","b"],["p","$2","in","b"]]],
       
]

For = [
    
    ["E" , [["for","T","$2","B"] , ["for","T","$2","E"], ["for","T","E"]]],
    ["E", [ ["for","T","$2","b"]]],
]

conditional = [
    
    ["if",[["if","T","$2","E"],["if","T","$2","b"],["if","T","$2","B"],["if","$2"],['if', 'T', '$2', 'T',]]],
    ["elif",[["if","elif","T","$2","E"],["if","elif","T","$2","b"],["if","elif","T","$2","B"],["elif","$2"],['if','elif', 'T', '$2', 'T',]]],
    ["E",[["if","else","E"],["if","else","b"],["if","else","B"]]],
    ["E",[["elif","else","E"],["elif","else","b"],["elif","else","B"]]],
    ["T",[["elif","else","T"],['if', 'else', 'T']]],
    
]

While = [
    
    ["E" , [["while","T","$2","B"] , ["while","T","$2","E"],["while","T","E"]]],
    ["E", [ ["while","T","$2","b"]]],
]

function = [    
 
    ["M" , [ ["function","T","$2","=>","$2","E"] , ["function","T",":","T" ,"=>","$2","E"] 
            ,["function","T","$2","=>","$2","b"] ,["function","T",":","T","=>","$2","b"] ,
             [ 'function', 'T', ':', 'T', 'b'],['function', 'T', '$2', 'b', ],['function', 'T', '$2' ,'E', ],
             ['T','$2' , '=>', '$2', 'E'],['T', ':' , 'T' , '=>', '$2', 'E'],
             ['T', ':', 'E'],['T', ':', 'T', 'b'],
            ]],
]

types = [
    ["M", [["type","T","$2","b"  ], ["type","T","$2","inherits","T","$2","b"],
           ["type","T","b"] , ['type', 'T', 'inherits', 'T', 'b']  ]],
    ["T" , [ ["new","F"] ]],
]

protocols = [
    ["M" , [["protocol","T","$2","b"] ,[ "protocol","T","$2","extends","T","$2","b"],['protocol', 'T', 'b',],['protocol', 'T', 'extends', 'T', 'b',]]]
    
]

vector = [
    
    ["T" , [[ "[","T","||","T" , "]"] , [ "[" , "p" , "]" ] , ["T","[" , "T" , "]" ]  ]],
]

gramar =[ vector , protocols , types , function , While , conditional , 
         For , IN , numbers , booleans , literals , expression_block , 
         strings , function_caLL
=======
grammar =[ 
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          numbers, let, variable,
        #  For , IN  , booleans  , expression_block , 
        #   vector , protocols , types , function , While , conditional , 
        #  strings , function_caLL
>>>>>>> 3c71142 (asigment and variable declaration , ok)
=======
          
<<<<<<< HEAD
        numbers, let, variable,expression_block,
=======
        
        numbers, let, variable,expression_block, params ,
>>>>>>> 12f9d30 (column and line showing when semantic error, done)
=======
          
        numbers, let, variable,expression_block,
>>>>>>> ce54e3f (error detected in parser, fixed)
=======
        numbers, let, variable,expression_block, params,
>>>>>>> e0c1daa (functions parsed)
        For , IN  , booleans   , 
        vector , protocols , types , function , While , conditional
        , function_caLL
        
>>>>>>> d3a2291 (blocks made)
        ]