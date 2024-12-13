from os import system

from src.parser import Parser as P
from src.semantic_check import context_and_type_checking, semantic_errors, visitor
from src.lexer.lexer_definition import HULKLexer

system("cls")

file = open('./TestCode.hk','r')
code = file.read()
file.close()

Lexer = HULKLexer()
Lexer.LoadCode(code)

tokens = [token for token in Lexer.Tokenize()]


#__________________PARSER__________________________________________

# go to parse
gp =P.Parser( [value[0] for value in tokens] , use_saved_table=1 )

ast = gp.tree


if ast == None: 
    
    print(" \033[1;32m >\033[1;31m CODE HAS ERRORS :( \033[0m")
    exit()

ast = visitor.ast_reducer(ast=ast)

#_________________________SEMANTIC CHEKING__________________________________

error_list = []

context_error = semantic_errors.semantic_errors()

# check types

# check rules

# check_context
graph = context_and_type_checking.context_checker(ast=ast,error_list=error_list , printing= 1 )

context_error.add_error(error_list)

context_error.print_()

#_________________________CODE GENERATION__________________________________


# AST = ASTCilBuilder( ast=ast )

# print(AST.Code)

pass
#________________________END_____________________________________________