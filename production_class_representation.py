import HULK_LANGUAGE_DEFINITION as hulk

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
        
        if self.validator(token_list):
        
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
        
                if item[0] == token_list[1][0]:
        
                    self.AST = item[1]
    
    def validator(self,token_list):
        
        operators = [ '.', '-=', '*=', '!=', '|', '<=', '<', '==', 'as', ':', '@', '**', '/',
                        '-', '+' , '*' , '^' , '%' , '@@', ':=', 'is', '>' , '>=', '=' , '&' ,
                        '/=', '+=', 'in', ]
        try:
        
            if operators.__contains__(token_list[1][0]):
                return True
        
        except: pass
        
        return False

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
                    
                    self.AST = item[1]

    class new(ASTNode):

        def __init__(self,token_list):
            
            self.set_identifier('new')
            self.left = token_list[1][1]
            
            pass
        
    class let(ASTNode):
    
        def __init__(self,token_list):
        
            if token_list[0] == 'let':
                
                self.set_identifier('let')
                self.right = token_list[1][1]
    
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
        
        if hulk.SYMBOLS_and_OPERATORS_parser.__contains__(token_list[0][0]) and token_list[0][0].SelfType != 'object'  : 
            pass
        
        else:
            self.avaliable = True
            self.set_identifier('var')
            self.name=token_list[0]
        
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
        
        if (token_list[0][0] == 'if' and token_list[1][0] == 'elif') : 
            
            self.avaliable = True
            self.set_identifier(id='elif')
            self.condition = token_list[2][1]
            self.body = token_list[3][1]
        
        pass
    
    
    pass

class else_(ASTNode):
    
    avaliable = False
    def __init__(self,token_list):
        
        if token_list[1][0] == 'else' : 
            
            self.avaliable = True
            self.set_identifier(id='else')
            self.condition = token_list[0][1].condition
            self.body = token_list[2][1]
        
        pass
    
    pass

class def_function(ASTNode):
    
    avaliable = False
    def __init__(self,token_list):
        
        self.name = None
        self.args = None
        self.body = None
        
        if self.validator(token_list):
            
            self.avaliable= True
            self.set_identifier(id='function_form')
            
            if token_list[0][0] == 'function': 
                self.function_kw(token_list)
                        
            elif token_list[0][1].id == 'FunctionCall': 
                self.simple_form(token_list)
                
    def function_kw(self,token_list):
        
        self.name = token_list[1][1].name
        self.args = token_list[1][1].args
        
        if token_list[2][1].id == 'block' or token_list[2][1].id == 'expression':
        
            # function f b | function f E
            self.body = token_list[2][1]
        
        
        elif token_list[2][0] == '=>':
        
            # function f => E | function f => b
            self.body = token_list[3][1]
        
        elif token_list[2][0] == ':':
        
            self.anotated_type = token_list[3][1]
            
            if token_list[4][0] == '=>':
                
                # function f : T => b | function f : T => E
                self.body=token_list[5][1]
            
            else:
                # function f : T b
                self.body=token_list[5][1]
        
    def simple_form(self,token_list):
        
        self.name = token_list[0][1].name
        self.args = token_list[0][1].args
        
        if token_list[1][0] == ":":
            
            # c():T
            self.anotated_type = token_list[2][1]
            
            if len(token_list)>3:
                
                # c():T => b
                self.body = token_list[4][1]
            
            elif len(token_list) > 2:
                
                # c():T b
                self.body = token_list[3][1]
            
        elif token_list[1][0] == "=>":
            
            # c() => E | c() => b
            self.body = token_list[2][1]
        
        else:
            
            # c() E | c() b
            self.body = token_list[1][1]

    def validator(self,token_list):
        
        try:
            if token_list[0][0] == 'function': return True
            
            if token_list[0][0].id == 'FunctionCall' and (token_list[1][0] == ':' or token_list[1][0] == '=>' ):
                return True
        
        except:
            pass
        
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
class vectors(ASTNode):
    
    avaliable = False
    filter_ = None
    domain = None
    
    def __init__(self,token_list):
        
        self.set_identifier('vector')
        
        if self.validator(token_list):
            
            self.validator = True

            self.array_(token_list)
            
    def validator(self,token_list):
        
        if token_list[0][0] == '[': return True
        
        return False
    
    def array_(self,token_list):
        
        if token_list[1][0] == 'p':
            
            self.domain = token_list[1][1].parameters
            
        elif token_list[1][0] == 'T' :
            
            self.filter_ = token_list[1][1]
            self.domain = token_list[3][1]        

class literal(ASTNode):
    
    value = None
    avaliable = False
    def __init__(self,token_list):
        
        if self.validator(token_list) :
            pass
        
        else:
            self.avaliable = True
            self.set_identifier('literal')
            self.value = token_list[0][0].Text
            
    def validator(self,token_list):
        
        if token_list[0][0].SelfType != 'number' and token_list[0][0].SelfType != 'string' and token_list[0][0].SelfType != 'boolean':
            return True
        
        return False
    
    pass

class index(ASTNode):
    
    avaliable = False
    args = None
    name = None
    def __init__(self,token_list):
        
        if self.validator:
            
            self.set_identifier('index')
            self.name = token_list[0][1].name
            self.args = token_list[2][1]      
        
        pass
    
    def validator(self,token_list):
        
        target = ["T","[" , "T" , "]" ]  
        try:
            index = 0
            while index < len(token_list):
                
                if token_list[index] != target[index]: return False
                
                index += 1
                                
        except: 
            return False
        
        return True

class while_(ASTNode):
    
    avaliable = False
    condition = None
    body = None
    
    def __init__(self,token_list):
        
        if self.validator:
            
            self.condition = token_list[1][1]
            self.body = token_list[2][1]
        
        pass
    
    def validator(self,toke_list):
        
        if toke_list[0][0] == 'while':
            return True
        
        return False

class for_(ASTNode):
    
    avaliable = False
    condition = None
    body = None
    
    def __init__(self,token_list):
        
        if self.validator:
            
            self.condition = token_list[1][1]
            self.body = token_list[2][1]
        
        pass
    
    def validator(self,toke_list):
        
        if toke_list[0][0] == 'for':
            return True
        
        return False

class block(ASTNode):
    
    expressions = [] # solve from left to right
    avaliable = False
    
    def __init__(self,token_list):
        
        self.set_identifier('block')
        
        if self.validator(token_list): 
            
            self.avaliable = True
            
            if len(token_list) == 1: # if the first token is a param
                
                self.expressions = token_list[0][1].expressions
            
            else:
                
                if token_list[0][0] == 'O':
                    
                    for item in token_list[0][1]:
                        self.expressions.append(item.expressions)
                    
                    self.expressions.append(token_list[1][1])
                    
                    pass
                
                elif token_list[1][0] == 'O':
                    
                    self.expressions.append(token_list[0][1])
                    
                    for item in token_list[1][1]:
                        self.expressions.append(item.expressions)
                    
                    pass
                else:
                    self.expressions.append(token_list[0][1])
                    self.expressions.append(token_list[1][1])
                            
    def validator(self,token_list):
        
        if token_list[0][0] == 'p': return True
        
        if len(token_list)>1 and token_list[1][0] == ',': return True
        
        return False