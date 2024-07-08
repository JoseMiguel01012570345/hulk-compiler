"""
lexical

here's defined the lexical rules for the hulk language
"""

from enum import Enum
class ScapeChars(Enum):
    
    JumpLine = '\n'
    Tabulation = '\t'
    WhiteSpace = ' '
    
    pass
class TokenType(Enum):
    
    Keyword = 0
    Operator = 1
    Symbol = 2
    Variable = 3
    Number = 4
    Boolean = 5
    String = 6
    
    pass

class LexicalAnalyzer:
    
    """
    An abstraction of a lexical checker
    
    checkers: list of functions that returns true for a token if this check the rule corresponding
    
    """
    
    _string_delimeter = ''
    
    def __init__(self,string_delimeter,*checkers):
        self._checkers = checkers
        self._string_delimeter = string_delimeter
        pass
    
    @property
    def StringDelimeter(self):
        """
        returns the string delimeter for this instances of analyzer
        """
        return self._string_delimeter
    
    def Check(self,token):
        """
        returns true if the token checks all the rules
        """
        for rule in self._checkers:
            if not rule(token):
                return False
            pass
        return True
    
    pass

class HULKLexical(LexicalAnalyzer):
    
    def __init__(self):
        super().__init__('"',self.variable_rule)
        pass
    
    @staticmethod
    def variable_rule(token):
        if token.Type == TokenType.Variable:
            return not token.Text[0].isnumeric()
        return True
    
    @property
    def ErrorMessage(self):
        return 'Los nombres de variables no deben comenzar con numeros'
    
    pass