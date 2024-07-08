<<<<<<< HEAD
from Lexer import Lexer
from RegExDefinitions import TokenConstrainedRegEx,TokenFinitRegEx
from TokensDefinition import KeywordToken,SimbolToken,OperatorToken,VariableToken,LiteralToken,Type,SimbolEndToken
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES,SIMBOL_VALUES,OPERATOR_VALUES
from Rules import LiteralBooleanRule,LiteralNumericRule,LiteralStringRule,NameVariableRule
<<<<<<< HEAD
from ExpressionDefinitions import NumberExpression,StringExpression,BooleanExpression
from VariableDefinitions import NumberVariable,StringVariable,BooleanVariable
from LiteralDefinitions import NumberLiteral,StringLiteral,BooleanLiteral
import GRAMMAR_PRODUCTIONS
import translator
=======
>>>>>>> 12f9d30 (column and line showing when semantic error, done)
=======

from lexer import HULKLexer
>>>>>>> bac6c5e (lexer fixed)
import Parser as P
from os import system
import semantic_errors
import visitor
import context_checker


file = open('./TestCode.hk','r')
code = file.read()
file.close()

Lexer = HULKLexer()
Lexer.LoadCode(code)

<<<<<<< HEAD
keyword_token_recognizer = TokenFinitRegEx(KEYWORD_VALUES,KeywordToken)

simbol_token_recognizer = TokenFinitRegEx(SIMBOL_VALUES,SimbolToken)

operator_token_recognizer = TokenFinitRegEx(OPERATOR_VALUES,OperatorToken)

variable_token_recognizer = TokenConstrainedRegEx([NameVariableRule()],VariableToken)

boolean_literal_token_recognizer = TokenConstrainedRegEx([LiteralBooleanRule()],LiteralToken,Type.Boolean)

numeric_literal_token_recognizer = TokenConstrainedRegEx([LiteralNumericRule()],LiteralToken,Type.Number)

string_literal_token_recognizer = TokenConstrainedRegEx([LiteralStringRule()],LiteralToken,Type.String)

print('+++++++++++++++++++++ TokeniZING ++++++++++++++++++++++++++++++')

# save to priority dictionary

recognizers = {
    0: keyword_token_recognizer,
    1: simbol_token_recognizer,
    2: operator_token_recognizer,
    3: boolean_literal_token_recognizer,
    4: numeric_literal_token_recognizer,
    5: string_literal_token_recognizer,
    6: variable_token_recognizer
}

# start lexer with defined rules

lexer = Lexer(recognizers)

system("cls")

# load code
reader = open('TestCode.hk','r')
code = reader.read()

lexer.LoadCode(code)

# check for lexical errors
Error = False
my_list =[]
<<<<<<< HEAD
for state in lexer.LexicalAnalisys(lexer.Tokenize(),FiltToken):
=======

p = lexer.LexicalAnalisys(lexer.Tokenize(),FiltToken)

for state in p :
>>>>>>> 12f9d30 (column and line showing when semantic error, done)
    
    my_list = my_list.__add__(state.TokensSequence)
    
    if state.Error != None:
        
        Error =True
        print(state)
        
        break
    pass

if not Error:
    
    tokens =[]
    for token in my_list:
        if token.Text != '\n' and token.Text != ' ':
            tokens.append(token)
    
    
    my_list = tokens + [SimbolEndToken()]
    
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    # ------------PRINTS_TOKEN_SEQUENCE----------------
    # zz=[]
    # for item in my_list:
    #     zz.append(item.Text)
    
=======
    #------------PRINTS_TOKEN_SEQUENCE----------------
>>>>>>> d3a2291 (blocks made)
    # for t in my_list:
    #     print(t.Text)
    #     pass
    # ----------------------------
    
<<<<<<< HEAD
    gd_token= translator.traslator(my_list)
    
    # print(gd_token)
=======
    gp =P.Parser( my_list )
>>>>>>> 5798f64 (another fix to the parser)
=======
=======
    print([ item.Text for item in my_list ])

    # input()
=======
tokens = [token for token in Lexer.Tokenize()]
>>>>>>> bac6c5e (lexer fixed)

#__________________PARSER__________________________________________

# go to parse
    
<<<<<<< HEAD
>>>>>>> 29b2e32 (new grammar generated)
    gp =P.Parser( my_list , use_saved_table=1 )
>>>>>>> e1988ab (fixing context issues)

<<<<<<< HEAD
    gp =P.Parser(GRAMMAR_PRODUCTIONS.gramar,gd_token )

    if gp.Error : exit()
    
    elif gp.derivation_Tree == None: 
        
        print(" \033[1;32m >\033[1;31m CODE HAS ERRORS :( \033[0m")
        exit()
#_________________________SEMANTIC CHEKING__________________________________

    gp.derivation_Tree.parent_reference()

    gp.derivation_Tree.send_context()
    
    context_error = semantic_errors.context_errors()
    
    error_list = gp.derivation_Tree.context_check([])
=======
    ast = gp.tree
    if ast == None: 
        
        print(" \033[1;32m >\033[1;31m CODE HAS ERRORS :( \033[0m")
        exit()

    ast = visitor.ast_reducer(ast=ast)
=======
gp =P.Parser( [value[0] for value in tokens] , use_saved_table=1 )

ast = gp.tree
if ast == None: 
>>>>>>> bac6c5e (lexer fixed)
    
    print(" \033[1;32m >\033[1;31m CODE HAS ERRORS :( \033[0m")
    exit()

ast = visitor.ast_reducer(ast=ast)

#_________________________SEMANTIC CHEKING__________________________________
<<<<<<< HEAD
    
    error_list = []
    
    context_error = semantic_errors.semantic_errors()
    
<<<<<<< HEAD
<<<<<<< HEAD
    # error_list = ast.context_check([])
>>>>>>> 5689be6 (steps to code -> search_in_ast <- hard coded)
    
    context_error.add_error(error_list)
    
=======
=======
    # check types
    
    # check rules
    
    # check_context
    graph = context_checker.context_checker(ast=ast,error_list=error_list , printing= 1 )
    
<<<<<<< HEAD
    # check rules
    
<<<<<<< HEAD
>>>>>>> e1988ab (fixing context issues)
    error_list = []
    
    ast.check_context(error_list)
    
=======
>>>>>>> e5f3f48 (another fix in blocks builder)
=======
>>>>>>> eb2506b (id changed to replacement , @@ changed to .)
    context_error.add_error(error_list)
    
>>>>>>> 9d5529b (context checking has passed a few tests)
    context_error.print_()
    
#_________________________CODE GENERATION__________________________________

    
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    AST = ASTCilBuilder(gp.derivation_Tree)
=======
    # AST = ASTCilBuilder( ast=ast )
>>>>>>> cb6fe93 (fixes made to grammar)
=======
    AST = ASTCilBuilder( ast=ast )
>>>>>>> 4e16424 (refactoring cil code)
=======
    # AST = ASTCilBuilder( ast=ast )
>>>>>>> 3dcd092 (dot-comma to the blocks)
    
    print(AST.Code)
=======

error_list = []

context_error = semantic_errors.semantic_errors()

# check types

# check rules

# check_context
graph = context_checker.context_checker(ast=ast,error_list=error_list , printing= 1 )

context_error.add_error(error_list)

context_error.print_()

#_________________________CODE GENERATION__________________________________

>>>>>>> bac6c5e (lexer fixed)

# AST = ASTCilBuilder( ast=ast )

# print(AST.Code)

pass
#________________________END_____________________________________________