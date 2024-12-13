<<<<<<< HEAD
from EnumIntermediateCodeDefinitions import IntermediateCodeType
from IntermediateCodeGeneratorDefinitions import *

class CilTree:
    
    def __init__(self,node,childs):
        if type(node) == CilTree:
            self._node = node._node
            pass
        else:
            self._node = node
            pass
        self._childs = childs
        pass
    
    @property
    def Functions(self):
        """
        retorna todos los nodos que son funciones
        """
        functions = []
        for child in self._childs:
            for function in child.Functions:
                if functions.count(function) == 0:
                    functions.append(function)
                    pass
                pass
            pass
        
        if self._node.Type == IntermediateCodeType.Function and functions.count(self._node.Name) == 0:
            functions.append(self._node)
            pass
        
        return functions
    
    @property
    def Data(self):
        """
        retorna todos los datos string usados
        """
        
        data = []
        for child in self._childs:
            for d in child.Data:
                if data.count(d) == 0:
                    data.append(d)
                    pass
                pass
            pass
        
        if self._node.Type == IntermediateCodeType.Function:
            for d in self._node.Body.Data:
                if type(d) == DataNode and data.count(d) == 0:
                    data.append(d)
                    pass
                pass
            pass
        
        return data
    
    @property
    def Types(self):
        
        types = []
        
        for child in self._childs:
            for t in child.Types:
                if types.count(t) == 0:
                    types.append(t)
                    pass
                pass
            pass
        
        if self._node.Type == IntermediateCodeType.Type and types.count(self._node) == 0:
            types.append(self._node)
            pass
        
        return types
    
    @property
    def DataDefinitions(self):
        definition = '.DATA\n\n'
        for data in self.Data:
            definition += data.Template['DATA'] + '\n'
            pass
        return definition + '\n\n'
    
    @property
    def TypesDefinitions(self):
        definition = '.TYPES\n\n'
        for t in self.Types:
            d = t.Template['TEMPLATE'].split(';')
            definition += d[0] + '\n'
            for i in range(1,len(d) - 1):
                definition += d[i] + ';\n'
                pass
            definition += d[len(d) - 1] + '\n\n'
            pass
        return definition + '\n\n'
    
    @property
    def FunctionsDefinitions(self):
        definition = '.CODE\n\n'
        
        for function in self.Functions:
            d = function.Template['TEMPLATE'].split(';')
            definition += d[0] + ';\n'
            for i in range(1,len(d) - 1):
                if len(d[i]) > 0:
                    definition += d[i] + ';\n'
                    pass
                pass
            definition += d[len(d) - 1] + '\n\n'
            pass
        
        return definition
    
    @property
    def Code(self):
        
        datas = self.DataDefinitions
        types = self.TypesDefinitions
        codes = self.FunctionsDefinitions
        
        return datas + types + codes
    
    pass

################ CIL NODE-BUILDERS FUNCTIONS #######################

def BinaryExpressionNodeBuilder(node):
    
    left = ExpressionNodeBuilder(node.left)
    right = ExpressionNodeBuilder(node.right)
    
    return BinaryExpressionNode(left,right,node.id)

def UnaryExpressionNodeBuilder(node):
    if node.id in ['let','new']:
        address = ExpressionNodeBuilder(node.right).Value
        return AllocateExpression(address,128)
    val = ExpressionNodeBuilder(node.right).Value
    return UnaryExpressionNode(val,node.id)

def FunctionCallExpressionNodeBuilder(node):
    return FunctionInvocationNode(str(hex(hash(node))),node.name)

def VarExpressionNodeBuilder(node):
    return AllocateExpression(node.name,128)

def LiteralExpressionNodeBuilder(node):
    if type(node.value) == str:
        return DataNode(node.value,str(hex(hash(node))))
    return ValueNode(node.value)

def BodyNodeBuilder(node):
    if type(node) == list:
        expressions = [ExpressionNodeBuilder(expression) for expression in node]
        return BodyNode(expressions)
    return BodyNode([ExpressionNodeBuilder(node)])

def DefFunctionNodeBuilder(node):
    body = None
    if type(node.body) == list:
        body = BodyNodeBuilder(node.body)
        pass
    else:
        body = BodyNodeBuilder([node.body])
        pass
    if type(node.args) == list:
        return FunctionNode(node.name,body,body.Value,[ParamNode(param.left.name) for param in node.args])
    if node.args == None:
        return FunctionNode(node.name,body,body.Value,[])
    return FunctionNode(node.name,body,body.Value,[ParamNode(node.args.left.name)])

def LetInNodeBuilder(node):
    left = ExpressionNodeBuilder(node.left)
    right = ExpressionNodeBuilder(node.right)
    body = BodyNode([left,right])
    return FunctionNode('let',body,body.Value,[])

def ForNodeBuilder(node):
    body = None
    if node.body.id == 'block':
        body = BodyNodeBuilder(node.body.expressions)
        pass
    else:
        body = BodyNodeBuilder(node.body)
        pass
    return FunctionNode('for',body,body.Value,[])

def ExpressionNodeBuilder(node):
    builders = {
        'FunctionCall' : FunctionCallExpressionNodeBuilder,
        'var' : VarExpressionNodeBuilder,
        'literal' : LiteralExpressionNodeBuilder,
        'function_form' : DefFunctionNodeBuilder,
        'in' : LetInNodeBuilder,
        'for' : ForNodeBuilder,
        'block' : BlockCilBuilder
        
    }
    
    if list(builders.keys()).count(node.id) > 0:
        return builders[node.id](node)
    
    if node.id in ['!','++','--','new','let']:
        return UnaryExpressionNodeBuilder(node)
    return BinaryExpressionNodeBuilder(node)

def BlockCilBuilder(node):
    expressions = None
    if type(node.expressions) == list:
        expressions = [ExpressionNodeBuilder(expression) for expression in node.expressions]
        pass
    else:
        expressions = [ExpressionNodeBuilder(node.expressions)]
        pass
    return BodyNode(expressions)

def DefFunctionCilBuilder(node):
    return CilTree(DefFunctionNodeBuilder(node),[])

def ASTNodeCilBuilder(node):
    builders = {
        'block' : BlockCilBuilder,
        'function_form' : DefFunctionCilBuilder,
    }
    
    if list(builders.keys()).count(node.id) == 0:
        return CilTree(ExpressionNodeBuilder(node),[])
    
    return CilTree(builders[node.id](node),[])

def ASTCilBuilder(ast):
    cilnode = ASTNodeCilBuilder(ast)
    childs = ast.visitor()
    cils = []
    if type(childs) == list:
        for child in childs:
            if not child == None:
                cils.append(ASTNodeCilBuilder(child))
                pass
            pass
        pass
    elif not childs == None:
        cils.append(ASTNodeCilBuilder(childs))
        pass
    trees = []
    for cil in cils:
        if type(cil) == CilTree:
            trees.append(cil)
            pass
        pass
    return CilTree(cilnode,trees)

# ################################COMPROBANDO#######################
=======

class CilTree:

    

    pass    
>>>>>>> jhosef
