import HULK_LANGUAGE_DEFINITION as hulk
import EnumsTokensDefinition as enumTD
'''
NOTE:

token_list is of the form : ( label , ASTNode )

'''
class ASTNode:
    
    """
    defines the nodes of the AST

    > token: Token
    > token -> token corresponding to the node
    > kwargs -> must contain the functions 'Resolver', 'Checker', and Type
    > Resolver must receive as parameters the value of this node and its children
    > Checker must receive as parameters the value of this node, its children, and a dictionary with the context up to the
    > Both, the Resolver and the Checker must return a tuple where the first value is the result and the second the error in case of occurrence
    
    """   
    
    anotated_type = None
    
    def set_identifier(self,id_:str):  
        
        self.id = id_
        
        return self.id
    
    def get_context(self):
        
        # work with the Contex_Builder to return a context
        
        pass
    
    def context_check(self):
        
        pass

    def type_checking(self):
        pass        

    def cil_node_code(self):
        """
        return CIL codes

        """
        pass

class function_call( ASTNode):

    avaliable = False
    def __init__( self, token_list ):
        
        try:
        
            self.set_identifier('FunctionCall')
            self.name = token_list[0][1].name
            self.args = token_list[1][1]
            self.avaliable = True
        
        except:    
            pass
        
        pass
    
class params( ASTNode):
    
    parameters = []
    avaliable = False
    
    def __init__(self,token_list):
        
        self.set_identifier('params')
        
        if self.validator(token_list): self.avaliable = True
        
        if self.avaliable and token_list[0][0] == 'p': # if the first token is a param
            
            self.parameters = token_list[0][1].parameters
            
        elif self.avaliable:
            
            param1 = token_list[0][1]
            self.parameters.append(param1)
            
            if token_list[1][0] == 'p': #  if second token is a param, unbox param "p"
                
                for item in token_list[1][1].parameters:
                    
                    self.parameters.append(item)

            else:
                    
                param2 = token_list[1][1]
                self.parameters.append(param2)
            
                            
    def validator(self,token_list):
        
        if token_list[0][0] == 'p': return True
        
        if len(token_list)>1 and token_list[1][0] == ',': return True
        
        return False

    pass

