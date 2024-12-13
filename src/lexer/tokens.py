from copy import copy
from . import lexical 
TokenType = lexical.TokenType

class Token:
    
    def __init__(self,text,column,line,_type):
        self._text = text
        self._type = _type
        self._column = column
        self._line = line
        pass
    
    def __str__(self):
        return self._text

    def __repr__(self):
        return str((self._text,self._type))
    
    @property
    def line(self):
        return self._line
    
    @property
    def column(self):
        return self._column
    
    @property
    def Text(self):
        return self._text

    @property
    def Type(self):
        return self._type
    
    pass

class EOF(Token):
    
    """
    A token to represent the EOF character
    """
    
    def __init__(self,line,column):
        super().__init__('',column,line,TokenType.Symbol)
        pass
    
    pass
