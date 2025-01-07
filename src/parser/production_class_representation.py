import networkx as nx
from networkx import DiGraph
from ..risk import risk
import inspect

class ASTNode:
      
    parent = None
    derivation = []
    def_node = False
    builder = None
    visitor = None
    line = 10e306
    column =10e306
    expected_type = "type_Object"
    node_type = "type_Object"
    type_checker = False
    rules = []
    referent_node = ''
    
    def check_rules(self):
        
        for rule in self.rules:
            rule(self)

    def __init__(
        self, grammar= {
                        
                        "derivation":"",
                        "identifier":"" ,
                        "definition_node?":"" , 
                        "builder":None , 
                        "visitor":None
                    } ) -> None:
    
        self.set_identifier(grammar["identifier"])
        self.derivation = grammar["derivation"]
        self.def_node = grammar["definition_node?"]
        self.builder = grammar["builder"]
        self.visitor = grammar["visitor"]
        
    def pointer_to_node_type(self):
        return self.node_type
    
    def children_name(self):
        return ["replacement"]
    
    def visitor_ast(self):
        '''
        return the children of the current node
        '''
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
    
    def type( self, graph:nx.DiGraph=None):
        
        '''
        #### `<referent_node>` is the reference node of the actual node in `graph`
        '''
        return self.pointer_to_node_type()
#___________________________________________________AST OF THE GRAMMAR_________________________________________>>>>>>>>>>>>>>>>

class function_call( ASTNode): # check context

    '''
    atributes of this class are:
    
    > id
    > name
    > args
    
    '''
    name=""
    args=""
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def children_name(self):
        return [ "args" ]
    
    @risk.log_state_on_error
    def type(self, graph: nx.DiGraph = None ):
        risk.frame_logger.append( inspect.currentframe()) # add frame to  frame_logger
        
        target = f"{ self.referent_node }_{self.id}_{self.name}"
        if not graph.has_node(target):
            return 'Object'
        
        func_call_neighbor = next(graph.neighbors(target))
        
        def_function_ast = None
        if func_call_neighbor is not None:
            def_function_ast = graph.nodes[func_call_neighbor]["ASTNode"]
            
            return def_function_ast.type(graph=graph)
        
        self.node_type = 'type_Object'
        return self.pointer_to_node_type()
    
class params( ASTNode):
    
    '''
    atributes of this class are
    > id : params
    
    '''
    expressions=[]
    parent_constructor = False
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def children_name(self):
        return [ "expressions" ]
    
#_________________________________________________BINARY EXPRESSIONS___________________________________________>>>>>>>>>>>>>>>>

class binary_opt(ASTNode):
    
    left_node = None
    right_node = None
    type_checker = True
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    
    def children_name(self):
        return [ "left_node" , "right_node" ]
    
class dot(binary_opt):# the context of the left side is passed to the context of the right side
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        return self.right_node.type( graph )
    
class in_(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    expressions = []
    body: ASTNode = None
    
    def children_name(self):
        return [ "args" , "body" ]
    
    def type(self, graph: DiGraph = None):
        return self.body.type( graph   )

class plus(binary_opt):
    
    expected_type = "type_Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()
        
class minus(binary_opt):
    
    expected_type = "type_Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()

class multiplication(binary_opt):
    
    expected_type = "type_Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()

class divition(binary_opt):
    
    expected_type = "type_Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()
    
class pow_(binary_opt):
    
    expected_type = "type_Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()
    
class per_cent(binary_opt):
    
    expected_type = "type_Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)

    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()

class concatenation(binary_opt):
    
    expected_type = "String"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()
      
class blank_space_concatenation(binary_opt):
    
    expected_type = "String"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)

    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()

class double_dot_equal(binary_opt): # the context of the right side is passed to the context of the left side
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        right_node_type = self.right_node.type( graph   )
        self.left_node.node_type = right_node_type
        
        self.node_type = right_node_type
        
        return self.pointer_to_node_type()
    
