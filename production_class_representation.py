import networkx as nx
from networkx import DiGraph

class ASTNode:
      
    parent = None
    derivation = []
    def_node = False
    builder = None
    visitor = None
    line = 10e306
    column =10e306
    expected_type = "any"
    node_type = "any"
    type_checker = False
    rules = []
    
    def check_rules(self):
        
        for rule in self.rules:
            rule(self)

        pass
        
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
    
    def type( self, graph:nx.DiGraph=None , referent_node=""):
        
        '''
        #### `<referent_node>` is the reference node of the actual node in `graph`
        '''
        pass

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
        return [ "name" , "args" ]
    
    def type(self, graph: DiGraph = None, referent_node=""):

        target_node = f"{referent_node}_def_function_{ self.name.name}"
        
        if not graph.has_node( target_node ):
            return 'any'
        
        target_node_ast:ASTNode = graph.nodes[target_node]["ASTNode"]
        return target_node_ast.type( graph ,  referent_node  )
    
class params( ASTNode):
    
    '''
    atributes of this class are
    > id : params
    
    '''
    expressions=[]
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def children_name(self):
        return [ "expressions" ]
    
    pass

#_________________________________________________BINARY EXPRESSIONS___________________________________________>>>>>>>>>>>>>>>>

class binary_opt(ASTNode):
    
    left_node = None
    right_node = None
    type_checker = True
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    
    def children_name(self):
        return [ "left_node" , "right_node" ]
    
    pass

class dot(binary_opt):# the context of the left side is passed to the context of the right side
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        return self.right_node.type( graph ,  referent_node  )
    
class in_(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    pass
    
    expressions = []
    body: ASTNode = None
    
    def children_name(self):
        return [ "args" , "body" ]
    
    def type(self, graph: DiGraph = None, referent_node=""):
        return self.body.type( graph ,  referent_node  )

class plus(binary_opt):
    
    expected_type = "Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
    
    pass
        
class minus(binary_opt):
    
    expected_type = "Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
        
    pass

class multiplication(binary_opt):
    
    expected_type = "Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
    
    pass

class divition(binary_opt):
    
    expected_type = "Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
        
    pass
    
class pow_(binary_opt):
    
    expected_type = "Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
        
    pass
    
class per_cent(binary_opt):
    
    expected_type = "Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)

    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type

    pass

class concatenation(binary_opt):
    
    expected_type = "String"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
        
    pass
      
class blank_space_concatenation(binary_opt):
    
    expected_type = "String"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)

    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
    
    pass

class double_dot(binary_opt): # the context of the right side is passed to the context of the left side
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)

    def type(self, graph: DiGraph = None, referent_node=""):
        
        right_node_type = self.right_node.type( graph ,  referent_node  )
        self.left_node.node_type = right_node_type
        
        return right_node_type
    
    pass

class double_dot_equal(binary_opt): # the context of the right side is passed to the context of the left side
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        right_node_type = self.right_node.type( graph ,  referent_node  )
        self.left_node.node_type = right_node_type
        
        return right_node_type
    
class as_(binary_opt):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        self.expected_type = self.right_node.name
        return self.right_node.type( graph ,  referent_node  )
    
    pass

class is_(binary_opt):
    
    expected_type = "Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
        
    pass

class equal(binary_opt): # the context of the right side is passed to the context of the left side
    
    expected_type = "Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
    
    
class bigger_than(binary_opt):
    
    expected_type = "Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
    
    pass

class smaller_than(binary_opt):
    
    expected_type = "Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
    
    pass

class bigger_or_equal(binary_opt):
    
    expected_type = "Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
    
    pass

class smaller_or_equal(binary_opt):
    
    expected_type = "Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
        
    pass

class assign(binary_opt):
    
    expected_type = "any"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        self.left_node.node_type = right_node_type
        
        return right_node_type
    
    
class or_(binary_opt):
    
    expected_type = "Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
        
    pass

class and_(binary_opt):
    
    expected_type = "Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
        
    pass
    
class different(binary_opt):
    
    expected_type = "Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def type(self, graph: DiGraph = None, referent_node=""):
        
        left_node_type = self.left_node.type( graph ,  referent_node  )
        right_node_type = self.right_node.type( graph ,  referent_node  )
        
        if left_node_type != right_node_type or right_node_type != self.expected_type or left_node_type != self.expected_type :
            return "any"
        
        else:
            return self.expected_type
    
    pass
 
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
    
    def type(self, graph: DiGraph = None, referent_node=""):
        
        node_type = self.node.type( graph ,  referent_node  )
        return node_type
    
    pass
    
