"""
lexer

here is defined a basic implementation of a generic tokenizer and an implentation of a lexer for HULK langauge, joined to a lexical analyzer implementation

"""

from copy import copy
from ..status import StatusOK,StatusERROR,Error,ErrorType
from . import tokens
from . import lexical
from . import recognizers

Token,TokenType,EOF = tokens.Token , tokens.TokenType , tokens.EOF
LexicalAnalyzer,HULKLexical,ScapeChars = lexical.LexicalAnalyzer , lexical.HULKLexical , lexical.ScapeChars
KeywordRecognizer,NumericRecognizer,VariableRecognizer,BooleanRecognizer,SymbolRecognizer,OperatorRecognizer,StringRecognizer = \
recognizers.KeywordRecognizer, recognizers.NumericRecognizer , recognizers.VariableRecognizer , recognizers.BooleanRecognizer , recognizers.SymbolRecognizer , recognizers.OperatorRecognizer , recognizers.StringRecognizer


class Lexer:
    
    """
    A generic lexer definition
    
    recognizers -> list of Automaton: the token's recognizers for the language
    """
    
    _recognizers = []
    _union_recognizer = None
    _code = ''
    _position = 0
    _text_readed = ''
    _analyzer = HULKLexical()
    _line = 1
    _column = 0
    
    def __init__(self,*recognizers):
        if len(recognizers) == 0:
            raise Exception('most be at least one recognizer')
        self._recognizers = recognizers
        self._union_recognizer = recognizers[0]
        for recognizer in recognizers:
            if self._union_recognizer == recognizer: continue
            self._union_recognizer |= recognizer
            pass
        self._code = ''
        self._position = 0
        self._text_readed = ''
        pass

    def SetLexical(self,analyzer):
        """
        analyzer -> lexical analyzer for this instance
        """
        self._analyzer = analyzer
    
    def LoadCode(self,code):
        """
        load a code to tokenize
        """
        self._text_readed = ''
        self._code = code
        self._position = 0
        self._line = 1
        self._column = 0
        pass
    
    def _get_token(self):
        """
        get's the current token recognized if there's one
        """
        raise NotImplementedError()
    
    def _tokenize(self):
        """
        returns an iterable of all the tokens recognized in the source code provided
        """
        while self._position < len(self._code):
            while True:
                if self._code[0] == ' ':
                    self._code = self._code[1:]
                    break
                self._union_recognizer.move(self._code[self._position])
                if self._union_recognizer.State.Fault:
                    yield self._get_token()
                    self._text_readed = ''
                    self._union_recognizer.restart()
                    self._code = self._code[self._position:]
                    break
                self._text_readed += self._code[self._position]
                self._position += 1
                if self._position == len(self._code): 
                    yield self._get_token()
                    self._code = ''
                    break
                pass
            self._position = 0
            pass
        yield EOF(self._line,self._column)
        yield Token('$',self._column,self._line,TokenType.Symbol)
        pass
    
    def Tokenize(self):
        """
        returns an iterable of Token, StatusCode for the code loaded. If an error status is found, interrup iteration
        """
        for token in self._tokenize():
            if not token or len(token.Text) == 0 or token.Text == ' ' or token.Text == '\n': continue
            if not self._analyzer.Check(token):
                error = Error(self._analyzer.ErrorMessage,ErrorType.LEXICAL,token.Line,token.Column)
                yield token,StatusERROR(error)
                break
            yield token, StatusOK()
            pass
        pass
    
    pass

class HULKLexer(Lexer):
    
    """
    An implementation of a lexer for the HULK language
    """
    
    #esta es la configuracion que tenias tu, en donde no consideras las palabras claves
    #_priorities = {
        #0: copy(BooleanRecognizer),
        #1: copy(NumericRecognizer),
        #2: copy(StringRecognizer),
        #3: copy(VariableRecognizer),
        #4: copy(SymbolRecognizer),
        #5: copy(OperatorRecognizer)
    #}
    
    #_recognizer_types = {
        #0: TokenType.Boolean,
        #1: TokenType.Number,   
        #2: TokenType.String,
        #3: TokenType.Variable,
        #4: TokenType.Symbol,
        #5: TokenType.Operator
    #}
    
    
    #esta es la configuracion que creo que esta correcta, en donde si considero las palabras claves
    _priorities = {
        0: copy(BooleanRecognizer),
        1: copy(NumericRecognizer),
        2: copy(StringRecognizer),
        3: copy(KeywordRecognizer),
        4: copy(VariableRecognizer),
        5: copy(SymbolRecognizer),
        6: copy(OperatorRecognizer)
    }
    
    _recognizer_types = {
        0: TokenType.Boolean,
        1: TokenType.Number,   
        2: TokenType.String,
        3: TokenType.Keyword,
        4: TokenType.Variable,
        5: TokenType.Symbol,
        6: TokenType.Operator
    }
    
    def __init__(self):
        super().__init__(*[copy(self._priorities[key]) for key in self._priorities.keys()])
        pass
    
    def _get_token(self):
        for i in range(len(self._priorities.keys())):
            if self._priorities[i].recognize(self._text_readed):
                self._priorities[i].restart()
                token = Token(self._text_readed,self._column,self._line,self._recognizer_types[i])
                if token.Text == ScapeChars.JumpLine.value:
                    self._column = 0
                    self._line += 1
                    pass
                else:
                    self._column += len(token.Text)
                    pass
                return token
            self._priorities[i].restart()
            pass
        pass
    
    pass
