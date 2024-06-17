<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

from EnumsTokensDefinition import Type
'''
NOTE:

token_list is of the form : ( label , ASTNode )

'''
=======
#____________________________________________________________________________________________>>>>>>>>>>>>>>>>
>>>>>>> c5c76dc (refactoring)
=======
import copy
>>>>>>> 5689be6 (steps to code -> search_in_ast <- hard coded)
=======
>>>>>>> 9d5529b (context checking has passed a few tests)

class ASTNode:
      
    anotated_type = None
    hash_ = 0
    build_in = [
                {'id': 'let'         , 'name': 'Object' } ,
                {'id': 'let'         , 'name': 'Number' } ,
                {'id': 'let'         , 'name': 'String' } ,
                {'id': 'let'         , 'name': 'Boolean' } ,
                {'id': 'type'         , 'name': 'Object' } ,
                {'id': 'type'         , 'name': 'Number' } ,
                {'id': 'type'         , 'name': 'String' } ,
                {'id': 'type'         , 'name': 'Boolean' } ,
                {'id': 'function_form' , 'name': 'tan' } ,
                {'id': "function_form" , 'name': 'cot' } ,
                {'id': "function_form" , 'name': 'sqrt'} ,
                {'id': "function_form" , 'name': 'sin' } ,
                {'id': "function_form" , 'name': 'cos' } ,
                {'id': "function_form" , 'name': 'log' } ,
                {'id': "function_form" , 'name': 'exp' } ,
                {'id': "function_form" , 'name': 'rand' } ,
                {'id': "function_form" , 'name': 'range' } ,
                {'id': "function_form" , 'name': 'print' } ,
                {'id': "let"          , 'name': 'E' } ,
                {'id': "let"          , 'name': 'PI' } ,
                {'id': "let"          , 'name': 'self' }
                
                ]
    parent = None
<<<<<<< HEAD
=======
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
    
    def visitor_ast(self):
        return self.visitor(self)
    
    def ast_reducer(self):
        
        children = self.visitor_ast()
        
        if len(children) == 1 and children[0] != None:
            return children[0],False
        
        return self,True
            
    def ignition(self,token_list):
        
        attributes = self.builder(token_list)
        
        for property in attributes: # property: ( property_name , property_value)
            self.__dict__[property[0]] = property[1]
        
        ast_node, is_self = self.ast_reducer()
        
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return True,self
    
    def validator(self,token_list):
        
        if len(self.derivation) != len(token_list): return False
        
        if self.match( token_list=token_list , derivation=self.derivation ): return True
        
        return False
    
    def match(self,token_list,derivation):
        
        return any(lambda x,token : x != token , derivation , token_list)
>>>>>>> c5c76dc (refactoring)
    
    def parent_reference(self):
        
        children = self.visitor()
=======
        pass
=======
        return self
>>>>>>> c1b5cd8 (parser-ast integrated)
=======
        if is_self:
            self.parent_reference()
        
        return ast_node
>>>>>>> 66b45d6 (ast fixed and working)
    
    def parent_reference(self):
        
<<<<<<< HEAD
        list_children = self.visitor(self)
>>>>>>> b1116a1 (AST almost integrated to parser)
=======
        list_children = self.visitor_ast()
>>>>>>> 5689be6 (steps to code -> search_in_ast <- hard coded)
        
        for child in children:
            
            if type(child) == list:
                
                for x in child:
                    
                    if x != None:
                        x.parent = self
        
            else:
                
                if child != None:
                    child.parent = self
        
    def my_self(self):
        
        if self.def_node():
            return { 'id': self.id  , 'name': self.name  }
    
    def set_identifier(self,id_:str):  
        
        self.id = id_
        
        return self.id
    
<<<<<<< HEAD
    def def_node(self):
=======
    def check_context(self,error_list):
>>>>>>> 5689be6 (steps to code -> search_in_ast <- hard coded)
        
<<<<<<< HEAD
        def_node = ['function_form','protocol','type','let']
        
        for item in def_node:
=======
        children = self.visitor(self)    
>>>>>>> b1116a1 (AST almost integrated to parser)
            
<<<<<<< HEAD
            if item == self.id:
                return True
        
        return False
    
    def send_context(self): 
        
        '''
        pass the context from one child to another
        
        '''
        
        children: list = self.visitor()
        
        for child in children:
            
            if child == None: continue
            
            my_context = [ item for item in self.context]
            
            if type(child) == list:
                
                for little in child:
                
                    little.context = [ item for item in my_context ]
                    little.send_context()
            else:
                    child.context = [ item for item in my_context ]
                    child.send_context()
                
        
            pass
        
        pass
    
    def context_check(self,error_list:list):
        
        children = self.visitor()
        
        for child in children:
            
            if child == None: continue
            
            if type(child) == list:
                
                for element in child:
                    
                    element.context_check(error_list)
                    
                pass
            
            else:
                    child.context_check(error_list)
                
