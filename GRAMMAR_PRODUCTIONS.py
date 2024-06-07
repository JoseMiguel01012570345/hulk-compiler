
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
    
    ["E",["T","+","E"]],
    ["E",["T","-","E"]],
    ["E",["T"]],
    
    ["T",["T","*","F"]],
    ["T",["T","/","F"]],
    ["T",["T","%","F"]],
    ["T",["F"]],
    
    ["F",["(","E",")"]],
    ["F",["i"]]
    
]

non_terminals = [
    
        "E",
        "F",
        "T",
                           
]

terminals= [
            
            "+",
            "%",
            "-",
            "*",
            "/",
            "i" ,
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