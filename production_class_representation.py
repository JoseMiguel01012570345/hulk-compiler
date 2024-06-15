#____________________________________________________________________________________________>>>>>>>>>>>>>>>>

class ASTNode:
      
    build_in = [
                {'id': 'let'           , 'name': 'Object'  } ,
                {'id': 'let'           , 'name': 'Number'  } ,
                {'id': 'let'           , 'name': 'String'  } ,
                {'id': 'let'           , 'name': 'Boolean' } ,
                {'id': 'type'          ,'name':  'Object'  } ,
                {'id': 'type'          ,'name':  'Number'  } ,
                {'id': 'type'          ,'name':  'String'  } ,
                {'id': 'type'          ,'name':  'Boolean' } ,
                {'id': 'function_form' ,'name':  'tan'     } ,
                {'id': "function_form" ,'name':  'cot'     } ,
                {'id': "function_form" ,'name':  'sqrt'    } ,
                {'id': "function_form" ,'name':  'sin'     } ,
                {'id': "function_form" ,'name':  'cos'     } ,
                {'id': "function_form" ,'name':  'log'     } ,
                {'id': "function_form" ,'name':  'exp'     } ,
                {'id': "function_form" ,'name':  'rand'    } ,
                {'id': "function_form" ,'name':  'range'   } ,
                {'id': "function_form" ,'name':  'print'   } ,
                {'id': "let"           , 'name': 'E'       } ,
                {'id': "let"           , 'name': 'PI'      } ,
                {'id': "let"           , 'name': 'self'    }
                ]
    anotated_type = None
    hash_ = 0
    parent = None
    derivation = []
    context = []
    def_node = False
    builder = None
    visitor = None
    name = ""
    type_ = ""
    self_ = ""
    
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
    
    def ast_reducer(self):
        
        children = self.visitor(self)
        
        if len(children) == 1 and children[0] != None:
            self = children[0]
            self.ast_reducer()
        
        pass
    
    def ignition(self,token_list):
        
        attributes = self.builder(token_list)
        
        for property in attributes: # property: ( property_name , property_value)
            self.__dict__[property[0]] = property[1]
        
        self.ast_reducer()
            
        self.parent_reference()
        
        return self
    
    def parent_reference(self):
        
        list_children = self.visitor(self)
        
        for child in list_children:
            
            if child != None:
                child.parent = self
                
                pass
        
            pass
        
    def my_id(self):
        
        if self.definition_node():
            return { 'id': self.id  , 'name': self.name  }
    
    def set_identifier(self,id_:str):  
        
        self.id = id_
        
        return self.id
    
    def check_children(self,error_list):
        
        children = self.visitor(self)    
            
        for child in children:
                
            if child != None:
                ASTNode(child).context_check(error_list)    
    
    def context_checker(self, node_id , error_list:list , error_type , error_description, allow_apparence , name ,type_name= None):
        
        # falta determinar que nodos hacen este analisis, porque no todos los nodos deben hacerlo, en especial nodos como "varibles" y declaracion de: "funciones" , "types" , "protocols" y "let"
        node_exists = self.search_in_ast( name , node_id, type_name=type_name )
        
        if node_exists and allow_apparence:
        
            self.check_children(error_list)
            pass    
        
        else:
            
            error_ = { "type" : error_type , "description" : error_description }
            error_list.append(error_)
        
        return error_list
    
    def search_in_ast(self , attr_name , attr_id , type_name= None ) -> bool:
        
        parent_node = self

        while True:
            
            if ASTNode(parent_node).__dict__["parent"] != None:
            
                parent_node = ASTNode(parent_node).parent
                
                if type_name != None:
                    
                    if parent_node.__dict__["name"] == None : 
                        continue
                    if parent_node.name != type_name:
                        continue
                    
                for item in type_(parent_node).body:
            
                    if ASTNode(item).id == attr_id and ASTNode(item).__dict__["name"] == attr_name:
                        return True
            
            else:
                return False
        
    def infer_type(self,error_list:list):
        pass
      
    def type_checking(self):
        pass        
    
    def cil_node_code(self):
        """
        return CIL codes

        """
        pass

#___________________________________________________AST OF THE GRAMMAR_________________________________________>>>>>>>>>>>>>>>>