=======
        if self.id == "var": # check if I am a variable
            
            error_type = "variable declaration"
            error_description = "variable used before declared"
            
            int_max =  2**63 - 1
            
            if self.parent.id == "params": 
                
                # if parent are parameter , it means that the actual node is contained into
                # a function call or a def function or a type definition or a protocol definition,
                # so we have to desambiguate
                
                if self.parent.parent.def_node: # the parent of the params is a def function or a def type or a def protocol
                    
                    self.context_checker( node_id= "let" , error_list= error_list , error_type=error_type , error_description=error_description, name=self.name , h=1 )    
                
                else: # the parent of the params is a function call
                    self.context_checker( node_id= "let" , error_list= error_list , error_type=error_type , error_description=error_description, name=self.name , h=int_max )    
                
            else: # the node is not contained in params
                self.context_checker( node_id= "let" , error_list= error_list , error_type=error_type , error_description=error_description, name=self.name , h=int_max )    
        
        elif self.def_node: # check if I am a definition node
            
            error_type = "definition error"
            error_description = f" {child.id} {child.name} already defined"
            
            self.context_checker( node_id= self.id , error_list= error_list , error_type= error_type , error_description=error_description , name=self.name , h=1 )    
        
        for child in children: # check children
                
            if child != None:
                
                child.check_context(error_list)
        
                pass
            
            pass
        
        pass        
    
    def context_checker( self, node_id , error_list:list , error_type , error_description , name , type_name=None , h=0 ):
        
        allow_apparence = True
        
        if self.def_node:
            allow_apparence = False
        
        node_existence = self.search_in_ast( attr_name=name , attr_id=node_id , type_protocol_name=type_name , h=h )
        
        if allow_apparence and node_existence == 2:
            return error_list
        
        if not allow_apparence and node_existence == 1:
            return error_list
        
        # if node does not exits and should exist , report an error. If exit and it shouldn't ,  report an error
        error_ = { "type" : error_type , "description" : error_description }
        error_list.append(error_)
        
        return error_list
    
    def search_in_ast(self , attr_name , attr_id , type_protocol_name= None , n=0 , h=0 ) -> int: # return the number of features in ast
    
        parent = self.parent
        
        while parent != None or h == -1 :
        
            for child in parent.visitor_ast(): 
                
                if child == None : continue
                
                if type_protocol_name == None: # pass over child if type_protocol_name is not defined
                    
                   if child.__dict__.__contains__("name") and child.name == attr_name and child.id == attr_id:
                        
                        n+=1
                       
                        pass
                
                # if type_protocol_name is defined , then search in types or protocols
                elif child.__dict__.__contains__("name") and type_protocol_name == child.name and ( child.id == "type" or child.id == "protocol") :
                    
                    type_protocol_block = child.visitor_ast()
                    
                    for filds in type_protocol_block:
                        
                        if filds.__dict__.__contains__("name") and filds["name"] == attr_name and filds.id == attr_id:
                            
                            n +=1
                            
                            pass    
                
                    
            parent = parent.parent
            h -= 1
        
        return n
        
    def infer_type(self,error_list:list):
>>>>>>> 5689be6 (steps to code -> search_in_ast <- hard coded)
        pass
                
        return error_list
        
    def type_checking(self):
        pass        

    def visitor(self):
        
        '''
        visitor returns a list of elements you can visit
        example: 
        
            while condition 
                
                body
                
            "visitor" returns : [ condition , body ]
        
        by default "visitor" returns binary operation visitation
        
        '''
        
        return [ self.left , self.right ]
    
    def cil_node_code(self):
        """
        return CIL codes

        """
        pass

class function_call( ASTNode): # check context

    '''
    atributes of this class are:
    
    > id
    > name : FunctionCall
    > args
    
    '''
    
    context = []
    avaliable = False
    
<<<<<<< HEAD
    def __init__( self, token_list ):
        
        if self.validator(token_list):
        
            self.set_identifier('FunctionCall')
            self.name = token_list[0][1].name
            self.args = token_list[1][1]
                
            self.avaliable = True
        
        pass
    
    def visitor(self):
        
        if self.args != None and self.args.id == 'parameters':
            return self.args
    
        else: return [self.args]
    
