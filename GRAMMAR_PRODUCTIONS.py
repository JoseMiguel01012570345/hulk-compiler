
# function_caLL = [
#     [ "",[ [] , [] ] ]
# ]

# strings = [
    
#     [ "",[ [] , [] ] ]
# ]

# expression_block = [
    
#     [ "",[ [] , [] ] ]
    
# ]

# literals = [

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

numbers = [
    
    ["E",["E","+","T"]],
    ["E",["E","-","T"]],
    ["E",["T"]],
    
    ["T",["T","*","F"]],
    ["T",["T","/","F"]],
    ["T",["F"]],
    
    ["F",["(","E",")"]],
    ["F",["i"]]
    
    # ["E",["A","X","=","X"]],
    # ["A",["let"]],
    # ["X",["i"]],
    
]

non_terminals = [
    
        "E",
        "F",
        "T",
        # "A",
        # "X"
                           
]

terminals= [
            
            # "let",       
            "+",
            "-",
            "*",
            "/",
            "i" ,
            # "=" ,
            "(" ,
            ")" ,
            "$" , 
            
        ]

grammar =[ 
          numbers,
        #   vector , protocols , types , function , While , conditional , 
        #  For , IN  , booleans , literals , expression_block , 
        #  strings , function_caLL
        ]