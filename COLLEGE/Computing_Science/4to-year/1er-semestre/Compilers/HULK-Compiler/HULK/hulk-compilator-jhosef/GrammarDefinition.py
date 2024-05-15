from GrammarInterface import ProductionType,Grammar
from ExpressionDefinitions import NumberExpression
from VariableDefinitions import NumberVariable
from LiteralDefinitions import NumberLiteral
from EnumsTokensDefinition import TokenType,Operator,Simbol,SimbolType,OperatorType,Type

"""
Las definiciones de las gramaticas
"""

# falta diferenciar entre las prioridades de la potencia y modulacion; y la multiplicacion y division

ArithmeticTerminals = [
    'n',
    'a',
    'p',
    '',
    '+',
    '-',
    '*',
    '/',
    '^',
    '%',
    '(',
    ')',
    '$'
]

ArithmeticNonTerminals = [
    'E',
    'T',
    'F',
    'P',
    'Q'
]

Priorities = {
    '(' : -1,
    ')' : 0,
    '+' : 0,
    '-' : 0,
    '%' : 1,
    '*' : 2,
    '/' : 2,
    '^' : 3
}

ArithmeticProductions = {
    'E' : ['E+T','E-T','T'],
    'T' : ['T%F','F'],
    'F' : ['F*P','F/P','P'],
    'P' : ['P^Q','Q'],
    'Q' : ['(E)','n']
}

ArithmeticTranslator = {
    TokenType.Literal : 'n',
    Operator.Plus : '+',
    Operator.Minus : '-',
    Operator.Div : '/',
    Operator.Mul : '*',
    Operator.Exp : '^',
    Operator.Rest : '%',
    Simbol.LeftP : '(',
    Simbol.RightP : ')',
    TokenType.Variable : 'n'
}

ArithMeticGrammar = Grammar(
    ArithmeticNonTerminals,
    ArithmeticTerminals,
    ArithmeticProductions,
    'E',
    Priorities
)