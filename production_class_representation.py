import networkx as nx

class ASTNode:
      
    parent = None
    derivation = []
    def_node = False
    builder = None
    visitor = None
    line = 10e306
    column =10e306
    
    
    def __init__(
        self, grammar= {
                        
                        "derivation":"",
                        "identifier":"" ,
                        "definition_node?":"" , 
                        "builder":None , 
                        "visitor":None
                    }, *args ) -> None:
        
        self.set_identifier(grammar["identifier"])
        self.derivation = grammar["derivation"]
        self.def_node = grammar["definition_node?"]
        self.builder = grammar["builder"]
        self.visitor = grammar["visitor"]
        
        pass
    
    def children_name(self):
        return ["replacement"]
    
    def visitor_ast(self):
        return self.visitor(self)
            
    def ignition(self,token_list):
        
        attributes = self.builder(token_list)
        
        for property in attributes: # property: ( property_name , property_value)
            self.__dict__[property[0]] = property[1]
        
        for token in token_list:
           
           if self.line > token.line:
            self.line = token.line 
            self.column = token.column

        return self
        
    def my_id(self):
        
        if self.definition_node():
            return { 'id': self.id  , 'name': self.name  }
    
    def set_identifier(self,id_:str):  
        
        self.id = id_
        
        return self.id
    
    def type( self, graph:nx.DiGraph=None ):
        pass

#___________________________________________________AST OF THE GRAMMAR_________________________________________>>>>>>>>>>>>>>>>

class function_call( ASTNode): # check context

    '''
    atributes of this class are:
    
    > id
    > name
    > args
    
    '''
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def children_name(self):
        return [ "name" , "args" ]
    
    def type(self):
        return super().type()
    
class params( ASTNode):
    
    '''
    atributes of this class are
    > id : params
    
    '''
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def children_name(self):
        return [ "expressions" ]
                
    pass

#_________________________________________________BINARY EXPRESSIONS___________________________________________>>>>>>>>>>>>>>>>

class binary_opt(ASTNode):
    
    left_node = []
    right_node = []
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    
    def children_name(self):
        return [ "left_node" , "right_node" ]
    
    pass

class dot(binary_opt):# the context of the left side is passed to the context of the right side
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def context_check(self, error_list: list):
        
        left_id = self.left_node.id
        
        if self.left_node.__dict__["name"] == None:
            ## error
            
            error_type = ""
            error_description = ""
            error_list.append({ "type":error_type , "description":error_description })
            
            return error_list
            
        
        left_name = self.left_node.name
        
        # completar el metodo , este debe buscar en left_node lo que esta en rigth_node
        
        
        pass
    
    def check_right_side_context(self, type_name , attr_name , attr_id ):
        
        
        
        found_attr = False
        parent_node = self

        while not found_attr:
            
            if ASTNode(parent_node).__dict__["parent"] != None:
                parent_node = ASTNode(parent_node).parent
            
            else:
                return False
            
            if parent_node.__dict__["name"]:
                found_attr = type_name == parent_node.__dict__["name"]
            
        pass
    
        for item in type_(parent_node).body:
            
            if ASTNode(item).id == attr_id and ASTNode(item).__dict__["name"] == attr_name:
                return True
        
        return False