class new(unary_expression):

    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def type(self, graph: DiGraph = None, referent_node=""):
        return self.node.name.name
    
    pass
    
class not_(unary_expression):
    
    expected_type = "Boolean"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
class plus_plus(unary_expression):
    
    expected_type = "Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
class minus_minus(unary_expression):
    
    expected_type = "Number"
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
     
#_____________________________________________________________________________________>>>>>>>>>>>>>>>
     
class let(ASTNode):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def type(self,graph: nx.DiGraph = None, referent_node=""):
        return "any"
        
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
    
    def __init__(self, grammar={ "derivation": "","identifier": "var"," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
        
    def children_name(self):
        return []
    
    def type(self, graph: nx.DiGraph = None, referent_node=""):
        
        if self.literal:
            return self.type_
        
        node_search = f"{referent_node}_var_{self.name}"
        neighborn_re_assigment = [ node for node in  graph.neighbors(node_search) if "re_assigment" in node ]
        
        if len(neighborn_re_assigment) == 0:
            
            let_node_ast = graph.nodes[f"{referent_node}_let_{self.name}"]["ASTNode"]
            
            return let_node_ast.node_type
        else:
            
            neighborn_re_assigment = neighborn_re_assigment[0]
            
            neighborn_re_assigment_ast = graph.nodes[neighborn_re_assigment]["ASTNode"]
            
            return neighborn_re_assigment_ast.node_type
        
    
class conditional(ASTNode):
    
    id = ""
    condition = None
    body = None
        
    def __init__(self, grammar={ "derivation": "","identifier": "","definition_node?": "","builder": None,"visitor": None }, *args) -> None:
        super().__init__(grammar, *args)
    
    def type(self , graph:nx.DiGraph , referent_node=""):
        return self.body.type( graph ,  referent_node  )

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
    name = None
    args = None
    body = None
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)    
    
    def children_name(self):
        
        children = []
        
        children.append("name")
        
        if self.args is not None:
            children.append("args")
        
        children.append("body")
        
        return children
    
    def type(self, graph:nx.DiGraph ,  referent_node=""):
        return self.body.type( graph ,  referent_node  )
    
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
    
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    
    def children_name(self):
        
        children = []
    
        if self.__dict__.__contains__("name"):
            children.append("name")
    
        if self.parent_name is not None:
            children.append("parent_name")
        
        if self.constructor is not None:
            children.append("constructor")
            
        if self.base is not None:
            children.append("base")

        if self.body is not None:
            children.append( "body" )
        
        return children
    
    def type(self, graph: DiGraph = None, referent_node=""):
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
    name = None
    parent_name = None
    body = None
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def children_name(self):
        children =[]
    
        if self.name is not None:
            children.append("name")
        
        if self.parent_name is not None:
            children.append("parent_name")
        
        if self.body is not None:
            children.append("body")
        
        return children
    
    def type( self ,graph: DiGraph = None, referent_node=""):
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
    
    def type(graph: DiGraph = None, referent_node=""):
        return "Iterable"
                  
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
    
    pass

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
        
    def type(graph: DiGraph = None, referent_node=""):
        return "any"
    
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
    
    def type(self,graph: DiGraph = None, referent_node=""):
        return self.body.type(graph , referent_node)
    
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
    
    def type(self, graph: DiGraph = None, referent_node=""):
        return self.body.type(graph , referent_node )
        
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
    
    def type(self, graph: DiGraph = None, referent_node=""):
        return self.expressions[-1].type(graph , referent_node)
  
  
  
class build_in:
    type_ = ""

class object(build_in):
    type_ = "object"

class Number(build_in):
    type_ = "Number"

class Boolean(build_in):
    type_ = "boolean"

class String(build_in):
    type_ = "string"

class cos(build_in):
    type_ = "Number"
    args=params

class cot(build_in):
    type_ = "Number"
    args=params

class exp(build_in):
    type_ = "Number"
    args=params

class log(build_in):
    type_ = "Number"
    args=params

class rand(build_in):
    type_ = "Number"
    args=params

class sqrt(build_in):
    type_ = "Number"
    args=params

class range(build_in):
    type_ = "Iterable"
    args=params

class tan(build_in):
    type_ = "Number"
    args=params

class sin(build_in):
    type_ = "Number"
    args=params

class e(build_in):
    type_ = "Number"

class PI(build_in):
    type_ = "Number"

class print(build_in):
    type_ = "String"
    args=params

class self:
    
    type=""
    
    def __init__(self,type) -> None:
        self.type = type
