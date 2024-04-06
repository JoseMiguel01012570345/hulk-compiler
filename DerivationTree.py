from EnumsTokensDefinition import TokenType, Type, Keyword
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES, SIMBOL_VALUES, OPERATOR_VALUES
from enum import Enum
from TokensDefinition import SimbolToken, OperatorToken, LiteralToken
import production_class_representation as pdr

def AST(self):
        """
        retorna el AST asociado
        """
        # Si es el caracter vacio
        if len(self.Text) == 0:
            return None
        # Si es un nodo hoja
        if self.IsLeaf:
            return self.ASTNode
        # Si solamente tiene un hijo
        if len(self.Childs) == 1:
            return self.Childs[0].AST
        # Si es un operador
        if self.Type == TokenType.Operator:
            # computamos los ast de cada hijo
            ASTChilds = [child.AST for child in self.Childs]
            # creamos el astnode correspondiente a este nodo
            node = self.ASTNode
            # le ponemos los ast hijos de este nodo
            node.Childs = ASTChilds
            return node
        # si el nodo no ofrece ninguna informacion
        if (
            not self.Type == TokenType.Operator
            and not self.Type == TokenType.Keyword
            and not self.Type == TokenType.Variable
        ):
            # buscamos por algun hijo que si nos ofrezca informacion
            childs = self.Childs
            position = 0
            for i in range(len(childs)):
                # encontramos el nodo deseado, un operador, una variable, un literal o una palabra clave
                if (
                    childs[i].Type == TokenType.Operator
                    or childs[i].Type == TokenType.Keyword
                    or childs[i].Type == TokenType.Variable
                    or childs[i].Type == TokenType.Literal
                ):
                    position = i
                    break
                pass
            #  extraemos el nodo encontrado
            node = childs.pop(position)
            #  computamos sus hijos y los agregamos a los hijos que tenemos hasta ahora
            childs = childs.__add__(node.Childs)
            # eliminamos la referencia a sus hijos
            node._childs = None
            # computamos el astnode correspondiente al nodo encontrado
            ASTNode = node.ASTNode
            # computamos los ast de cada hijo existente
            ASTChilds = []
            for child in childs:
                ASTChilds.append(child.AST)
                pass
            # le pasamos la referencia de ellos al astnode actual
            ASTNode.Childs = ASTChilds
            # retornamos el AST construido
            return ASTNode
        # extraemos el ASTNode correspondiente al nodo actual
        ASTNode = self.ASTNode
        # computamos los AST hijos
        ASTChilds = [child.AST for child in self.Childs]
        # agregamos la referencia y retornamos
        ASTNode.Childs = ASTChilds
        return ASTNode
    
class builder:

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
    
    def F(self ,toke_list:list):
        
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
            self.b(token_list),
            self.B(token_list),
            self.p(token_list),
            self.else_(token_list),
            self.elif_(token_list),
            self.if_(token_list),
            self.M(token_list),
            self.while_(token_list),
            self.for_(token_list),
         ]
        
        binary_exp = pdr.binary_expression(token_list)
        if binary_exp.avaliable:
            return binary_exp.AST
        
        unary_exp = pdr.unary_expression(token_list)
        if unary_exp.avaliable: 
            return unary_exp.AST
        
        
        for item in expressions:
            if item != None: return item    
    
        return None
    
    def while_(self,token_list):
        
        while_ = pdr.while_(token_list)
        
        if while_.avaliable: return while_
        
        return None
    
    def for_(self,token_list):
        
        for_ = pdr.while_(token_list)
        
        if for_.avaliable: return for_
        
        return None
    
    def var(self,token_list):
        
        var = pdr.variable(token_list)
        if var.avaliable : return var
        
        literal = pdr.literal(token_list)
        if literal.avaliable: return literal