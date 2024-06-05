
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
    
    
    # sum
    ["E" , [ "A" ]],
    ["E",["(","A",")"]],
    ["A",["(","A",")"]],
    ["A",["E","+","A"]],
    ["A",["i"]],
    
]

non_terminals = [
    
        "A",
        "E",
                            
]

terminals= [
            
            "+",
            
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