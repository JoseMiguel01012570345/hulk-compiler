import HULK_LANGUAGE_DEFINITION as HK

gramar =[

# function_caLL
[
    ["F",[ ["c","P"] , ["c","N" ] , ["c","T"] ] ],
    ["P",[["(","p",")"]]],
    ["T",[["F"]],],
    ["N",[["(",")"]]],
],

# strings
[
    ["T", [ ["T","@","T"] ,["F","@","T"], ["T","@@","T"] , ["F","@@","T"]] ],
    ["E", [["T","@","E"] ,["F","@","E"],["T","@@","E"] , ["F","@@","E"] ] ]
],

# expression_block
[
    ["O",[["E","E"],["O","$2","O"], ["T","$2","O"] ,["O","E"],["O","B"],["O","$2","b"],["b","$2","E"],["M","E"],["E","M"],["O","M"],["M","O"],['O','Q'],['Q','$2']]],
    ['O',[["E","$2","M"],['M','$2','O'],['O','T']]],
    ["O",[["O","$2","E"],["E","$2","b"] , ["E","$2","O"],["O","$2"] , ["O",";"],["E","$2","E"],["b","$2","b"],[ 'O', '$2', 'M']]],
    ["b",[["{","O","}"],["{","E","}"],["{","B","}"],["{","}"],["b","$2"],["{","b","}"],["{","T","}"]]],
    ["B",[["b",";"]]],
    ["T",[["T","$2"]]],
    ["E",[["E","$2"],["B"]]],
    ["E",[["$2",";","$3"],["E",";"]]],
    
    ["b",[["{","M","}"],]],
    
    ["E" , [["T",";"]]],
    ["T",  [["T" ,".","E"] , ["F" ,".","E"], ["T" ,".","T"] , ["F" ,".","T"] ]],
    ["E",  [["T" ,".","E"] ]]
],

# literals
[

    ["T" , [ ["let","T"] , ["T",":","T"]]],
    ["E" , [ ["let","E"] , ["T",":","E"]]],
    ["p" , [ ["T", ",","$2" ,"T" ] , ["T",",","$2","p"] ]], ## add function and types !!!!!!!!!!
    ["T" , [ ["T",":=","T"] ]],
    ["E" , [ ["T",":=","E"] ]],
    ["T" , [ ["T","=","T"]  ]],
    ["E" , [  ["T","=","E"] ]],
    ["T" , [ ["T","as","T"] , ["F","as","T"] , ["T","as","E"] ]],
    ["E" , [ ["T","as","E"] ]],
    ["E", [["T",";","$2"]]],
    ["T", [["(","T",")"]]],

],

# booleans
[
    
    ["T" , [["T","&","T"] , ["F","&","T"] ,  ["T","|","T"]  , ["F","|","T"]  , ["T","!=","T"] , ["F","!=","T"] , 
            ["T",">","T"] , ["F",">","T"]  , ["T","<","T"]  , ["F","<","T"]  , ["T","<=","T"] , ["F","<=","T"] ,
            ["T",">=","T"] ,["F",">=","T"] , ["T","==","T"] , ["F","==","T"] , 
            ["T","is","T"] , ["F","is","T"] ,['!','T'] ,      ['!','F']]],
    
    ["E" , [["T","&","E"]  , ["T","|","E"]  , ["T","!=","E"] ,
            ["T",">","E"]  , ["T","<","E"]  , ["T","<=","E"] ,
            ["T",">=","E"] , ["T","==","E"] , 
            ["T","is","E"] ]],
],

# numbers
[
    
    ["T" , [["T","+","T"] , ["T","+","T"] , ["T","-","T"],[ "T","*","T"], ["T","/","T"],["T","/","T"], ["T","^","T"], ["T","%","T"],["T","**","T"]]],
    ["T" , [["T","$2","+","T"] , ["T","$2","+","T"] , ["T","$2","-","T"],[ "T","$2","*","T"], ["T","$2","/","T"],["T","$2","/","T"], ["T","$2","^","T"], ["T","$2","%","T"],["T","$2","**","T"]]],
    ["E" , [["T","$2","+","E"] , ["T","$2","+","E"] , ["T","$2","-","E"],[ "T","$2","*","E"], ["T","$2","/","E"],["T","$2","/","E"], ["T","$2","^","E"], ["T","$2","%","E"],["T","$2","**","E"]]],
    ["E" , [["T","+","E"], ["F"+"E"],["T","-","E"],[ "T","*","E"], ["T","/","E"],["T","/","E"], ["T","^","E"], ["T","E"]]],
    ["T" , [ ["T","-=","T"] ,["T","+=","T"] ,["T","/=","T"] ,["T","*=","T"] , ["T","--"]  , ["T","++"]]],
    ["E" , [ ["T","-=","E"] ,["T","+=","E"] ,["T","/=","E"] ,["T","*=","E"] , ["E","--"] , ["E","++"],["E","**"],["E","**","E"]]],

],

# IN
[
    
    ["p",[["p","$2"]]],
    ["T", [["T","in","T"] ,["T","$2","in","T"],["p","$2","in","T"],["p","$2","in","p"], ["p","in","T"] , ["p","in","p"]]],
    ["T", [["T","$2"]]],
    ["E", [["T","in","E"], ["T","$2","in","E"] ,["T","in","b"],["T","$2","in","b"] ,["p","$2","in","E"] ,["p","in","E"],["p","in","b"],["p","$2","in","b"]]],
       
],

#  For
[
    
    ["E" , [["for","T","$2","B"] , ["for","T","$2","E"], ["for","T","E"]]],
    ["E", [ ["for","T","$2","b"]]],
    
],

# conditional
[
    
    ["if",[["if","T","$2","E"],["if","T","$2","b"],["if","T","$2","B"],["if","$2"],['if', 'T', '$2', 'T',]]],
    ["elif",[["if","elif","T","$2","E"],["if","elif","T","$2","b"],["if","elif","T","$2","B"],["elif","$2"],['if','elif', 'T', '$2', 'T',]]],
    ["E",[["if","else","E"],["if","else","b"],["if","else","B"]]],
    ["E",[["elif","else","E"],["elif","else","b"],["elif","else","B"]]],
    ["T",[["elif","else","T"],['if', 'else', 'T']]],
    
],

# While
[
    
    ["E" , [["while","T","$2","B"] , ["while","T","$2","E"],["while","T","E"]]],
    ["E", [ ["while","T","$2","b"]]],
],

# function
[    
 
    ["M" , [ ["function","T","$2","=>","$2","E"] , ["function","T","$2",":","T" ,"=>","$2","E"] 
            ,["function","T","$2","=>","$2","b"],["function","T","$2",":","T","=>","$2","b"] ,
            [ 'function', 'T',"$2", ':', 'T', 'b'],['function', 'T', '$2', 'b', ],['function', 'T', 'E', ],
            [ "function", "T","=>","$2","E"],
            ['T', '$2', ':', 'Q'],['T', '$2', ':', 'E'],['T', '$2', ':', 'T', 'b',],
            ['function','T','$2',':','Q']
            ]],
    ["Q",[['T', '=>', '$2', 'E']]],
    
    ["M",[["M","$2"],["M","$2","M"],["M",";"],["M","M"]]]
],

# types
[
    ["M", [["type","T","$2","b"  ], ["type","T","$2","inherits","T","$2","b"],["type","T","b"] , ['type', 'T', 'inherits', 'T', 'b']]],
    ["T" , [ ["new","F"] ]],
],

# protocols
[
    ["M" , [["protocol","T","$2","b"] ,[ "protocol","T","$2","extends","T","$2","b"],['protocol', 'T', 'b',],['protocol', 'T', 'extends', 'T', 'b',]]]
    
],

# vector
[
    
    ["T" , [[ "[","T","||","T" , "]"] , [ "[" , "p" , "]" ] , ["T","[" , "T" , "]" ]  ]],
],

]

