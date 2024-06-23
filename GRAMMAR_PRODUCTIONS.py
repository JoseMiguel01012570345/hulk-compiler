import builder as B
import production_class_representation as pcr
import visitor as V

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

strings = [
    
]

booleans = [
>>>>>>> d3a2291 (blocks made)
    
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
    
    pcr.variable({  "derivation": ["A",["F", "=" , "E" ]] , "identifier": "var" , "definition_node?": False ,"builder": B.re_asigment , "visitor": V.var } ) ,
    
]

expression_block = [
    
    # B -> { E
    pcr.block({  "derivation": ["B",[ "{", "E" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block } ) ,
    # B -> BB
    pcr.block({  "derivation": ["B",[ "B", "B" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block   } ) ,
    # B -> BE
    pcr.block({  "derivation": ["B",[ "B", "E" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.block , "visitor": V.block   } ) ,
    # E-> B }    
    pcr.block({  "derivation": ["E",[ "B", "}" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    # E-> B } ;    
    pcr.block({  "derivation": ["E",[ "B", "}",";" ]] , "identifier": "block" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ) ,
    
]
let = [

    # A -> let F = X
    pcr.let({  "derivation": ["A",["let","F", "=" , "E" ]] , "identifier": "let" , "definition_node?": True ,"builder": B.let , "visitor": V.let } ) ,
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
    pcr.plus({ "derivation" : ["X",["X","+","T"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
>>>>>>> 3c71142 (asigment and variable declaration , ok)
=======
    pcr.plus({ "derivation" : ["X",["X","+","F"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
>>>>>>> cb6fe93 (fixes made to grammar)
=======
    pcr.plus({ "derivation" : ["X",["X","+","T"]] , "identifier": "+" ,"definition_node?": False ,"builder": B.plus  , "visitor": V.binary_opt } ),
>>>>>>> c73392d (hidding blocks , ok)
    
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
>>>>>>> 3c71142 (asigment and variable declaration , ok)
    
>>>>>>> 20b2c73 (perfect)
]

booleans = [
    
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
        "E",
        "X",
        "F",
        "T",
        "A",
        "B"
                           
>>>>>>> 4ea3226 (another fix to the parser, chose the first reduction)
]

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
terminals= [
            
            "let",
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
          numbers, let, variable,
        #  For , IN  , booleans  , expression_block , 
        #   vector , protocols , types , function , While , conditional , 
        #  strings , function_caLL
>>>>>>> 3c71142 (asigment and variable declaration , ok)
=======
          
        numbers, let, variable,expression_block,
        For , IN  , booleans   , 
        vector , protocols , types , function , While , conditional , 
        strings , function_caLL
        
>>>>>>> d3a2291 (blocks made)
        ]