class binary_expression:
    
    avaliable = False
    AST = None
    def __init__(self,token_list:list):
        
        try:
            # fixxxxx
            if not token_list[1].type() == enumTD.OperatorType.Binary or token_list[1] == ':' or token_list[1] == 'in' :
                pass
        except:
            self.avaliable = True
        
            binary_expresion =[ ('+',self.plus(token_list)) , ('-', self.minus(token_list)) ,
                                ('*', self.multiplication(token_list)) ,('/', self.divition(token_list)) ,
                                ('^', self._pow(token_list)),('**', self._pow(token_list)),
                                ('%', self.per_cent(token_list)),('@', self.concatenation(token_list)),
                                ('@@', self.blank_space_concatenation(token_list), (':',self.double_dot(token_list))),
                                (':=', self.double_dot_equal(token_list), ('as',self.as_(token_list))),
                                ('is', self.is_(token_list), ('==',self.equal(token_list))),
                                ('>', self.bigger_than(token_list), ('<',self.smaller_than(token_list))),
                                ('>=', self.bigger_or_equal(token_list), ('<=',self.smaller_or_equal(token_list))),
                                ('=', self.assign(token_list), ('|',self.or_(token_list))),
                                ('&', self.and_(token_list), ('!=',self.different(token_list))),
                                ('/=', self.divide_and_assign(token_list), ('*=',self.multiply_and_assign(token_list))),
                                ('+=', self.plus_and_assign(token_list), ('-=',self.minus_and_assign(token_list))),
                                ('in', self.in_(token_list)) , ('.', self.in_(token_list))
                                ]
        
            for item in binary_expresion:
        
                if item[0] == token_list[1]:
        
                    self.AST = item[1]
    
    class dot(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('.')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
            pass
        
        pass
        
    class in_(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('in')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
            pass
        
        pass

    class plus(ASTNode):
            
            def __init__(self,token_list):
              
                self.set_identifier('+')
                self.left = token_list[0][1]
                self.right = token_list[2][1]
                
            pass      
  
    class minus(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('-')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class multiplication(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('*')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class divition(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('/')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class _pow(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('^')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class per_cent(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('%')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class concatenation(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('@')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class blank_space_concatenation(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('@@')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
   
    class double_dot(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier(':')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class double_dot_equal(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier(':=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class as_(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('as')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
        pass
    
    class is_(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('is')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
        pass
    
    class equal(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('==')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class bigger_than(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('>')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class smaller_than(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('<')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class bigger_or_equal(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('>=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class smaller_or_equal(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('<=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class assign(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class or_(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('|')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class and_(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('&')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class different(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('!=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class divide_and_assign(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('/=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class multiply_and_assign(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('*=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class plus_and_assign(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('+=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class minus_and_assign(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('-=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
class unary_expression:
    
    avaliable = False
    AST = None
    def __init__(self,token_list):
    
        if hulk.OPERATORS_UNARY.__contains__(token_list[0]):
            pass
        
        else:
            self.avaliable = True
            
            unary = [ ('!',self.not_(token_list)),
                    ('++',self.plus_plus(token_list)),
                    ('--',self.minus_minus(token_list)),
                    ]
            
            for item in unary:
                
                if item[0] == token_list[0]:
                    
                    self.AST = item[1]
    
    class not_(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('!')
            self.right = token_list[1][1]
            
    class plus_plus(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('++')
            self.right = token_list[1][1]
    
    class minus_minus(ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('--')
            self.right = token_list[1][1]
     
class variable(ASTNode):
    
    avaliable = False
     
    def __init__(self,token_list):
        
        if hulk.SYMBOLS_and_OPERATORS_parser.__contains__(token_list[0]): 
            pass
        
        else:
            self.avaliable = True
            self.set_identifier('var')
            self.name=token_list[0]
        
        pass

class variable_def(ASTNode):
    
    avaliable = False
    
    def __init__(self,token_list):
        
        try:
        
            if token_list[0] == 'let':
                
                self.avaliable=True
                
                self.set_identifier('declare_var')
                self.null_son = None
                self.expression = token_list[1][1]
        except:
            pass
    
    pass

class if_(ASTNode):
    
    avaliable = False
    def __init__(self,token_list):
        
        if token_list[0][0] == 'if': 
            
            self.avaliable = True
            self.set_identifier(id='if')
            
            self.condition = token_list[1][1]
            self.body = token_list[2][1]
        
        pass
    
    pass

class elif_(ASTNode):
    
    avaliable = False
    def __init__(self,token_list):
        
        if token_list[0][0] == 'if' and token_list[1][0] == 'elif' : 
            
            self.avaliable = True
            self.set_identifier(id='elif')
            self.condition = token_list[2][1]
            self.body = token_list[3][1]
        
        pass
    
    pass

class type_or_function_or_protocol:
    
    avaliable = False
    selection = None
    
    def __init__(self,token_list):
        
        
                
        pass
    class def_function(ASTNode):
        
        avaliable = False
        def __init__(self,token_list):
            
            self.name = None
            self.args = None
            self.body = None
            
            if self.validator(token_list):
                
                self.validator = True
                self.set_identifier(id='function_form')
                
                
                if token_list[0][0] == 'function':
                    
                    self.name = token_list[1][1].name
                    self.args = token_list[1][1].args
                    
                    if token_list[2][1].id == 'block' or token_list[2][1].id == 'expression':
                    
                        self.body = token_list[2][1]
                    
                    elif token_list[2][0] == '=>':
                        
                        self.body = token_list[3][1]
                    
                    elif token_list[2][0] == ':':
                        
                        if token_list[2][1].id == 'function_form':
                            self.anotated_type
                        
                        self.anotated_type = token_list[3][0]
                        self.body = token_list
                    
#                    elif token_list
                    
                elif len(token_list) > 1 and token_list[1][0] == ':':
                    pass
                
                else:
                    pass
            
                pass
        
            pass
        
        def validator(self,token_list):
            
            
            
            return False
        
        pass

    class type_(ASTNode):
        
        avaliable = False
        def __init__(self,token_list):
            
            if token_list[0][0] == 'type':
                
                self.set_identifier(id='type')
                
                self.name = token_list[1][1].name
                self.body = None
                self.constructor = None
                
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
        
    class protocol(ASTNode):
        
        avaliable = False
        def __init__(self,token_list):
            
            if token_list[0][0] == 'protocol':
            
                self.set_identifier(id='protocol')
                
                self.name = token_list[1][1].name
                self.body = None
                
                self.parent_name = None
            
                if token_list[2][0] == 'extends' :
                    
                    self.parent_name = token_list[3][1].name
                    self.body = token_list[4][1]
                        
                else:
                    self.body = token_list[2][1]
        
            pass

class expression_E(ASTNode):
    
    avaliable = False
    def __init__(self,token_list):
        pass

    pass