class as_(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        self.expected_type = self.right_node.name
        return self.right_node.type( graph   )

class is_(binary_opt):
    
    expected_type = "type_Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()

class equal(binary_opt): # the context of the right side is passed to the context of the left side
    
    expected_type = "type_Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()
    
    
class bigger_than(binary_opt):
    
    expected_type = "type_Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()

class smaller_than(binary_opt):
    
    expected_type = "type_Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()

class bigger_or_equal(binary_opt):
    
    expected_type = "type_Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()

class smaller_or_equal(binary_opt):
    
    expected_type = "type_Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()

class assign(binary_opt):
    
    expected_type = "type_Object"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        return self.pointer_to_node_type()
        
class or_(binary_opt):
    
    expected_type = "type_Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()

class and_(binary_opt):
    
    expected_type = "type_Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type()
    
class different(binary_opt):
    
    expected_type = "type_Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def type(self, graph: DiGraph = None):
        
        left_node_type = self.left_node.type( graph   )
        right_node_type = self.right_node.type( graph   )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            self.node_type = "type_Object"
            return self.pointer_to_node_type()
        
        else:
            self.node_type = self.expected_type
            return self.pointer_to_node_type() 
#______________________________________________________UNARY EXPRESSIONS_______________________________>>>>>>>>>>>>>>>
    
class unary_expression(ASTNode):
    
    '''
    this class selects the kind of binary expression the token_list refers to. Every
    class in this class has as attributes:
    
    > id : the kind of expression it is specified by its symbol
    > node: right unary member
    
    '''
    node:ASTNode = None
    type_checker = True
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def children_name(self):
        return [ "right" ]
    
    def type(self, graph: DiGraph = None):
        return self.pointer_to_node_type()
    
    
class new(unary_expression):

    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None):
        return self.pointer_to_node_type()
    
class not_(unary_expression):
    
    expected_type = "type_Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
class plus_plus(unary_expression):
    
    expected_type = "type_Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
class minus_minus(unary_expression):
    
    expected_type = "type_Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
     
#_____________________________________________________________________________________>>>>>>>>>>>>>>>
     
class let(ASTNode):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def type(self,graph: nx.DiGraph = None, ):
        return self.pointer_to_node_type()