class function_call( ASTNode): # check context

    '''
    atributes of this class are:
    
    > id
    > name
    > args
    
    '''
    name = ""
    args = []
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
    def context_check(self,error_list):
        
        for item in self.context:
            
            if item['id'] == 'function_form' and item['name'] == self.name:
                
                super().context_check( error_list= error_list )
                return error_list
        
        for item in self.build_in:
        
            if item['id'] == 'function_form' and item['name'] == self.name:
                
                super().context_check( error_list= error_list )
                return error_list
        
        error_type = "function undefined"
        error_decription = f"function {self.name} could not be found"
        scope = self.context
        error_list.append({'type': error_type, 'description': error_decription, 'scope':scope})
        
        super().context_check( error_list= error_list )
        
        return error_list
    
    def type_checking(self):
        return super().type_checking()
    
class params( ASTNode):
    
    '''
    atributes of this class are
    > id : params
    > parameters
    
    '''
    
    parameters = []
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
                
    pass

#_________________________________________________BINARY EXPRESSIONS___________________________________________>>>>>>>>>>>>>>>>

class binary_opt(ASTNode):
    
    left_node = []
    right_node = []
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
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
    
    def retrive_var_context(self,node:ASTNode):
    
        try:
            if node.id == '=' and node.left.id == ':':
                return { 'id': 'let', 'name': node.left.left.name }
            
            elif node.id == '=' and node.left.id == 'let':
                return { 'id': 'let', 'name': node.left.name }
            
            elif node.id == ':' and node.left.id == 'let':
                return { 'id': 'let', 'name': node.left.name }
            
            elif node.id == 'let':
                return { 'id': 'let', 'name': node.name }
        
        except:    
            return None
        
        return None

    def create_context(self,args_AST:list):
        
        params_context = []
        
        if args_AST.id == 'in':
            params_context = [ item for item in self.create_context(args_AST.left) ]    
            return params_context
        
        if args_AST.id == 'params':
            
            args_AST = args_AST.parameters
            
            for param in args_AST:
                
                var = self.retrive_var_context(param)
                if var != None:
                    params_context.append(var)
            
        else:
            arg = self.retrive_var_context(args_AST)
            
            if arg != None:
                params_context.append( arg )
        
        return params_context

    def send_context(self):
        
        new_context = [ item for item in self.context ]
        params_context = self.create_context(args_AST= self)
        
        self.left.context = self.merge_context(params_context,new_context)
        self.left.send_context()
        
        right_context = self.merge_context(params_context,new_context)
        
        self.right.context = right_context
        self.right.send_context()
        
        pass
    
    def merge_context(self,context1,context2):
        
        result_context = [  ]
        for item in context2:
            
            result_context.append(item)
        
        for item in context1:
            
            if self.equal(item,result_context):
                continue
            
            result_context.append(item)
        
        return result_context
        
    def equal(self,node1,new_context):
    
        if node1 == None : return False
        
        return any( lambda item: node1['id'] == item['id'] and node1['name'] == item['name'] , new_context )

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
    right= []
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def builder(self, token_list):
        self.right = token_list[1][1]
        pass
    
    def visitor(self):
        return [self.right]
    
    pass
    
class new(unary_expression):

    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
        
    def context_check(self, error_list: list):
        
        for item in self.context:
        
            if (item['id'] == 'type' or item['id'] == 'protocol')  and item['name'] == self.right.name:
                return error_list
        
        error_type = 'undefined type'
        error_description = f"The type {self.right.name} is not defined or visible for new keyword"
        scope = self.context
        
        error_list.append({'type':error_type,'description':error_description,'scope':scope})
        
        return error_list
    
    pass
    
class let(unary_expression):
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": "","visitor": "" }) -> None:
        super().__init__(grammar)
    
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
     
class variable(ASTNode): # check context
    
    '''
    this class has the attributes:
    
    > id : var
    > name: name of the variable
    
    '''
    def __init__(self, grammar={ "derivation": "","identifier": "var"," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def context_check(self,error_list):
        
        for item in self.context:
            
            if item['id'] == 'let' and item['name'] == self.name :
                return error_list
            
        for item in self.build_in:
        
            if item['id'] == 'let' and item['name'] == self.name : # this variable is E , Pi or self
                return error_list
        
        if self.parent.def_node: return error_list # this variable is being defined
        
        error_type = "variable undefined"
        error_description = f"variable {self.name} could not be found"
        scope = self.context
        error_list.append({ "type": error_type, "description": error_description, "scope": scope})
        
        return error_list

class if_(ASTNode):
    
    '''
    this class has the attributes:
    
    > id : if
    > condition : condition for if statement
    > body: body of the statement
    
    '''
    condition = [] 
    body = []
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)

class elif_(ASTNode):
    
    '''
    this class has the attributes:
    
    > id : elif
    > condition : condition for elif statement and the condition for the if statement , the condition is a list
    > body: body of the statement
    
    NOTE:
    
    The condition is a list that refers to if statement , and has second element has the elif statement
    
    '''
    condition=None
    body = None
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
        
    pass

class else_(ASTNode):
    
    
    '''
    this class has the attributes:
    
    > id : else
    > condition : condition for else is the condition for the if statement and condition for the
                elif statement, the condition is a list that refers to elif
    > body: body of the statement
    
    
    NOTE:
    
    the condition is a list to refers to elif statement , in case it exists , or tho the if statement in worst case
    
    '''
    
    condition = None
    body = None
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)

