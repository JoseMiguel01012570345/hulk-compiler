from os import system

from src.parser import parser as P
from src.semantic_check import context_and_type_checking, semantic_errors, visitor
from src.lexer.lexer_definition import HULKLexer
from src.parser.parse_code import parse_input

system("cls")

file = open('./TestCode.hk','r')
code = file.read()
file.close()

Lexer = HULKLexer()
Lexer.LoadCode(code)

tokens = [token for token in Lexer.Tokenize()]


#__________________PARSER__________________________________________
# uncomment to build states 
# P.Parser()

# parse code
ast , error_list = parse_input( code=[value[0] for value in tokens] )

semantic_errors

if ast == None: 
    
    print(" \033[1;32m >\033[1;31m Syntaxis errors :( \033[0m")
    exit()

#_________________________SEMANTIC CHEKING__________________________________


#_________________________CODE GENERATION__________________________________

#________________________END_____________________________________________