class in_(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass
    
    def children_name(self):
        return [ "args" , "body" ]

class plus(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass
        
class minus(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    pass

class multiplication(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass

class divition(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    pass
    
class pow_(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    pass
    
class per_cent(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)

    pass

class concatenation(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    pass
      
class blank_space_concatenation(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)

    pass

class double_dot(binary_opt): # the context of the right side is passed to the context of the left side
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)

    def context_check(self, error_list: list):
        
        for item in self.context:
            
            if (item['id'] == 'type' or item['id'] == 'protocol') and item['name'] == self.right.name:
                return error_list                
            
        for item in self.build_in:
            
            if (item['id'] == 'type' or item['id'] == 'protocol') and item['name'] == self.right.name:
                return error_list                
            
        return error_list

    pass

class double_dot_equal(binary_opt): # the context of the right side is passed to the context of the left side
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass

class as_(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    pass

class is_(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    pass

class equal(binary_opt): # the context of the right side is passed to the context of the left side
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def infer_type(self,error_list:list):
        
        if self.left_node.id != "let":
            
            error_type = "assignment"
            error_description = "unexpected use of \"=\" , you only can use \"=\" with let statement"
            error_list.append( { "type": error_type , "description": error_description } )
            return error_list
        
        variable(unary_expression(self.left_node).right).type_ = ASTNode(self.right_node).type_
    
        return error_list
    
class bigger_than(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass

class smaller_than(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass

class bigger_or_equal(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass

class smaller_or_equal(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass

class assign(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass
    
class or_(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass

class and_(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass
    
class different(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass

class divide_and_assign(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass
    
class multiply_and_assign(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass

class plus_and_assign(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass

class minus_and_assign(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass
 
#______________________________________________________UNARY EXPRESSIONS_______________________________>>>>>>>>>>>>>>>
    
class unary_expression(ASTNode):
    
    '''
    this class selects the kind of binary expression the token_list refers to. Every
    class in this class has as attributes:
    
    > id : the kind of expression it is specified by its symbol
    > right: right unary member
    
    '''
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def children_name(self):
        return [ "right" ]
    
    pass
    
class new(unary_expression):

    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass
    
class not_(unary_expression):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
class plus_plus(unary_expression):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
class minus_minus(unary_expression):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
     
#_____________________________________________________________________________________>>>>>>>>>>>>>>>
     
class let(ASTNode):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def type(self):
        return "unknow"
        
class variable(ASTNode): # check context
    
    '''
    this class has the attributes:
    
    > id : var
    > name: name of the variable
    
    '''
    
    id = ""
    name = ""
    
    def __init__(self, grammar={ "derivation": "","identifier": "var"," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
        
    def children_name(self):
        return []
    
    def type(self, graph: nx.DiGraph = None):
        
        start_node = f"var_{self.name}"
        end_node = f"let_{self.name}"
        
        if nx.has_path( graph , start_node , end_node):
            return 
        
        pass    
    
class conditional(ASTNode):
    
    id = ""
    condition = ASTNode
    body = ASTNode
        
    def __init__(self, grammar={ "derivation": "","identifier": "","definition_node?": "","builder": None,"visitor": None }, *args) -> None:
        super().__init__(grammar, *args)
    
    def type(self):
        return self.body.type()

class if_(conditional):
    
    '''
    this class has the attributes:
    
    > id : if
    > condition : condition for if statement
    > body: body of the statement
    
    '''
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def children_name(self):
        return [ "condition" , "body" ]

class elif_(conditional):
    
    '''
    this class has the attributes:
    
    > id : elif
    > condition : condition for elif statement and the condition for the if statement , the condition is a list
    > body: body of the statement
    
    NOTE:
    
    The condition is a list that refers to if statement , and has second element has the elif statement
    
    '''
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
        
    pass

    def children_name(self):
        return [ "condition" , "body" ]

class else_(conditional):
    
    
    '''
    this class has the attributes:
    
    > id : else
    > condition : condition for else is the condition for the if statement and condition for the
                elif statement, the condition is a list that refers to elif
    > body: body of the statement
    NOTE:
    
    the condition is a list to refers to elif statement , in case it exists , or tho the if statement in worst case
    
    '''
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
        
    def children_name(self):
        return [ "body" ]
    
class def_function(ASTNode): # check context
    
    '''
    atributes of this class are:
    
    > id : function_form
    > name: name of the function declared
    > args
    > body
    
    '''
    id = ""
    name = ASTNode
    args = ASTNode
    body = ASTNode
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)    
    
    def children_name(self):
        
        children = []
        
        if self.__dict__.__contains__("name"):
            children.append("name")
        
        if self.__dict__.__contains__("args"):
            children.append("args")
        
        children.append("body")
        
        return children
    
    def type(self):
        return self.body.type()
    
class type_(ASTNode): # check context
    
    '''
    atributes of this class are:
    
    > id : type
    > name: name of the type
    > constructor: constructor params
    > parent_name: the name of the class this class inherits from
    > base: parents constructor
    > body
    
    '''
    name = ASTNode
    constructor = ASTNode
    parent_name = ASTNode
    base = ASTNode
    body = ASTNode
    
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    
    def children_name(self):
        
        children = []
    
        if self.__dict__.__contains__("name"):
            children.append("name")
    
        if self.__dict__.__contains__("parent_name"):
            children.append("parent_name")
        
        if self.__dict__.__contains__("constructor"):
            children.append("constructor")
            
        if self.__dict__.__contains__("base"):
            children.append("base")

        if self.body != None:
            children.append( "body" )
        
        return children
    
    def type(self):
        return self.name.name
            
class protocol(ASTNode): # check context
    
    '''
    atributes of this class are:
    
    > id : protocol
    > name: name of the type
    > parent_name: the name of the class this class inherits from
    > body
    
    '''
    id = ""
    name = ASTNode
    parent_name = ASTNode
    body = ASTNode
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def children_name(self):
        children =[]
    
        if self.name != None:
            children.append("name")
        
        if self.__dict__.__contains__("parent_name"):
            children.append("parent_name")
        
        if self.body != None:
            children.append("body")
        
        return children
    
    def type(self):
        return self.name.name
    
class vectors(ASTNode):
    
    '''
    
    vector form: 
    1. [ filter || domain ]
    2. [ 1,2,3,4, ... ]
    
    attributes:
    
    > filter_ : the filter of a vector
    > domain: the domain of a vector
    
    '''

    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def type(self):
        return "Iterable"
                  
class literal(ASTNode):
    
    '''
    attributes:
    
    > id: literal
    > value: value of the literal
    
    '''
    
    value = None
    type = None
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def children_name(self):
        return []
    
    def type(self):
        return self.type
    
    pass

class index(ASTNode): # check context
    
    '''
    attributes:
    
    > id : index
    > name: name of the indexation vector
    > index : index of the vector 
    
    '''
    
    args = ASTNode
    name = ASTNode
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
        
    def type(self):
        return "unknow"
    
class while_(ASTNode):
    
    '''
    attributes:
    
    > id : while
    > condition : condition of the while loop
    > body
    
    '''
    
    condition = ASTNode
    body = ASTNode
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
        
    def children_name(self):
        return [ "args" , "body" ]
    
    def type(self):
        return self.body.type()
    
class for_(ASTNode):
    
    '''
    attributes:
    
    > id : for
    > condition : condition of the for loop
    > body
    
    '''
    
    condition = ASTNode
    body = ASTNode
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def children_name(self):
        return [ "args" , "body" ]
    
    def type(self):
        return self.body.type()
    
class block(ASTNode):
    
    '''
    attributes:
    
    > id : block
    > expressions : expressions inside of the block
    
    >> solve from left to right
    
    '''
    
    expressions = []
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)

    def children_name(self):
        return ["expressions"]
    
    def type(self):
        return self.expressions[-1].type_checking()
        
    