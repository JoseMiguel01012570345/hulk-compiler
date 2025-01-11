import copy
from ..lexer import HULK_LANGUAGE_DEFINITION 
symb_and_op = HULK_LANGUAGE_DEFINITION .SYMBOLS_and_OPERATORS_parser  
from . import GRAMMAR_PRODUCTIONS as GD
from src.semantic_check import context_and_type_checking, visitor
ctck = context_and_type_checking

import json

def parse_input( code , allow=1 ):

    parser_table =  read_from_json()
    
    symbols = []
    state = [0]
    tree = []
    error = False
    parser_msg = []
    
    k = 0
    while k < len(code):
        
        item = code[k].Text
        
        if not special_token(item=item):
            item = "int"
            
        result =""
        
        if dict(parser_table[ state[-1] ]).__contains__( item ) : 
            result = parser_table[ state[-1] ][ item ]
            
            if result == "*":
                parser_msg.append( f"\033[1;31m unexpected {code[k].Text } at line: {code[k].line} column: {code[k].column} \033[0m" )
                print( f"\033[1;31m unexpected {code[k].Text } at line: {code[k].line} column: {code[k].column} \033[0m" )
                error = True
                break
        
        else: # no string belongness
            parser_msg.append(f"\033[1;31m >> ERROR: item \033[1;33m {code[k].Text } \033[1;31m is not valid at line { code[k].line } column {code[k].column} \033[0m")
            print(f"\033[1;31m >> ERROR: item \033[1;33m {code[k].Text } \033[1;31m is not valid at line { code[k].line } column {code[k].column} \033[0m")
            error = True
            break
            
        if type(result) == int: # shift
            
            state.append(result)
            symbols.append(item)
            parser_msg.append(  f"{symbols} state={state[-1]}" )
            tree.append(code[k])
            
        elif type(result) == tuple or type(result) == list : # reduce
            
            i = 0
            token_list = []
            
            while i < len(result[0][1]):
                
                state.pop()
                token = tree[-1]
                token_list.insert(0,token)
                symbols.pop()
                tree.pop()
                
                i += 1

                parser_msg.append( f"{symbols} state={state[-1]}" )
                
            result_ast = search_ast_in_grammar(result[0])
            
            ast = copy.deepcopy(result_ast)
            
            ast_initialized = ast.ignition(token_list=token_list) # initialize ast
            ast_reduced = visitor.ast_reducer(ast=ast_initialized) # reduce ast
            
            tree.append( ast_reduced )
                
            key_stone = result[0][0]
            last_state_number = state[-1]
            
            if parser_table[ last_state_number ][ key_stone ] == "*":
                parser_msg.append( f"unexpected character at line {code[k].line} and column {code[k].line}" )
                print( f"unexpected character at line {code[k].line} and column {code[k].line}" )
                error = True 
                break
            
            state.append( parser_table[ last_state_number ][ key_stone ] )
            
            symbols.append(key_stone)
            parser_msg.append( f"{symbols} state={state[-1]}" )
            
            continue  
        
        elif result == "OK":
                break
            
        else: # error
            parser_msg.append( f"\033[1;31m >> ERROR: item \033[1;33m {code[k].Text } \033[1;31m is not valid at line { code[k].line } column {code[k].column} \033[0m" )
            print( f"\033[1;31m >> ERROR: item \033[1;33m {code[k].Text } \033[1;31m is not valid at line { code[k].line } column {code[k].column} \033[0m" )
            error = True
            break
        
        k +=1
    
    if error:
        parser_process_printer( allow=allow , parser_msg=parser_msg)
        exit()
    
    parser_msg.append( f"\033[1;32m GOOD syntaxis \033[0m" )
    print( f"\033[1;32m GOOD syntaxis \033[0m" )
    
    parser_process_printer( allow=allow , parser_msg=parser_msg)
    return tree[0]

def parser_process_printer( allow= 1 , parser_msg:list=[] ):
    parser_file = open('./parser_file.txt' , 'w')
    if allow:
        for msg in parser_msg:
            parser_file.write( f"{msg} \n" )
        
        parser_msg.clear()
    parser_file.close()

def search_ast_in_grammar( production ):        
        grammar = GD.grammar
        k = 0
        for feature in grammar:
            
            for ast in feature:
                
                if production[0] == ast.derivation[0] and len(production[1]) == len(ast.derivation[1]): 
                    is_equal = 0
                    for index,right_side in enumerate(ast.derivation[1]):
                        if right_side != production[1][index]:
                            break
                        is_equal += 1
                    if is_equal == len(production[1]):
                        return ast
                k += 1
                
        raise Exception("no index found")
    
def special_token(item):
    return GD.terminals.__contains__(item) or symb_and_op.__contains__(item)
    
def read_from_json( ):
    with open("./src/parser/parser_table.json","r") as file:
        return json.load(file)
            
        