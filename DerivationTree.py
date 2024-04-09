from EnumsTokensDefinition import TokenType, Type, Keyword
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES, SIMBOL_VALUES, OPERATOR_VALUES
from enum import Enum
from TokensDefinition import SimbolToken, OperatorToken, LiteralToken
import production_class_representation as pdr
    
class builder:

    '''
    This class builds the AST for every node, nodes are:
    
    > Function call
    > blocks
    > for loop
    > while loop
    > if , elif , else
    > variables
    > literals
    > class (type)
    > protocols
    
    '''

    def __init__(self, label ,token_list ):
        
        feature = self.filter_feature(label)
        
        token_list = self.filter_(token_list)
        
        if len(token_list) == 0 : 
            
            self.ASTNode = None
            return None
        
        self.ASTNode = feature(token_list)        
        
    # every function in this class returns an AST of its production
    
    def filter_(self,token_list):
        
        non_token = ['$2','$1','$3',';','{','}','(',')']
        new_token_list = [ item for item in token_list if not any( item[0] == garbage for garbage in non_token )  ]
        
        return new_token_list

    def filter_feature(self,label):
        
        features = [('F',self.F) , ('P',self.P) , ('O',self.O) ,
                    ('b',self.b) , ('B',self.B) , ('p',self.p) , ('E',self.expression),
                    ('if',self.if_) , ('elif',self.elif_) , ('M',self.M) , ('T',self.expression),
                    ('c',self.c) , ( 'var' ,self.var) ,('N',self.N)]
        
        for item in features:
            
            if label == item[0]:
                return item[1]
    
    '''
    All of the next methods are the derivations that a parser can derivate in, 
    except for for_ , while_ and variable 
    
    '''
    
    def F(self ,toke_list:list):
        
        if toke_list[0][0] == 'b': return pdr.block(toke_list)
        
        fc = pdr.function_call(toke_list)
        
        if fc.avaliable : 
            return fc
        
        return None
        
    def N(self,token_list): return None
    
    def c(self,token_list):
        
        variable = pdr.variable(token_list)
        
        if variable.avaliable : return variable
        
        return None
    
    def P(self,toke_list):
        
        params = pdr.params(toke_list)
    
        if params.avaliable: return params
        
    def O(self,token_list):
        
        block = pdr.block(token_list)
        
        if block.avaliable: return block
        
        return None
    
    def b(self,token_list):
                
        if len(token_list) == 0 or len(token_list) > 1 :
            return None # no expression in block , nothing to return
        
        derivations = ["O","E","B","b","T"]
        
        if any(token_list[0][0] == item for item in derivations): return token_list[0][1]  # return what the block has
        
        pass
    
    def B(self,token_list):
        
        if token_list[0][0] != 'B': return None
    
        return  token_list[0][1] # return what the block has
    
    def p(self,token_list):
        
        params = pdr.params(token_list)
        
        if params.avaliable: return params
        
        return None
    
    def else_(self,token_list):
        
        else_ = pdr.else_(token_list)
        
        if else_.avaliable : return else_
        
        return None    
    
    def if_(self,token_list):
        
        if token_list[0][0] == 'if' and len(token_list) == 1 : 
            return token_list[0][1]
        
        if_ = pdr.if_(token_list)
        
        if if_.avaliable : return if_
        
        return None
    
    def elif_(self,token_list):
        
        if token_list[0][0] == 'elif' and len(token_list) == 1 : 
            return token_list[0][1]

        elif_= pdr.elif_(token_list)
        
        if elif_.avaliable : return elif_
        
        return  None

    def M(self,token_list):

        if len(token_list) == 1 and token_list[0][0] == 'M':
            return token_list[0][1]

        type_ = pdr.type_(token_list)
        protocol = pdr.protocol(token_list)
        function = pdr.def_function(token_list)
        
        if type_.avaliable: return type_
        
        if protocol.avaliable: return protocol
        
        if function.avaliable: return function
        
        return None
        
    def expression(self,token_list):
        
        # detects the kind of expression it is

        if len(token_list) == 1 : 
            return token_list[0][1]

        expressions =[
            
            self.F(token_list),
            self.P(token_list),
            self.B(token_list),
            self.p(token_list),
            self.else_(token_list),
            self.elif_(token_list),
            self.if_(token_list),
            self.while_(token_list),
            self.for_(token_list),
            self.indexation(token_list),
         ]
        
        binary_exp = pdr.binary_expression(token_list)
        if binary_exp.avaliable:
            return binary_exp.AST_binary
        
        unary_exp = pdr.unary_expression(token_list)
        if unary_exp.avaliable: 
            return unary_exp.AST_unary
        
        vector = pdr.vectors(token_list)
        if vector.avaliable:
            return vector
        
        for item in expressions:
            if item != None: return item    
    
        return None
    
    def while_(self,token_list):
        
        while_ = pdr.while_(token_list)
        
        if while_.avaliable: return while_
        
        return None
    
    def for_(self,token_list):
        
        for_ = pdr.for_(token_list)
        
        if for_.avaliable: return for_
        
        return None
    
    def indexation(self,token_list):
        
        index = pdr.index(token_list)
        
        if index.avaliable: return index
        
        return None
    
    def var(self,token_list):
        
        var = pdr.variable(token_list)
        if var.avaliable : return var
        
        literal = pdr.literal(token_list)
        if literal.avaliable: return literal