def traslator(token_list:list):
    
    import DerivationTree as DT
    
    parse_list=[("$1",None)]
    parse_list.append(("$2",None))
    
    parse_list.append(("{",None))
    
    index=0
    while index < len(token_list ):
        
        if token_list[index].Text =="'" or token_list[index].Text == "\"" : 
            
            index1 = index + 1
            while index1 < len(token_list):
                
                if token_list[index1] == "'" or token_list[index1] == "\"" :
                
                    builder = DT.builder( "T").feature
                    
                    parse_list.append(("T", DT.DerivationTree( token_list[index1] , None ,builder) ) )
                    #parse_list.append(("T", None ) )
                    
                    index = index1
                    index += 1
                
                    break
                
                index1 +=1
                    
        kw = False                    
        for arg in HK.SYMBOLS_and_OPERATORS_parser:            
            
            if token_list[index].Text == arg:
            
                if arg == "in":
                    parse_list.append(("$2",None))
                    
                parse_list.append((token_list[index].Text,None))
                
                if arg == ";" or arg == ")" or arg == "}" or arg == "]" or arg == "," or arg == "=>":
                    
                    parse_list.append(("$2",None))
                
                kw =True
                break
            
        if not kw:
            
            if index + 1 < len(token_list) and token_list[index + 1 ].Text == "(" :
                
                builder = DT.builder( "c").feature
                
            parse_list.append(("c", DT.DerivationTree( token_list[index] , None ,builder) ) )
            #parse_list.append(("c", None ) )
            
        else:
                
            builder = DT.builder("T").feature
            parse_list.append(("T", None ))
            
            #parse_list.append(("T", DT.DerivationTree( token_list[index] , None ,builder) ) )
                
        index += 1
    
    parse_list.append(("$3",None))
    parse_list.insert(-1,("}",None))
        
    return parse_list
