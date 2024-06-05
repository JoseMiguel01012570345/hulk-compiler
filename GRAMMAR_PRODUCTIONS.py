
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
    
    # minus
    # ["E" , [ "A", "-" , "A" ]],
    # ["A" , [ "i" , "-" , "i" ]],
    # ["A" , [ "A" , "-" , "i" ]],
    
    # ["A" , [ "i" ]],
    
    # # sum
    # ["E" , [ "A", "+" , "A" ]],
    # ["A" , [ "i" , "+" , "i" ]],
    # ["A" , [ "A" , "+" , "i" ]],
    
    # # backets
    
    # ["E" , [ "(" , "A" , ")" ]],
    
    # ["E",["A"]]

    ["E",["(","E",")"]],
    ["E",["(","i",")"]],

]

non_terminals = [
    
        "T",
        "E",
                            
]

terminals= [

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