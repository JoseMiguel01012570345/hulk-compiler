from os import system

import src.parser.Parser as P

from src.semantic_check import context_and_type_checking, semantic_errors
from src.semantic_check.graph_utils import print_graph
ctck = context_and_type_checking
from src.lexer.lexer_definition import HULKLexer
from src.parser.parse_code import parse_input
from src.semantic_check import type_inspector

system("cls")

file = open('./TestCode.hk','r')
code = file.read()
file.close()

Lexer = HULKLexer()
Lexer.LoadCode(code)

tokens = [token for token in Lexer.Tokenize()]

#__________________PARSER__________________________________________
# uncomment to build states 
if P.Parser():
    exit()

# parse code
ast = parse_input( code=[value[0] for value in tokens]  , allow=1 )

s_error = semantic_errors.semantic_errors()

if ast == None: 
    
    print(" \033[1;32m >\033[1;31m Syntaxis errors :( \033[0m")
    exit()

#_________________________SEMANTIC CHEKING_______________________________

graph = ctck.init_graph()
error_log = []
ctck.solve_context_and_type( graph=graph , ast=ast , error_log=error_log , stack_referent_node=[""] ) # check context and type
s_error.add_error(error_log) # add errors to error list
s_error.print_()

print_graph( graph=graph )

type_inspector.type_inpector( ast=ast , graph=graph )


#_________________________CODE GENERATION________________________________

#________________________END_____________________________________________