@risk.log_state_on_error
class variable(ASTNode): # check context
    
    '''
    this class has the attributes:
    
    > id : var
    > name: name of the variable
    
    '''
    
    id = ""
    name = ""
    value = None
    type_ = None
    literal = False
    \
    def __init__(self, grammar={ "derivation": "","identifier": "var"," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
        
    def children_name(self):
        return []
    
    @risk.log_state_on_error
    def type(self, graph: nx.DiGraph = None ):
        risk.frame_logger.append( inspect.currentframe()) # add frame to  frame_logger
        
        if self.literal:
            return self.pointer_to_node_type()
        
        if self.id == 'let':
            return self.pointer_to_node_type()
        
        # simple variable case ( id == var )
        target = f"{ self.referent_node }_{self.id}_{self.name}"
        if not graph.has_node(target):
            return 'type_Object'
        
        var_neighbor = next(graph.neighbors(target))
            
        let_node_ast = None
        if var_neighbor is not None:
            let_node_ast = graph.nodes[var_neighbor]["ASTNode"]
            
            return let_node_ast.type(graph=graph)
        
        self.node_type = 'type_Object'
        return self.pointer_to_node_type()
        
class conditional(ASTNode):
    
    id = ""
    condition = None
    body = None
        
    def __init__(self, grammar={ "derivation": "","identifier": "","definition_node?": "","builder": None,"visitor": None }, *args) -> None:
        super().__init__(grammar, *args)
    
    def type(self , graph:nx.DiGraph ):
        return self.body.type( graph  )

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
    name = None
    args = None
    body = None
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)    
    
    def children_name(self):
        
        children = []
        
        if self.args is not None:
            children.append("args")
        
        children.append("body")
        
        return children
    
    def type(self, graph:nx.DiGraph   ):
        if self.body is not None:
            return self.body.type( graph  )
        
        return self.pointer_to_node_type()
    
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
    name = None
    constructor = None
    parent_name = None
    base = None
    body = None
    node_type = name
    
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    
    def children_name(self):
        
        children = []
    
        if self.constructor is not None:
            children.append("constructor")
            
        if self.base is not None:
            children.append("base")

        if self.body is not None:
            children.append( "body" )
        
        return children
    
    def type(self, graph: DiGraph = None):
        self.node_type = self.referent_node
        return self.pointer_to_node_type()
            
class protocol(ASTNode): # check context
    
    '''
    atributes of this class are:
    
    > id : protocol
    > name: name of the type
    > parent_name: the name of the class this class inherits from
    > body
    
    '''
    id = ""
    name = None
    parent_name = None
    body = None
    node_type = name
    
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def children_name(self):
        children =[]
    
        if self.body is not None:
            children.append("body")
        
        return children
    
    def type( self ,graph: DiGraph = None, ):
        self.node_type = self.referent_node
        return self.pointer_to_node_type()
    
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
    
    def type( self, graph: DiGraph = None, ):
        self.node_type = "Iterable"
        return self.pointer_to_node_type()
                  
class literal(ASTNode):
    
    '''
    attributes:
    
    > id: literal
    > value: value of the literal
    
    '''
    
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def children_name(self):
        return []
    
class index(ASTNode): # check context
    
    '''
    attributes:
    
    > id : index
    > name: name of the indexation vector
    > index : index of the vector 
    
    '''
    
    args = None
    name = None
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
        
    def type( self, graph: DiGraph = None, ):
        self.node_type = "type_Object"
        return self.pointer_to_node_type()
    
class while_(ASTNode):
    
    '''
    attributes:
    
    > id : while
    > condition : condition of the while loop
    > body
    
    '''
    
    condition = None
    body = None
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
        
    def children_name(self):
        return [ "args" , "body" ]
    
    def type(self,graph: DiGraph = None ):
        return self.body.type(graph)
    
class for_(ASTNode):
    
    '''
    attributes:
    
    > id : for
    > condition : condition of the for loop
    > body
    
    '''
    
    condition = None
    body = None
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def children_name(self):
        return [ "args" , "body" ]
    
    def type(self, graph: DiGraph = None):
        return self.body.type( graph )
        
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
    
    def type(self, graph: DiGraph = None):
        return self.expressions[-1].type( graph )
  
  
  
class build_in:
    
    expected_type = 'type_Object'
    node_type = 'type_Object'
    
    def __init__(self):
        pass
    
    def type(self,graph):
        return self.pointer_to_node_type()
    
    def pointer_to_node_type( self ):
        return self.node_type.node_type
    
class buil_in_params:

    expressions=[]
    
    def __init__(self , param_type:list):
        
        types = []
        for type in param_type:
            
            ast_node = ASTNode()
            ast_node.expected_type =type.expected_type
            ast_node.node_type = type.expected_type
            
            types.append( ast_node )
        
        self.expressions = [ type for type in types]
        
    def children_name(self):
        return [ "expressions" ]
        
class Object(build_in):
    id = 'type'
    expected_type = 'type_Object'
    node_type = 'type_Object'

class Number(build_in):
    id = 'type'
    expected_type = 'type_Number'
    node_type = 'type_Number'

class Boolean(build_in):
    id = 'type'
    expected_type = 'type_Boolean'
    node_type = 'type_Boolean'

class String(build_in):
    id = 'type'
    expected_type= "type_String"
    node_type= "type_String"

class Iterable(build_in):
    id = 'type'
    expected_type= "type_Iterable"
    node_type= "type_Iterable"

class cos(build_in):
    id = 'def_function'
    expected_type = Number
    node_type = Number
    args=buil_in_params( [ Number ] )

class cot(build_in):
    id = 'def_function'
    expected_type = Number
    node_type = Number
    args=buil_in_params( [ Number ] )
    
class exp(build_in):
    id = 'def_function'
    expected_type = Number
    node_type = Number
    args=buil_in_params( [ Number ] )
    
class log(build_in):
    id = 'def_function'
    expected_type = Number
    node_type = Number
    args=buil_in_params( [ Number ] )
    
class rand(build_in):
    id = 'def_function'
    expected_type = Number
    node_type = Number
    args=buil_in_params( [ Number  , Number ] )
    
class sqrt(build_in):
    id = 'def_function'
    expected_type = Number
    node_type = Number
    args=buil_in_params( [ Number ] )
    
class range(build_in):
    id = 'def_function'
    expected_type = Iterable
    node_type = Iterable
    args=buil_in_params( [ Number  , Number ] )
    
class tan(build_in):
    id = 'def_function'
    expected_type = Number
    node_type = Number
    args=buil_in_params( [ Object ] )
    
class sin(build_in):
    id = 'def_function'
    expected_type = Number
    node_type = Number
    args=buil_in_params( [ Number ] )

class e(build_in):
    id = 'let'
    expected_type = Number
    node_type = Number
    
class PI(build_in):
    id = 'let'
    expected_type = Number
    node_type = Number

class print(build_in):
    id = 'def_function'
    expected_type = String
    node_type = String
    args=buil_in_params( [ Object ] )
    
class self(ASTNode):
    
    expected_type = Object
    node_type = Object
    
    def __init__(self, node:ASTNode ) -> None:
        for key, value in node.__dict__.items():
            setattr(self, key, value)