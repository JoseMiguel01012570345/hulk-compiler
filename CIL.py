from EnumIntermediateCodeDefinitions import IntermediateCodeType
from IntermediateCodeGeneratorDefinitions import *

class CilTree:
    
    def __init__(self,node,childs):
        self._node = node
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

def FunctionCallNodeCilBuilder(node):
    tree = FunctionInvocationNode(node.name)
    return CilTree(tree,[])

def ParamsNodeCilBuilder(node):
    params = []
    for param in node.parameters:
        params.append(ParamNode(param))
        pass
    return CilTree(ParamsNode(params),[])

def BinaryASTNodeCilBuilder(node):
    return CilTree(BinaryExpressionNode(node.left,node.right,node.id),[])
        
def UnaryASTNodeCilBuilder(node):
    return CilTree(UnaryExpressionNode(node.right,node.id),[])

def VariableASTNodeCilBuilder(node):
    return CilTree(AllocateExpression(node.name,128),[])

def ExpressionNodeCilBuilder(node):
    unary_expressions_id = ['!','++','--','new','let']
    
    if node.id in unary_expressions_id:
        return UnaryExpressionNode(node.right,node.id)
            
    return BinaryExpressionNode(node.left,node.right,node.id)

def BodyASTNodeCilBuilder(node):
    
    expressions = []
    for expression in node.expressions:
        expressions.append(ExpressionNodeCilBuilder(expression))
        pass
    
    return CilTree(BodyNode(expressions),[])

def IfASTNodeCilBuilder(node):
    label = hex(hash(str(node.id) + str(node.condition.Value)))
    Label = LabelExpression(label)
    if_node = IfGoToExpression(label,f'!{node.Value}')
    expressions = []
    for expression in node.expressions:
        expressions.append(ExpressionNodeCilBuilder(expression))
        pass
    body = BodyNode(expressions)
    return CilTree(if_node,[CilTree(body,[]),Label])

def ElifASTNodeCilBuilder(node):
    return IfASTNodeCilBuilder(node)

def ElseASTNodeCilBuilder(node):
    label = hex(hash(str(node.id) + str(node.condition.Value)))
    Label = LabelExpression(label)
    expressions = []
    for expression in node.body.expressions:
        expression.append(ExpressionNodeCilBuilder(expression))
        pass
    return CilTree(BodyNode([Label].__add__(expressions)),[])

def DefFunctionASTNodeCilBuilder(node):
    params = ParamsNodeCilBuilder(node.args)
    body = BodyNode(node.body)
    return CilTree(FunctionNode(node.name,body,node.name,params),[])
    
def TypeASTNodeCilBuilder(node):
    attributes = []
    methods = {}
    counter = 1
    for expression in node.body.expressions:
        if expression.id == '=':
            attributes.append(ParamNode(expression.left))
            pass
        elif expression.id == 'function_form':
            methods[f'{node.name}_function{counter}'] = DefFunctionASTNodeCilBuilder(expression)
            counter += 1
            pass
        pass
    
    return CilTree(TypeNode(node.name,attributes,methods),[])

def ProtocolASTNodeCilBuilder(node):
    return None

def VectorASTNodeCilBuilder(node):
    address = str(hex(hash(node)))
    return CilTree(ArrayExpression(address,128),[])

def LiteralASTNodeCilBuilder(node):
    if type(node.value) == str:
        return CilTree(DataNode(node.id,node.value),[])
    return CilTree(ValueNode(node.value),[])
    
def IndexingASTNodeCilBuilder(node):
    return CilTree(GetIndexExpression(str(hex(hash(node))),node.name,node.index),[])

def WhileASTNodeCilBuilder(node):
    label = str(hex(hash(node)))
    Label = LabelExpression(label)
    expressions = []
    for expression in node.expressions:
        expressions.append(ExpressionNodeCilBuilder(expression))
        pass
    
    expressions = [Label].__add__(expressions)
    expressions.append(IfGoToExpression(label,node.condition.value))
    
    body = BodyNode(expressions)
    
    return CilTree(body,[])

def ForASTNodeCilBuilder(node):
    return WhileASTNodeCilBuilder(node)

def ASTNodeCilBuilder(node):
    builders = {
        'FunctionCall' : FunctionCallNodeCilBuilder,
        'params' : ParamsNodeCilBuilder,
        'var' : VariableASTNodeCilBuilder,
        'if' : IfASTNodeCilBuilder,
        'elif' : ElifASTNodeCilBuilder,
        'else' : ElseASTNodeCilBuilder,
        'function_form' : DefFunctionASTNodeCilBuilder,
        'type' : TypeASTNodeCilBuilder,
        'protocol' : ProtocolASTNodeCilBuilder,
        'vector' : VectorASTNodeCilBuilder,
        'literal' : LiteralASTNodeCilBuilder,
        'index' : IndexingASTNodeCilBuilder,
        'while' : WhileASTNodeCilBuilder,
        'for' : ForASTNodeCilBuilder,
        'block' : BodyASTNodeCilBuilder
    }
    
    return builders[node.id](node)

def ASTCilBuilder(ast):
    cilnode = ASTNodeCilBuilder(ast)
    try:
        childs = [ASTCilBuilder(child) for child in ast.visitor() if not child == None]
        cilnode._childs = childs
        pass
    except Exception:
        if not ast.visitor() == None:
            cilnode._childs = [ASTCilBuilder(ast.visitor())]
            pass
        pass
    return cilnode

# ################################COMPROBANDO#######################