import production_class_representation as pcr

def var(self:pcr.variable ):
    return [ ]

def binary_opt(self:pcr.variable ):
   
   children = [] 
   
   if self.left_node != None:
       children.append(self.left_node)
   
   if self.right_node != None:
       children.append(self.right_node)
    
   return children

def replacement(self:pcr.ASTNode ):
    
    children = []
    if self.replacement != None:
        children.append(self.replacement)
    
    return children
    
def block( self: pcr.ASTNode  ):
    
    if hasattr(self.expressions,"id"):
        return [ self.expressions ]
    
    return self.expressions
    
def type(self: pcr.ASTNode ):
    
    children = []
    
    if self.__dict__.__contains__("name"):
        children.append(self.name)
    
    if self.__dict__.__contains__("parent_name"):
        children.append(self.parent_name)
    
    if self.__dict__.__contains__("constructor"):
        children.append(self.constructor)
        
    if self.__dict__.__contains__("base"):
        children.append(self.base)

    if self.body != None:
        children.append( self.body )
    
    return children

def protocol(self: pcr.ASTNode ):
    
    children =[]
    
    if self.name != None:
        children.append(self.name)
    
    if self.__dict__.__contains__("parent_name"):
        children.append(self.parent_name)
    
    if self.body != None:
        children.append(self.body)
    
    return children

def def_function(self: pcr.ASTNode ):
   
   children = []
   
   if self.__dict__.__contains__("name"):
    children.append(self.name)
   
   if self.args != None:
    children.append(self.args)
   
   if self.body != None:
    children.append(self.body)
    
   return children

def function_call(self: pcr.ASTNode ):
   
    children =[]
    
    if self.name != None:
        children.append(self.name)
    
    if self.args != None:
       children.append(self.args)
   
    return children

def for_while(self:pcr.ASTNode):
    return [ self.args , self.body ]

def if_else(self:pcr.ASTNode):
    return [ self.args , self.body ]

def else_(self:pcr.ASTNode):
    return [ self.body ]
    
def conditional(self:pcr.ASTNode):
    return self.expressions

def unary_opt(self:pcr.ASTNode):
    return [self.right_node]

def ast_reducer(ast:pcr.ASTNode):
    
    reduced_ast = remove_child(ast=ast)
    
    reduced_ast = parent_reference(reduced_ast)
    
    return reduced_ast

def parent_reference(ast):
        
    list_children = ast.visitor_ast()
    
    for child in list_children:
        
        if child != None:
            
            child.parent = ast
            parent_reference(child)
                
            pass
        
        pass
    
    return ast

def remove_child(ast:pcr.ASTNode):

    children = ast.visitor_ast()
    
    for index,child in enumerate(children):
        
        if child == None:
            continue
        
        grand_son = child.visitor_ast()
        
        if len(grand_son) != 0:
            child = remove_child(child)
    
        reduce , num = reduce_node_condition(child)
        
        if reduce:
            
            children_name = ast.children_name()
            
            if children_name[0] == "expressions" :
                node_out = ""
            
            else:
                node_out = children_name[index]
            
            if num == 1:
                
                if children_name[0] == "expressions":
                    
                    new_node = child.visitor_ast()[0]
                    
                    ast.__dict__["expressions"][index] = new_node    
                    
                    continue
                
                new_node = child.visitor_ast()[0]
                ast.__dict__[node_out] = new_node  # because this child has only one son
            else:
                ast.__dict__[node_out] = None # because this child has only one son
            
            pass
        
            pass
    
    return ast

def non_reduce_node(id):
    
    nodes = [
            "literal" ,
             "protocol" ,
             "function_call",
             "def_function",
             "type",
             "var",
             "let",
             "if",
             "for",
             "while",
             "else",
             "elif"
             "new",
             "!",
             "++",
             "--",
             "args"
             ]
    
    return any( x == id for x in nodes )

def reduce_node_condition(child:pcr.ASTNode) -> bool:
    
    children = child.visitor_ast()
    
    if len(children) == 1 and children[0] != None and not non_reduce_node(child.id) :
        return True , 1

    if len(children) == 0 and not non_reduce_node(child.id):
        return True , 2

    return False , 3

