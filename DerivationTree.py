from EnumsTokensDefinition import TokenType, Type, Keyword
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES, SIMBOL_VALUES, OPERATOR_VALUES
from enum import Enum
from TokensDefinition import SimbolToken, OperatorToken, LiteralToken
import importing_file as impF

class NodeType(Enum):

    Variable = 0
    Number = 1
    String = 2
    Boolean = 3
    Function = 4
    Type = 5
    Undefined = 6

    pass

class DerivationTree:
    """
    This class defines the derivation tree of a grammar

    token: Token
    childs: list(DerivationTree)

    builder: constructor of the AST node class that will return

    """

    def __init__(self, label, childs, builder):

        self._token = label
        self._childs = childs
        self._builder = builder

        pass

    @property
    def IsLeaf(self):

        return len(self._childs) == 0

    @property
    def Childs(self):

        return [
            child
            for child in self._childs
            if not child.Type == TokenType.Simbol and not len(child.Text) == 0
        ]

    @property
    def IsRelevant(self):

        return (
            KEYWORD_VALUES.count(self.Text) > 0
            or SIMBOL_VALUES.count(self.Text) > 0
            or OPERATOR_VALUES.count(self.Text) > 0
        )

    @property
    def Type(self):

        try:
            return self._token.Type

        except Exception:
            return Type.NONE

    @property
    def Text(self):

        try:
            return self._token.Text

        except Exception:
            return self._token

    @property
    def Token(self):

        return self._token

    @property
    def ASTNode(self):

        return self._builder(self._token)

    @property
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

    pass

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
    @property
    def set_identifier(self,id):  
        
        self.id = id
        
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
    
class builder:

    def __init__(self, label ):
        
        feature = self.filter_feature(label)
        
        return feature

    def filter_feature(self,label):
        
        features = [('F',self.F) , ('P',self.P) , ('T',self.T) , ('N',self.N) ,
                    ('O',self.O) , ('b',self.b) , ('B',self.B) , ('p',self.p) , 
                    ('if',self.if_) , ('elif',self.elif_) , ('M',self.M) , ('Q',self.Q) ,
                    ('c',self.c) ]
        
        for item in features:
            
            if label == item[0]:
                return item[1]
        
    def inicializer(self , token_list ) -> list :
        
        features = []
        try:
            
            features.append( impF.pdr.function_call(token_list) )
            
            
            pass
        
        except:
            pass
        
        
        return
    
    def F(self ,toke_list:list):
        
        return impF.pdr.function_call(toke_list)
        
    def c(self,token_list):
        
        return impF.pdr.function_name(token_list)
    
    def P(self,toke_list):
        
        return impF.pdr.params(toke_list)
    
    def T(self,token_list):
        
        # detect the kind of expression it is
        
        return 
    
    def N(self,toke_list):
        
        return None  
    
    def O(self,toke_list):
        return  
    
    def b(self,toke_list):
        return  
    
    def B(self,toke_list):
        return  
    
    def p(self,toke_list):
        
        return impF.pdr.params(toke_list)
    
    def if_(self,toke_list):
        return  
    
    def elif_(self,toke_list):
        return  
    
    def M(self,toke_list):
        return  
    
    def Q(self,toke_list):
        return  
    
    def E(self,toke_list):
        return  
    
    pass


