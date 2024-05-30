class IContext:
    """
    Class that define the code context
    """
    
    Context = {}
    
    def Exist(self,name):
        """
        Return true if name exists in the current context
        """
        
        return list(self.Context.keys()).count(name) > 0
    
    def TypeOf(self,name):
        """
        return the type of the object that 'name' represents
        """
        
        return self.Context['Type']
    
    def Push(self,**data):
        """
        push into the context the data contained into data
        """
        
        raise NotImplementedError()
    
    def UpdateContext(self,**data):
        """
        update the data of the object with the data into 'data'
        """
        
        raise NotImplementedError()
    
    pass

class VariableContext(IContext):
    
    def Push(self,**data):
        """
        data most be a tuple (name,type)
        """
        self.Context[data['name']] = data['type']
        pass
    
    # def UpdateContext
    
    pass