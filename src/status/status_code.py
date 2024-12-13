"""
status_code

here are defined the differnts status code
"""

from enum import Enum
from . import errors

Errors , ErrorType =  errors.Error , errors.ErrorType

class StatusCode(Enum):
    
    OK = 0
    ERROR = 1
    
    pass

class Status:

    """
    An abstraction from the status of the code compilation
    """
    
    def __init__(self,status=StatusCode.OK,error=None):
        self._status = status
        self._error = error
        pass
    
    def __str__(self):
        if self._status == StatusCode.ERROR:
            return str(self._error)
        return 'OK'
    
    def __repr__(self):
        return str(self)
    
    @property
    def status(self):
        return self._status
    
    @property
    def error(self):
        return self._error
    
    pass

class StatusOK(Status):
    
    """
    Represents a good code state compilation
    """
    
    def __init__(self):
        super().__init__(StatusCode.OK)
        pass
    
    pass

class StatusERROR(Status):
    
    """
    Represents a wrong state compilation
    """
    
    def __init__(self,error):
        super().__init__(StatusCode.ERROR,error)
        pass