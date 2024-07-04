import production_class_representation as pcr

def binary_opt(self:pcr.binary_opt):
    return [ self.left_node , self.right_node ]

def var(self:pcr.variable):
    return [ None , self.value ]

def brackets(self:pcr.ASTNode):
    return [self.expression]

def replacement(self:pcr.ASTNode):
    return [self.replacement]

def let( self: pcr.ASTNode ):
    return [ None ,  self.value ]

def block( self: pcr.ASTNode ):
    if len(self.expressions) == 1:
        return [ None , self.expressions[0] ]
    else:
        return self.expressions 

def type(self: pcr.ASTNode):
    
    children = []
    
    if self.__dict__.__contains__("args"):
        children.append(self.args)
    if self.__dict__.__contains__("inheritence_args"):
        children.append(self.inheritence_args)
    
    children.append( self.body )
    
    return children

def protocol(self: pcr.ASTNode):
    
    children = [self.name]
    
    if self.__dict__.__contains__("inheritence_name"):
        children.append(self.inheritence_name)
    
    children.append(self.body)
    
    return children

def def_function(self: pcr.ASTNode):
    return [ self.args , self.body ]

def structure(self: pcr.ASTNode):
    return [ None , self.expressions ]

def function_call(self: pcr.ASTNode):
    return [ None , self.args ]