class def_function(ASTNode): # check context
    
    '''
    atributes of this class are:
    
    > id : function_form
    > name: name of the function declared
    > args
    > body
    
    '''
    
    name = None
    args = None
    body = None
        
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)    
    
    def context_check(self,error_list):
        
        for item in self.context:
            
            if item['id'] == self.id and item['name'] == self.name:
                
                error_type = "Function definition"
                error_decription = f"The function {self.name} has been already defined"
                scope = self.context
                
                error_list.append({ "type": error_type, "description": error_decription , "scope": scope })
        
        super().context_check()
                
        return error_list
   
    def retrive_var_context(self,node:ASTNode):
        
        if node != None and node.id == ':' and node.left.id == 'var' :
            
            return { 'id': 'let', 'name': node.left.name }
        
        elif node != None and node.id == 'var' :
            return { 'id': 'let', 'name': node.name }
        
        return None

    def create_context(self,args_AST:list):
        
        params_context = []
        if args_AST == None : return []
        
        if args_AST.id == 'params':
            for param in args_AST.parameters:
                
                var = self.retrive_var_context(param)
                if var != None:
                    params_context.append(var)
            
        else:
            arg = self.retrive_var_context(args_AST)
            if var != None:
                    params_context.append(arg)
        
        return params_context

    def send_context(self):
        
        new_context = [ item for item in self.context ]
        params_context = self.create_context(args_AST= self.args)
        my_type = self.my_id()
        
        if self.args != None:
            self.args.context = self.merge_context(params_context,new_context)
            self.args.send_context()
        
        new_context.append(my_type)
        if self.body != None:
            
            body_context = self.merge_context(params_context,new_context)
            
            self.body.context = body_context
            self.body.send_context()
        
        pass
    
    def merge_context(self,context1,context2):
        
        result_context = [  ]
        for item in context2:
            
            result_context.append(item)
        
        for item in context1:
            
            if self.equal(item,result_context):
                continue
            
            result_context.append(item)
        
        return result_context
        
    def equal(self,node1,new_context):
        
        if node1 == None : return False
        return any(lambda node: node['id'] == node1['id'] and node['name'] == node1['name'],new_context)

    pass

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
    body = []
    constructor = []
    base = []
    name = ""
    id = ""
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def context_check(self,error_list:list):
        
        for item in self.context:
        
            if item['id'] == 'type' and item['name'] == self.name:
                
                error_type = "Type definition"
                error_description = f"The Type {self.name} has been already defined"
                scope = self.context
                
                error_list.append({"type": error_type,"description": error_description,"scope": scope})
                
                break
                
        if self.parent_name != None:
        
            self.check_inheritence(error_list)
            pass
        
        super().context_check()
        
        return error_list
    
    def check_inheritence(self,error_list:list):
        
        for item in self.context:
            
                if (item['id'] == 'type' or item['id'] == 'protocol')  and item['name'] == self.name:
                    return
        
        for item in self.build_in:
            
                if item['id'] == 'type' and item['name'] == self.name:
                    return
        
        error_type = "Inheritence undefined"
        error_description = f"name {self.parent_name} could not be found"
        scope = self.context
        
        error_list.extend({ "type": error_type, "description": error_description , "scope":scope })
        
        return error_list
        
    def retrive_var_context(self,node:ASTNode):
        
        if node != None and  node.id == ':' and node.left.id == 'var' :
            
            return { 'id': 'var', 'name': node.left.name }
        
        elif node != None and node.id == 'var' :
            return { 'id': 'var', 'name': node.name }
        
        return None

    def create_context(self,args_AST:list):
        
        params_context = []
        if args_AST == None : return []
        
        if args_AST.id == 'params':
       
            for param in args_AST.parameters:
                
                var = self.retrive_var_context(param)
                if var != None:
                    params_context.append(var)
        else: 
            arg = self.retrive_var_context(args_AST)
            params_context.append( arg )
        
        return params_context

    def send_context(self):
        
        new_context = [ item for item in self.context ]
        params_context = self.create_context(args_AST= self.constructor)
        my_type = self.my_id()
        
        if self.equal( my_type , new_context ):
            
            print(f"\033[1;31m > \033[1;32m The type {my_type['name']} already exists  \033[0m")
            exit()
            
        else:    
            new_context.append(my_type)
        
        if self.constructor != None:
            self.constructor.context = self.merge_context(params_context,new_context)
            self.constructor.send_context()
        
        if self.base != None:
            base_context = self.create_context(args_AST= self.base)
            self.base.context = base_context
            self.base.send_context()
        
        if self.body != None:
            body_context = self.merge_context(params_context,new_context)
            
            self.body.context = body_context
            self.body.send_context()
        
        pass
    
    def merge_context(self,contex1,contex2):
        
        result_context = [  ]
        for item in contex2:
            
            result_context.append(item)
        
        for item in contex1:
            
            if self.equal(item,result_context):
                continue
            
            result_context.append(item)
        
        return result_context
    
    def equal(self,node1,new_context):
        
        if node1 == None : return False
        for item in new_context:
        
            if node1['id'] == item['id'] and node1['name'] == item['name'] : return True
        
        
        return False
    