=======
>>>>>>> c5c76dc (refactoring)
    def context_check(self,error_list):
        
        for item in self.context:
            
            if item['id'] == 'function_form' and item['name'] == self.name:
                return error_list
            
        for item in self.build_in:
        
            if item['id'] == 'function_form' and item['name'] == self.name:
                return error_list
            
        error_type = "Function undefined"
        error_decription = f"Function {self.name} could not be found"
        scope = self.context
        error_list.append({'type': error_type, 'description': error_decription, 'scope':scope})
        
        children = self.visitor()
        
        if type(children) == list:
            
            for child in children:
                
                if child != None:
                    child.context_check(error_list)    
                
                pass 
        
        return error_list
    
    def type_checking(self):
        return super().type_checking()
        
    def validator(self, token_list):
        
        if token_list[0][0] == 'c' or token_list[0][0] == 'b' : return True
    
class params( ASTNode):
    
    '''
    atributes of this class are:
    
    > id : params
    > parameters
    
    '''
    
    parameters = []
    avaliable = False
    context = []
    
<<<<<<< HEAD
    def __init__(self,token_list):
        
        self.set_identifier('params')
        
        if self.validator(token_list): self.avaliable = True
        
        if self.avaliable and token_list[0][0] == 'p': # if the first token is a param
            
            self.parameters = [ item for item in token_list[0][1].parameters ]
            
        elif self.avaliable:
            
            param1 = token_list[0][1]
            new_parameters = []
            
            if token_list[2][0] == 'p': #  if second token is a param, unbox param "p"
                
                new_parameters = [ item for item in token_list[2][1].parameters ]
                new_parameters.insert(0,param1)
                self.parameters = new_parameters
=======
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
            
>>>>>>> c5c76dc (refactoring)
            else:
                    
                param2 = token_list[2][1]
                new_parameters.append(param1)
                new_parameters.append(param2)
                self.parameters = new_parameters
        
    def visitor(self):
        return self.parameters
                            
    def validator(self,token_list):
        
        if token_list[0][0] == 'p': return True
        
        if len(token_list)>1 and token_list[1][0] == ',': return True
        
        return False

    pass

