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
        
        self.ASTNode = feature(token_list)        
        

    def filter_feature(self,label):
        
        features = [('F',self.F) , ('P',self.P) , ('T',self.T) , ('N',self.N) ,
                    ('O',self.O) , ('b',self.b) , ('B',self.B) , ('p',self.p) , 
                    ('if',self.if_) , ('elif',self.elif_) , ('M',self.M) , ('Q',self.Q) ,
                    ('c',self.c) ]
        
        for item in features:
            
            if label == item[0]:
                return item[1]
    
    def F(self ,toke_list:list):
        
        fc = pdr.function_call(toke_list)
        
        if fc.avaliable : return fc
        
        return None
        
    def c(self,token_list):
        
        variable = pdr.variable(token_list)
        
        if variable.avaliable : return variable
        
        return None
    
    def P(self,toke_list):
        
        try:
            params = pdr.params([toke_list[1]])
        
            if params.avaliable: return params
        
        except:
        
            return  None
    
    def T(self,token_list):
        
        # detects the kind of expression it is
        
        return 
    
    def N(self,token_list):
        return None  
    
    def O(self,token_list):
        return  
    
    def b(self,token_list):
        return  
    
    def B(self,token_list):
        return  
    
    def p(self,token_list):
        
        params = pdr.params(token_list)
        
        if params.avaliable: return params
        
        return None
    
    def if_(self,token_list):
        
        if_ = pdr.if_(token_list)
        
        if if_.avaliable : return if_
        
        return None
    
    def elif_(self,token_list):
        
        elif_= pdr.elif_(token_list)
        
        if elif_.avaliable : return elif_
        
        return  None

    def M(self,token_list):

        type_ = pdr.type_(token_list)
        protocol = pdr.protocol(token_list)
        function = pdr.def_function(token_list)
        
        if type_.avaliable: return type_
        
        if protocol.avaliable: return protocol
        
        if function.avaliable: return function
        
        return None
        
    def E(self,token_list):
        
        return 
    
    pass