class protocol(ASTNode): # check context
    
    '''
    atributes of this class are:
    
    > id : protocol
    > name: name of the type
    > parent_name: the name of the class this class inherits from
    > body
    
    '''
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def context_check(self,error_list):
        
        for item in self.context:
            
            if item['id'] == 'protocol' and item['name'] == self.name:
                
                error_type = "protocol definition"
                error_descrption = f"protocol {self.parent_name} already defined"
                scope = self.context
                
                error_list.append({ "type": error_type, "description": error_descrption , "scope":scope})
            
        
        if self.parent_name != None:
            self.check_inheritence(error_list)
            
        super().context_checker()
        
        return error_list
    
    def check_inheritence(self,error_list:list):
        
        for item in self.context:
            
            if item['id'] == 'protocol' and item['name'] == self.parent_name:
                return
        
        for item in self.build_in:
            
            if item['id'] == 'protocol' and item['name'] == self.parent_name:
                return
            
        error_type = "extension undefined"
        error_description = f"name {self.parent_name} could not be found"
        scope = self.context
        error_list.append({ "type": error_type, "description": error_description , "scope":scope})
        
        return error_list
    
class vectors(ASTNode):
    
    '''
    
    vector form: 
    1. [ filter || domain ]
    2. [ 1,2,3,4, ... ]
    
    attributes:
    
    > filter_ : the filter of a vector
    > domain: the domain of a vector
    
    '''

    filter_ = None
    domain = None
        
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
            
class literal(ASTNode):
    
    '''
    attributes:
    
    > id: literal
    > value: value of the literal
    
    '''
    
    value = None
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
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
        
    def context_check(self,error_list:list):
        
        for item in self.context:
            
            if item.id == 'var' and item.name == self.name : 
                
                return error_list

            error_type = "vector undefined"
            error_desciption = f"The vector {self.name} could not be found"
            scope = self.context
            
            error_list.append( {"type":error_type,"description":error_desciption,"scope":scope} )
    
        super().context_check()
            
        return error_list
    
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
    
class for_(ASTNode):
    
    '''
    attributes:
    
    > id : for
    > condition : condition of the for loop
    > body
    
    '''
    
    args = None
    body = None
    
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
    def create_context(self,args_AST:list):
        
        params_context = []
        
        if args_AST == None : 
            print(f"\033[1;31m > no arguments in for loop")
            params_context.append( {'id':'let','name': "" } )
        
        if self.args.left.id != 'var':
            print(f"\033[1;31m > \033[1;32m unexpected argument in \'for\' loop ")
            params_context.append( {'id':'let','name': "" } )
            
        else:    
            params_context.append( {'id':'let','name': self.args.left.name } )
    
        return params_context

    def send_context(self):
        
        new_context = [ item for item in self.context ]
        params_context = self.create_context(args_AST= self.args)
        
        self.args.context = self.merge_context(params_context,new_context)
        self.args.send_context()
        
        if self.body != None:
            
            body_context = self.merge_context(params_context,new_context)
            
            self.body.context = body_context
            self.body.send_context()
        
        pass
    
    def merge_context(self,contex1,contex2):
        
        result_context = [  ]
        for item in contex2:
            result_context.append(item)
        
        for item in contex1:
            
            if self.equal(item,result_context):
                continue
            
            result_context.append(item)
        
        return result_context
        
    def equal(self,node1,new_context):
        
        if node1 == None : return False
        
        return any( lambda item: node1['id'] == item['id'] and node1['name'] == item['name'], new_context)
      
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
    