class binary_expression:
    
    '''
    this class selects the kind of binary expression the token_list refers to. Every
    class in this class has as attributes:
    
    > id : the kind of expression it is specified by its symbol
    > left: left member
    > right: right member
    
    '''
    
    avaliable = False
    AST_binary = None
    def __init__(self,token_list:list):
        
        if self.validator(token_list):
        
            self.avaliable = True
        
            binary_expresion =[ ('+',self.plus(token_list)) , ('-', self.minus(token_list)) ,
                                ('*', self.multiplication(token_list)) ,('/', self.divition(token_list)) ,
                                ('^', self._pow(token_list)),('**', self._pow(token_list)),
                                ('%', self.per_cent(token_list)),('@', self.concatenation(token_list)),
                                ('@@', self.blank_space_concatenation(token_list)), (':',self.double_dot(token_list)),
                                (':=', self.double_dot_equal(token_list)), ('as',self.as_(token_list)),
                                ('is', self.is_(token_list)), ('==',self.equal(token_list)),
                                ('>', self.bigger_than(token_list)), ('<',self.smaller_than(token_list)),
                                ('>=', self.bigger_or_equal(token_list)), ('<=',self.smaller_or_equal(token_list)),
                                ('=', self.assign(token_list)), ('|',self.or_(token_list)),
                                ('&', self.and_(token_list)), ('!=',self.different(token_list)),
                                ('/=', self.divide_and_assign(token_list)), ('*=',self.multiply_and_assign(token_list)),
                                ('+=', self.plus_and_assign(token_list)), ('-=',self.minus_and_assign(token_list)),
                                ('in', self.in_(token_list)) , ('.', self.dot(token_list))
                                ]
        
            for item in binary_expresion:
        
                if item[0] == token_list[1][0]:
        
                    self.AST_binary = item[1]
                    return
    
    def validator(self,token_list):
        
        operators = [ '.', '-=', '*=', '!=', '|', '<=', '<', '==', 'as', ':', '@', '**', '/',
                        '-', '+' , '*' , '^' , '%' , '@@', ':=', 'is', '>' , '>=', '=' , '&' ,
                        '/=', '+=', 'in' ]
        try:
        
            if operators.__contains__(token_list[1][0]):
                return True
        
        except: pass
        
        return False

    class dot(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('.')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
            pass
        
        pass
        
        def visitor(self):
            return [ self.left , self.right ]
        
        pass
    class in_(ASTNode):
        
        context = []        
        def __init__(self,token_list):
            
            self.set_identifier('in')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
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
            
            if args_AST == None : return []
            
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
        
            if self.right != None:
                
                right_context = self.merge_context(params_context,new_context)
                
                self.right.context = right_context
                self.right.send_context()
            
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
            
                if node1['id'] == item['id'] and node1['name'] == item['name'] :
                    return True
            
            return False
     
        pass

    class plus(ASTNode):
            
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('+')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
        pass      
    
    class minus(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('-')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    
    class multiplication(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('*')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class divition(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('/')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
        
    class _pow(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('^')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
        
    class per_cent(ASTNode):
        
        context = []        
        def __init__(self,token_list):
            
            self.set_identifier('%')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
   
    
    class concatenation(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('@')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
        
        
    class blank_space_concatenation(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('@@')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
   
    class double_dot(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier(':')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
    
        
        def context_check(self, error_list: list):
            
            for item in self.context:
                
                try:
                    
                    if (item['id'] == 'type' or item['id'] == 'protocol') and item['name'] == self.right.name:
                        return error_list                
                except:
                    pass

            for item in self.build_in:
                
                try:
                    
                    if (item['id'] == 'type' or item['id'] == 'protocol') and item['name'] == self.right.name:
                        return error_list                
                except:
                    pass

            try:
                
                error_type = "type undefined"
                error_description = f"type {self.right.name} could not be found"
                scope = self.context
                
                error_list.append({"type":error_type,'description':error_description,'scope':scope})
            
            except:
                
                error_type = "unexpected expression"
                error_description = f"unexpected expression at the right side of double dots"
                scope = self.context
                
                error_list.append({"type":error_type,"description":error_description,"scope":scope})
                
            
            return error_list
    
        pass
    
    class double_dot_equal(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier(':=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class as_(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('as')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
        pass
    
    class is_(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('is')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
        pass
    
    class equal(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('==')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
        
    class bigger_than(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('>')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class smaller_than(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('<')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class bigger_or_equal(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('>=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class smaller_or_equal(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('<=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class assign(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
        
    class or_(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('|')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class and_(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('&')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
        
    class different(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('!=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class divide_and_assign(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('/=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
        
    class multiply_and_assign(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('*=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class plus_and_assign(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('+=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class minus_and_assign(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('-=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
class unary_expression:
    
    '''
    this class selects the kind of binary expression the token_list refers to. Every
    class in this class has as attributes:
    
    > id : the kind of expression it is specified by its symbol
    > right: right unary member
    
    '''
    
    avaliable = False
    AST_unary = None
    def __init__(self,token_list):
    
        unary_operators = ['!','++','--','new','let']
        if not unary_operators.__contains__(token_list[0][0]):            
            pass
        
        else:
            self.avaliable = True
            
            unary = [ ('!',self.not_(token_list)),
                    ('++',self.plus_plus(token_list)),
                    ('--',self.minus_minus(token_list)),
                    ('new',self.new(token_list)),
                    ('let',self.let(token_list)),
                    ]
            
            for item in unary:
                
                if item[0] == token_list[0][0]:
                    
                    self.AST_unary = item[1]
                    return

    class new(ASTNode):

        context = []
        def __init__(self,token_list):
            
            self.set_identifier('new')
            self.right = token_list[1][1]
            
            pass
        
        def context_check(self, error_list: list):
            
            for item in self.context:
            
                if item['id'] == 'type' and item['name'] == self.right.name:
                    return error_list
            
            error_type = 'undefined type'
            error_description = f"The type {self.right.name} is not defined or visible for new keyword"
            scope = self.context
            
            error_list.append({'type':error_type,'description':error_description,'scope':scope})
            
            return error_list
        
        def visitor(self):
            return [self.right]
        
    class let(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            if token_list[0][0] == 'let':
            
                self.set_identifier('let')
                self.right = token_list[1][1]
                
                try :
                    
                    if self.right.id == 'var':
                        self.name = self.right.name

                    else:
                        self.name = self.right.left.name
                
                except :
                    self.name = None
            
        def context_check(self, error_list: list):
        
            if self.name == None:
                
                error_type = "variable declaration"
                error_description = "No inicialization for \033[1;31m let \033[0m"
                scope = self.context
                error_list.append({ "type": error_type, "description": error_description, "scope": scope})
            
            
            self.right.context_check(error_list)
            
            return error_list
        
        def visitor(self):
            return [self.right]

    class not_(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('!')
            self.right = token_list[1][1]
            
        def visitor(self):
            return [self.right]
    class plus_plus(ASTNode):
        
        context = []    
        def __init__(self,token_list):
            
            self.set_identifier('++')
            self.right = token_list[1][1]
    
        def visitor(self):
            return [self.right]
    
    class minus_minus(ASTNode):
        
        context = []
        def __init__(self,token_list):
            
            self.set_identifier('--')
            self.right = token_list[1][1]
            
        def visitor(self):
            return [self.right]
     
class variable(ASTNode): # check context
    
    '''
    this class has the attributes:
    
    > id : var
    > name: name of the variable
    
    '''
    
<<<<<<< HEAD
    avaliable = False
    context = []
     
    def __init__(self,token_list):
        
        try:
            if not token_list[0][0].Type.name == 'Variable' and not token_list[0][0].KeywordType.name == 'Function'  :
                pass
            
            else:
                self.avaliable = True
                self.set_identifier('var')
                self.name=token_list[0][0].Text
        
        except : pass
    
    def visitor(self):
        return [None]

=======
>>>>>>> c5c76dc (refactoring)
    def context_check(self,error_list):
        
        for item in self.context:
            
            if item['id'] == 'let' and item['name'] == self.name :
                return error_list
            
        for item in self.build_in:
        
            if item['id'] == 'let' and item['name'] == self.name :
                return error_list
        
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
    
<<<<<<< HEAD
    avaliable = False
    context = []
    def __init__(self,token_list):
        
        if token_list[0][0] == 'if': 
            
            self.avaliable = True
            self.set_identifier('if')
            
            self.condition = token_list[1][1]
            self.body = token_list[2][1]
        
        pass
    
    pass

    def visitor(self):
        return [ self.condition , self.body ]
=======
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
>>>>>>> c5c76dc (refactoring)

class elif_(ASTNode):
    
    '''
    this class has the attributes:
    
    > id : elif
    > condition : condition for elif statement and the condition for the if statement , the condition is a list
    > body: body of the statement
    
    NOTE:
    
    The condition is a list that refers to if statement , and has second element has the elif statement
    
    '''
    
    avaliable = False
    condition=None
    context = []
    
    def __init__(self,token_list):
        
<<<<<<< HEAD
        if (token_list[0][0] == 'if' and token_list[1][0] == 'elif') : 
            
            self.avaliable = True
            self.set_identifier('elif')
            
            self.condition = [ token_list[0][1] , token_list[2][1] ]
            self.body = token_list[3][1]
        
        pass
    
    def visitor(self):
        return [ self.condition , self.body  ]
        
=======
>>>>>>> c5c76dc (refactoring)
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
    
    avaliable = False
    condition = None
    context = []
    
    def __init__(self,token_list):
        
        if token_list[1][0] == 'else' : 
            
            self.avaliable = True
            self.set_identifier('else')
            
            self.condition = token_list[0][1]
            
            self.body = token_list[2][1]
        
        pass
    
    pass

<<<<<<< HEAD
    def visitor(self):
        return [ self.condition , self.body ]

=======
>>>>>>> c5c76dc (refactoring)
class def_function(ASTNode): # check context
    
    '''
    atributes of this class are:
    
    > id : function_form
    > name: name of the function declared
    > args
    > body
    
    '''
    
    avaliable = False
    context = []
    
    def __init__(self,token_list):
        
        self.name = None
        self.args = None
        self.body = None
        
        if self.validator(token_list):
            
            self.avaliable= True
            self.set_identifier('function_form')
            
            if token_list[0][0] == 'function': 
                self.function_kw(token_list)
                        
            elif token_list[0][1].id == 'FunctionCall': 
                self.simple_form(token_list)
        
    def context_check(self,error_list):
        
        for item in self.context:
            
            if item['id'] == self.id and item['name'] == self.name:
                
                error_type = "Function definition"
                error_decription = f"The function {self.name} has been already defined"
                scope = self.context
                
                error_list.append({ "type": error_type, "description": error_decription , "scope": scope })
                
        children = self.visitor()
        
        if type(children) == list:
            
            for child in children:
                
                if child != None:
                     child.context_check(error_list)    
                
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
            params_context.append( arg )
        
        return params_context

    def send_context(self):
        
        new_context = [ item for item in self.context ]
        params_context = self.create_context(args_AST= self.args)
        my_type = self.my_self()
        new_context.append(my_type)
        
        if self.args != None:
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
<<<<<<< HEAD
        for item in new_context:
        
            if node1['id'] == item['id'] and node1['name'] == item['name'] : return True
        
        return False
    
    def function_kw(self,token_list):
        
        self.name = token_list[1][1].name
        self.args = token_list[1][1].args
        
        if token_list[2][0] == 'b' or token_list[2][0] == 'E':
        
            # function f b | function f E
            self.body = token_list[2][1]
    
        
        if token_list[2][0] == '=>':
        
            # function f => E | function f => b
            self.body = token_list[3][1]
        
        elif token_list[2][0] == ':':
        
            self.anotated_type = token_list[3][1]
            
            if token_list[4][0] == '=>':
                
                # function f : T => b | function f : T => E
                self.body=token_list[5][1]
            
            else:
                # function f : T b
                self.body=token_list[4][1]
        
    def simple_form(self,token_list):
        
        self.name = token_list[0][1].name
        self.args = token_list[0][1].args
        
        if token_list[1][0] == ":":
            
            # c():T
            self.anotated_type = token_list[2][1]
            
            if len(token_list)>4:
                
                # c():T => b
                self.body = token_list[4][1]
            
            elif len(token_list) > 3:
                
                # c():T b
                self.body = token_list[3][1]
            
        elif token_list[1][0] == "=>":
            
            # c() => E | c() => b
            self.body = token_list[2][1]
        
        else:
            
            # c() E | c() b
            self.body = token_list[1][1]

    def visitor(self):
        return [ self.args , self.body ]

    def validator(self,token_list):
        
        try:
            if token_list[0][0] == 'function': return True
            
            if token_list[0][1].id == 'FunctionCall' and (token_list[1][0] == ':' or token_list[1][0] == '=>' ):
                return True
        
        except:
            pass
        
        return False
    
=======
        return any(lambda node: node['id'] == node1['id'] and node['name'] == node1['name'],new_context)

>>>>>>> c5c76dc (refactoring)
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
    
    avaliable = False
    context = []
    def __init__(self,token_list):
        
        if token_list[0][0] == 'type':
            
            self.set_identifier('type')
            
            self.avaliable = True
            
            self.name = token_list[1][1].name
            self.body = None
            self.constructor = None
            self.anotated_type = self.name
            
            if token_list[1][1].id == 'FunctionCall':
                self.constructor = token_list[1][1].args
            
            self.parent_name = None
            self.base = None
            
            if token_list[2][0] == 'inherits' :
                
                self.parent_name = token_list[3][1].name
                
                if token_list[3][1].id == 'FunctionCall':
                    self.base = token_list[3][1].args
                
                self.body = token_list[4][1]
            
                if self.constructor != None and self.base != None:
                    self.avaliable = True
                    
            else:
                self.body = token_list[2][1]
        pass
    
    def context_check(self,error_list:list):
        
        for item in self.context:
        
            if item['id'] == 'type' and item['name'] == self.name:
                
                error_type = "Type definition"
                error_description = f"The Type {self.name} has been already defined"
                scope = self.context
                
                error_list.append({"type": error_type,"description": error_description,"scope": scope})
                
                break
                
        children = self.visitor()

        if type(children) == list:
        
            for child in children:
                
                if child != None:
                    child.context_check(error_list)    
                
                pass
        
        if self.parent_name != None:
        
            self.check_inheritence(error_list)
            pass
        
        return error_list
    
    def check_inheritence(self,error_list:list):
        
        for item in self.context:
            
                if item['id'] == 'type' and item['name'] == self.name:
                    return []
        
        for item in self.build_in:
            
                if item['id'] == 'type' and item['name'] == self.name:
                    return []
        
        error_type = "Inheritence undefined"
        error_description = f"Type {self.parent_name} could not be found"
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
        my_type = self.my_self()
        
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
    
<<<<<<< HEAD
    def visitor(self):
        return [ self.constructor , self.base , self.base ]

=======
>>>>>>> c5c76dc (refactoring)
class protocol(ASTNode): # check context
    
    '''
    atributes of this class are:
    
    > id : protocol
    > name: name of the type
    > parent_name: the name of the class this class inherits from
    > body
    
    '''
    
    avaliable = False
    context = []
    
    def __init__(self,token_list):
        
        if token_list[0][0] == 'protocol':
            
            self.avaliable = True
        
            self.set_identifier('protocol')
                
            self.name = token_list[1][1].name
            self.body = None
            self.anotated_type = self.name
            
            self.parent_name = None
        
            if token_list[2][0] == 'extends' :
                
                self.parent_name = token_list[3][1].name
                self.body = token_list[4][1]
                    
            else:
                self.body = token_list[2][1]
    
        pass
    
    def context_check(self,error_list):
        
        for item in self.context:
            
            if item['id'] == 'protocol' and item['name'] == self.name:
                
                error_type = "Protocol extention undefined"
                error_descrption = f"Protocol {self.parent_name} could not be found"
                scope = self.context
                
                error_list.append({ "type": error_type, "description": error_descrption , "scope":scope})
            
        children = self.visitor()
    
        if type(children) == list:
        
            for child in children:
                
                if child != None:
                    child.context_check(error_list)    
                
                pass
        
        if self.parent_name != None:
            self.check_inheritence(error_list)
            
        return error_list
    
    def check_inheritence(self,error_list:list):
        
        for item in self.context:
            
            if item['id'] == 'protocol' and item['name'] == self.parent_name:
                return []
        
        for item in self.build_in:
            
            if item['id'] == 'protocol' and item['name'] == self.parent_name:
                return []
            
        error_type = "Inheritence undefined"
        error_description = f"Type {self.parent_name} could not be found"
        scope = self.context
        error_list.append({ "type": error_type, "description": error_description , "scope":scope})
        
        return error_list
<<<<<<< HEAD
        
    def visitor(self):
        return [ self.body ]

=======
    
>>>>>>> c5c76dc (refactoring)
class vectors(ASTNode):
    
    '''
    
    vector forms: 
    1. [ filter || domain ]
    2. [ 1,2,3,4, ... ]
    
    attributes:
    
    > filter_ : the filter of a vector
    > domain: the domain of a vector
    
    '''
    
    avaliable = False
    filter_ = None
    domain = None
    context = []
        
<<<<<<< HEAD
    def __init__(self,token_list):
        
        self.set_identifier('vector')
        
        if self.validator(token_list):
            
            self.avaliable = True

            self.array_(token_list)
            
    def validator(self,token_list):
        
        if token_list[0][0] == '[': return True
        
        return False
    
    def array_(self,token_list):
        
        if token_list[1][0] == 'p':
            
            self.domain = [ item for item in token_list[1][1].parameters ]
            
        elif token_list[1][0] == 'T' :
            
            self.filter_ = token_list[1][1]
            self.domain = token_list[3][1]        

    def visitor(self):
        return [ self.filter_ , self.domain ]

=======
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
            
>>>>>>> c5c76dc (refactoring)
class literal(ASTNode):
    
    '''
    attributes:
    
    > id: literal
    > value: value of the literal
    
    '''
    
    value = None
    avaliable = False
    context = []
    
<<<<<<< HEAD
    def __init__(self,token_list):
        
        if self.validator(token_list) :
            pass
        
        else:
            self.avaliable = True
            self.set_identifier('literal')
            if token_list[0][0].SelfType == Type.Number:
                self.value = float(token_list[0][0].Text)
                pass
            else:
                self.value = token_list[0][0].Text
                pass

            
    def validator(self,token_list):
        
        try:
            if token_list[0][0].SelfType == 'Number' or token_list[0][0].SelfType == 'String' or token_list[0][0].SelfType == 'Boolean':
                return True
        except:    
            return False
    
    def visitor(self):
        return [None]
=======
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
>>>>>>> c5c76dc (refactoring)
    
    pass

class index(ASTNode): # check context
    
    '''
    attributes:
    
    > id : index
    > name: name of the indexation vector
    > index : index of the vector 
    
    '''
    
    avaliable = False
    args = None
    name = None
    context = []
    
    def __init__(self,token_list):
        
        if self.validator(token_list):
            
            self.avaliable = True
            self.set_identifier('index')
            self.name = token_list[0][1].name
            self.index = token_list[2][1]      
        
        pass
    
    def validator(self,token_list):
        
        target = ["T","[" , "T" , "]" ]  
        try:
            index = 0
            while index < len(token_list):
                
                if token_list[index][0] != target[index]: return False
                
                index += 1
                                
        except: 
            return False
        
        return True
    
    def context_check(self,error_list:list):
        
        for item in self.context:
            
            if item.id == 'var' and item.name == self.name : 
                
                return error_list

            error_type = "vector undefined"
            error_desciption = f"The vector {self.name} could not be found"
            scope = self.context
            
            error_list.append( {"type":error_type,"description":error_desciption,"scope":scope} )
    
        children = self.visitor()

        if type(children) == list:
            
            for child in children:
                
                child.context_check(error_list)    
                
                pass
            
        return error_list
    
<<<<<<< HEAD
    def visitor(self):
        return [self.index]
=======
>>>>>>> c5c76dc (refactoring)
class while_(ASTNode):
    
    '''
    attributes:
    
    > id : while
    > condition : condition of the while loop
    > body
    
    '''
    
    avaliable = False
    condition = None
    body = None
    context = []
    
<<<<<<< HEAD
    def __init__(self,token_list):
        
        if self.validator(token_list):
            
            self.avaliable = True
            self.set_identifier('while')
            self.condition = token_list[1][1]
            self.body = token_list[2][1]
        
        pass
    
    def validator(self,toke_list):
        
        if toke_list[0][0] == 'while':
            return True
        
        return False
    
    def visitor(self):
        return [ self.condition , self.body ]

=======
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
    
>>>>>>> c5c76dc (refactoring)
class for_(ASTNode):
    
    '''
    attributes:
    
    > id : for
    > condition : condition of the for loop
    > body
    
    '''
    
    avaliable = False
    args = None
    body = None
    context = []
    
    def __init__(self,token_list):
        
        if self.validator(token_list):
            
            self.avaliable = True            
            self.set_identifier('for')
            self.args = token_list[1][1]
            self.body = token_list[2][1]
        
        pass
    
    def validator(self,toke_list):
        
        if toke_list[0][0] == 'for':
            return True
        
        return False
    
    def visitor(self):
        return [ self.args , self.body ]
    
    def create_context(self,args_AST:list):
        
        params_context = []
        
        if args_AST == None : 
            print(f"\033[1;31m > No arguments in for loop")
            exit()
            
        if self.args.left.id != 'var':
            print(f"\033[1;31m > \033[1;32m unexpected argument for \'for\' loop ")
            exit()
            
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
        for item in new_context:
        
<<<<<<< HEAD
            if node1['id'] == item['id'] and node1['name'] == item['name'] : return True
        
        return False

=======
        return any( lambda item: node1['id'] == item['id'] and node1['name'] == item['name'], new_context)
      
>>>>>>> c5c76dc (refactoring)
class block(ASTNode):
    
    '''
    attributes:
    
    > id : block
    > expressions : expressions inside of the block
    
    >> solve from left to right
    
    '''
    
    expressions = [] 
    avaliable = False
    context = []
    
<<<<<<< HEAD
    def __init__(self,token_list):
        
        self.expressions = []
        self.avaliable = False
        self.context = []
        self.set_identifier('block')
        
        if self.validator(token_list): 
            
            self.avaliable = True
            
            if len(token_list) == 1: # if the first token is a param
                
                if token_list[0][0] == 'M':
                    self.expressions = token_list[0][1]
                
                elif token_list[0][1] != None and  token_list[0][1].id == 'block' : 
                    
                    self.expressions = token_list[0][1].expressions

                else:
                    self.expressions = token_list[0][1]
            else:
                
                if token_list[0][0] == 'O' and token_list[0][1] == 'O':
                    
                    self.expressions = token_list[0][1]
                    self.expressions.extend(token_list[1][1])
                
                
                elif token_list[0][0] == 'O':
                    
                    self.expressions = token_list[0][1].expressions
                    
                    if type(self.expressions) == list:
                        self.expressions.append(token_list[1][1])
                    
                    else:
                        new_expression_set = [self.expressions , token_list[1][1]]
                        self.expressions = new_expression_set
                    
                    pass
                
                elif token_list[1][0] == 'O':
                    
                    self.expressions.append(token_list[0][1])
                    
                    for item in token_list[1][1].expressions:
                        self.expressions.append(item)
                    
                    pass
                else:
                    self.expressions.append(token_list[0][1])
                    self.expressions.append(token_list[1][1])
    
    def send_context(self):
        
        new_context = [ item for item in self.context ]
        
        if type(self.expressions) == list:
            
            for expression in self.expressions:
            
                # nodes that define new variables , increases context
                if expression.def_node() : 
                    
                    expression_type = expression.my_self()
                    expression.context = [ item for item in new_context ]
                    expression.send_context()
                    new_context.append(  expression_type )
                
                else:
                    
                    expression.context = [ item for item in new_context ]
                    expression.send_context()
                    
        else:
                expression = self.expressions
                expression.context = [ item for item in new_context ]
                expression.send_context()
        
                if expression.def_node() : 
                    
                    expression_type = expression.my_self()
                    new_context.append(  expression_type )
                
        pass
    
    def equal(self,node1,new_context):
        
        if node1 == None : return False
        for item in new_context:
        
            if node1['id'] == item['id'] and node1['name'] == item['name'] : return True
        
        
        return False
    
    def validator(self,token_list):
        
        return True
    
    def visitor(self):
        
        if type(self.expressions) == list:
            return self.expressions
        
        else:
            return [self.expressions]
=======
    def __init__(self, grammar={ "derivation": "","identifier": ""," definition_node?": "","builder": None,"visitor": None }) -> None:
        super().__init__(grammar)
<<<<<<< HEAD
>>>>>>> c5c76dc (refactoring)
    
=======
>>>>>>> 5689be6 (steps to code -> search_in_ast <- hard coded)
