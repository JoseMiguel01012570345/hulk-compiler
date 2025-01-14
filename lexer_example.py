from src.lexer.lexer_definition import HULKLexer

lexer = HULKLexer()

#este es el caso en que defines la entrada directamente en raw
code = r'variable_a = print("the message is \"hello world\"") + 1e+100 - 1.0 + false'

#para obtenerlo wn formato raw directo de la entrada, el codigo es el siguiente:
#>>> code = input(r'')

#cuando lees el codigo directamente de un archivo, el formato por default es raw
#file = open('lexer_example.py','r')
#code = file.read()
#file.close()
#print(code) 
#esto dara como salida el contenido de este archivo en formato raw

#la entrada del lexer debe venir en formato raw

lexer.LoadCode(code)

for token,status in lexer.Tokenize():
    print(f'token: {token} -------- type: {token.Type}')
    pass

#OJO: Le hice un cambio en lexer_definition, miralo, si te conviene como estaba antes, borra lo que hice y descomenta lo que habias hecho

#la salida al ejecutar este archivo es la siguiente:

#token: variable_a -------- type: TokenType.Variable
#token: = -------- type: TokenType.Operator
#token: print -------- type: TokenType.Keyword
#token: ( -------- type: TokenType.Symbol
#token: "the message is \"hello world\"" -------- type: TokenType.String
#token: ) -------- type: TokenType.Symbol
#token: + -------- type: TokenType.Operator
#token: 1e+100 -------- type: TokenType.Number
#token: - -------- type: TokenType.Operator
#token: 1.0 -------- type: TokenType.Number
#token: + -------- type: TokenType.Operator
#token: false -------- type: TokenType.Boolean
#token: $ -------- type: TokenType.Symbol
