import importing_file as impF

'''
NOTE:

token_list is of the form : ( label , ASTnode )

'''

class function_call( impF.dt.ASTNode):

    def __init__( self, token_list ):
        
        self.set_identifier('FunctionCall')
        self.name = token_list[0][1].name
        self.args = token_list[1][1]
        
        pass

class function_name(impF.dt.ASTNode):
        
        def __init__(self,token_list):

            self.set_identifier("function_name")
            self.name = token_list[0][1].name
    
            pass
            
        pass

class params( impF.dt.ASTNode):
    
    parameters = []
    
    def __init__(self,token_list):
        
        self.set_identifier('params')
        
        if token_list[0][0] == 'p': # if the first token is a param
        
            param1 = token_list[0][1].parameters
        
            for item in param1:
                self.parameters.append(item)
            
            return
        
        else:
            param1 = token_list[0][1]
        
            
        if token_list[1][0] == 'p': #  if second token is a param, unbox param "p"
            
            for item in token_list[1][1].parameters:
                
                self.parameters.append(item)

        else:
            try:
                
                param2 = token_list[1][1]
                self.parameters.append(param2)
            
            except:
                pass
                
        pass    
    
    pass

class binary_expression:
    
    def __init__(self,token_list):
        
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
    
                return item[1]
    
    class dot(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('.')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
            pass
        
        pass
        
    class in_(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('in')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
            pass
        
        pass

    class plus(impF.dt.ASTNode):
            
            def __init__(self,token_list):
              
                self.set_identifier('+')
                self.left = token_list[0][1]
                self.right = token_list[2][1]
                
            pass      
  
    class minus(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('-')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class multiplication(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('*')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class divition(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('/')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class _pow(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('^')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class per_cent(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('%')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class concatenation(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('@')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
    
    class blank_space_concatenation(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('@@')
            self.left = token_list[0][1]
            self.right = token_list[2][1]

        pass
   
    class double_dot(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier(':')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class double_dot_equal(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier(':=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class as_(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('as')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
        pass
    
    class is_(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('is')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
            
        pass
    
    class equal(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('==')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class bigger_than(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('>')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class smaller_than(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('<')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class bigger_or_equal(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('>=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class smaller_or_equal(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('<=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class assign(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class or_(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('|')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class and_(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('&')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class different(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('!=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class divide_and_assign(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('/=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class multiply_and_assign(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('*=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class plus_and_assign(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('+=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
    class minus_and_assign(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('-=')
            self.left = token_list[0][1]
            self.right = token_list[2][1]
        
        pass
    
class unary_expression:
    
    def __init__(self,token_list):
    
        unary = [ ('!',self.not_(token_list)),
                   ('++',self.plus_plus(token_list)),
                   ('--',self.minus_minus(token_list)),
                   ('let',self.let(token_list))
                 ]
        
        for item in unary:
            
            if item[0] == token_list[0]:
                
                return item[1]
    
    class not_(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('!')
            self.right = token_list[1][1]
            
    class plus_plus(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('++')
            self.right = token_list[1][1]
    
    class minus_minus(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('--')
            self.right = token_list[1][1]
    
    class let(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('let')
            self.right = token_list[1][1]
    
class variable(impF.dt.ASTNode):
    
    def __init__(self,token_list):
        
        self.set_identifier('var')
        self.name=token_list[0]
        
        pass

class variable_def(impF.dt.ASTNode):
    
    def __init__(self,token_list):
        
        self.set_identifier('declare_var')
        self.null_son = None
        self.expression = token_list[1][1]
        
        pass
    
    pass
    