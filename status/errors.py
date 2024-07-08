"""
errors

the errors definitions
"""

from enum import Enum

class ErrorType(Enum):
    
    LEXICAL = 0
    SYNTAX = 1
    SEMANTIC = 2
    
    pass

class Error:

    """
    Represents an abstraction for the error
    """
    
    def __init__(self,message,_type,line,column):
        self._type = _type
        self._message = message
        self._line = line
        self._column = column
        pass
    
    def __str__(self):
        return f'{self._type} Error at line {self._line}, column {self._column}. {self._message}'
    
    def __repr__(self):
        return str(self)
    
    @property
    def Type(self):
        """
        returns the error type
        """
        return self._type
    
    @property
    def Message(self):
        """
        returns a brief description of the error
        """
        return self._message
    
    pass