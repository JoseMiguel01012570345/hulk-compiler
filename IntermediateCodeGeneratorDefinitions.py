from IntermediateCodeInterfaces import DeleteDuplicated,IFunctionCodeGenerator,IDataCodeGenerator,IExpressionCodeGenerator,ITypeCodeGenerator
from EnumIntermediateCodeDefinitions import IntermediateCodeType, ExpressionType

class DataNode(IDataCodeGenerator):
    
    def __init__(self,data,name):
        if not type(data) == str:
            raise Exception('los datos almacenados solo pueden ser de tipo string')
        self._data = data
        if not type(name) == str:
            raise Exception('La propiedad "name" debe ser string')
        self._name = name
        pass
    
    @property
    def Name(self):
        return f'data_{self._name}'
    
    @property
    def DataName(self):
        return self._name
    
    @property
    def Data(self):
        return self._data
    
    pass

class ValueNode(IDataCodeGenerator):
    
    def __init__(self,data):
        if type(data) == str:
            raise Exception('Los tipos string se deben instanciar como datos')
        self._data = data
        pass
    
    @property
    def Data(self):
        return self._data
    
    @property
    def Name(self):
        return str(self._data)
    
    @property
    def DataName(self):
        return str(self._data)
    
    @property
    def Template(self):
        return { 'DATA' : '' , 'TEMPLATE' : '' , 'LOCALS' : ''}
    
    pass

class ParamNode(IDataCodeGenerator):
    
    def __init__(self,name):
        self._name = name
        pass
    
    @property
    def Data(self):
        return self._name
        
    @property
    def Name(self):
        return self._name
    
    @property
    def DataName(self):
        return self._name
    
    @property
    def Template(self):
        return { 'DATA' : '' , 'TEMPLATE' : '' , 'LOCALS' : '' }
    
    pass

class ParamsNode(IDataCodeGenerator):
    
    def __init__(self,params):
        self._params = params
        pass
    
    @property
    def Data(self):
        return ''
    
    @property
    def Name(self):
        return ''
    
    @property
    def DataName(self):
        return ''
    
    @property
    def Template(self):
        return { 'DATA' : '' , 'TEMPLATE' : '' , 'LOCALS' : '' }
    
    pass

class BinaryExpressionNode(IExpressionCodeGenerator):
    
    def __init__(self,left,right,operator):
        self._left = left
        self._right = right
        self._operator = operator
        pass
    
    @property
    def Value(self):
        Id = hex(hash(f'{self._left.Value}_{self._operator}_{self._right.Value}'))
        return Id.split('x')[1]
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction
    
    @property
    def Locals(self):
        LOCALS = []
        
        if not self._left.Type == IntermediateCodeType.Data:
            
            for l in self._left.Locals:
                if LOCALS.count(l) == 0:
                    LOCALS.append(l)
                    pass
                pass
            
            if LOCALS.count(self._left.Value) == 0:
                LOCALS.append(self._left.Value)
                pass
            
            pass
        
        if not self._right.Type == IntermediateCodeType.Data:
            
            for l in self._right.Locals:
                if LOCALS.count(l) == 0:
                    LOCALS.append(l)
                    pass
                pass
            
            if LOCALS.count(self._right.Value) == 0:
                LOCALS.append(self._right.Value)
                pass
            
            pass
        
        return LOCALS
    
    @property
    def Template(self):
        data = ''
        for d in self.Data:
            data += d.Template['DATA']
            pass
        
        template = self._left.Template['TEMPLATE'] + self._right.Template['TEMPLATE']
        
        LOCALS = self._left.Template['LOCALS'] + ';' + self._right.Template['LOCALS'] + ';'
        
        if not self._left.Type == IntermediateCodeType.Data:
            LOCALS += f'LOCAL {self._left.Value};'
            pass
        
        if not self._right.Type == IntermediateCodeType.Data:
            LOCALS += f'LOCAL {self._right.Value}'
            pass
        
        template = DeleteDuplicated(template)
        LOCALS = DeleteDuplicated(LOCALS)
        
        return {
            'DATA' : data,
            'TEMPLATE' : f'{template}{self.Value} = {self._left.Value} {self._operator} {self._right.Value};',
            'LOCALS' : LOCALS
        }
    
    @property
    def Data(self):
        data = []
    
        if self._left.Type == IntermediateCodeType.Data and data.count(self._left) == 0:
            data.append(self._left)
            pass
        else:
            for d in self._left.Data:
                if data.count(d) > 0: continue
                data.append(d)
                pass
            pass
    
        if self._right.Type == IntermediateCodeType.Data and data.count(self._right) == 0:
            data.append(self._right)
            pass
        else:
            for d in self._right.Data:
                if data.count(d) > 0: continue
                data.append(d)
                pass
            pass
    
        return data
    
    pass

class UnaryExpressionNode(IExpressionCodeGenerator):
    
    def __init__(self,val,operator):
        self._operator = operator
        self._val = val
        pass
    
    @property
    def Value(self):
        Id = hex(hash(f'{self._operator}_{self._val.Value}'))
        return Id.split('x')[1]
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction
    
    @property
    def Data(self):
        data = []
    
        if self._val.Type == IntermediateCodeType.Data and data.count(self._val) == 0:
            data.append(self._val)
            pass
        else:
            for d in self._val.Data:
                if data.count(d) > 0: continue
                data.append(d)
                pass
            pass
        return data
    
    @property
    def Template(self):
        data = ''
        for d in self.Data:
            data += d.Template['DATA']
            pass
            
        
        template = self._val.Template['TEMPLATE']
        template = template.split(';')
        
        temp = []
        for t in template:
            if temp.count(t) == 0:
                temp.append(t)
                pass
            pass
        template = ''
        
        for t in temp:
            template += f'{t};'
            pass
        
        return { 'DATA' : data , 'TEMPLATE' : f'{template}{self.Value} = {self._operator} {self._val.Value}' }
    
    pass

class AssigmentExpression(BinaryExpressionNode):
    
    def __init__(self,val_address,expression):
        self._val = val_address
        self._expression = expression
        pass
    
    @property
    def Value(self):
        return self._val
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction
    
    @property
    def Locals(self):
        return []
    
    @property
    def Data(self):
        if self._expression.Type == IntermediateCodeType.Data:
            return [self._expression]
        return []
    
    @property
    def Template(self):
        template = ''
        if self._expression.Type == IntermediateCodeType.Data:
            code = self._expression.Template['TEMPLATE']
            template = f'{code}{self.Value} = {self._expression.Value};'
            pass
        elif self._expression.Type == IntermediateCodeType.FunctionInvocation:
            template = f'{self.Value} = CALL {self._expression.Name};'
            pass
        else:
            template = self._expression.Template['TEMPLATE']
            template = template.replace(self._expression.Value,self.Value)
            pass
        return {
            'DATA': '',
            'TEMPLATE' : f'{template}',
            'LOCALS' : ''
        }
    
    pass

class AllocateExpression(IExpressionCodeGenerator):
    
    def __init__(self,address,size):
        self._address = address
        self._size = size
        pass
    
    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction
    
    @property
    def Locals(self):
        return []
    
    @property
    def Data(self):
        return []
    
    @property
    def Template(self):
        return {
            'DATA' : '',
            'TEMPLATE' : f'{self.Value} = ALLOCATE {self._size};',
            'LOCALS' : ''
        }
    
    pass
class GetAttributeExpression(IExpressionCodeGenerator):
    
    def __init__(self,return_address,data,attribute):
        self._return = return_address
        self._data = data
        self._attribute = attribute
        pass
    
    @property
    def Value(self):
        return self._return
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction
    
    @property
    def Locals(self):
        return [self._return]
    
    @property
    def Data(self):
        return []
    
    @property
    def Template(self):
        return {
            'DATA' : '',
            'TEMPLATE' : f'{self._return} = GETATTR {self._data} {self._attribute};',
            'LOCALS' : ''
        }
    
    pass

class ArrayExpression(IExpressionCodeGenerator):
    def __init__(self, address, size):
        self._address = address
        self._size = size

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction

    @property
    def Locals(self):
        return [self._address]

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"{self._address} = ARRAY {self._size};",
            "LOCALS": "",
        }

    pass

class TypeofExpression(IExpressionCodeGenerator):
    def __init__(self, address, value):
        self._address = address
        self._value = value

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction

    @property
    def Locals(self):
        return [self._address]

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"{self.Value} = TYPEOF {self._value};",
            "LOCALS": "",
        }

    pass

class SetAttributeExpression(IExpressionCodeGenerator):
    def __init__(self, address, data, attribute):
        self._address = address
        self._data = data
        self._attribute = attribute

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.PrintInstruction

    @property
    def Locals(self):
        return []

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"SETATTR {self._address} {self._data} {self._attribute};",
            'LOCALS' : ''
        }

    pass

class GetIndexExpression(IExpressionCodeGenerator):

    def __init__(self, return_address, data, value):
        self._return = return_address
        self._data = data
        self._value = value
        pass

    @property
    def Value(self):
        return self._return
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction

    @property
    def Locals(self):
        return [self._return]

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"{self._return} = GETINDEX {self._data} {self._value};",
            'LOCALS' : ''
        }

    pass

class SetIndexExpression(IExpressionCodeGenerator):

    def __init__(self, return_address, data, value):
        self._return = return_address
        self._data = data
        self._value = value
        pass

    @property
    def Value(self):
        return self._return
    
    @property
    def ExpressionType(self):
        return ExpressionType.PrintInstruction

    @property
    def Locals(self):
        return []

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"SETINDEX {self._return} {self._data} {self._value};",
            'LOCALS' : ''
        }

    pass

class FunctionInvocationNode(IExpressionCodeGenerator):
    
    def __init__(self,address,function_name):
        self._address = address
        self._function = function_name
        pass
    
    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction
    
    @property
    def Locals(self):
        return []
    
    @property
    def Data(self):
        return []
    
    @property
    def Template(self):
        return {
            'DATA' : '',
            'TEMPLATE' : f'{self.Value} = CALL {self._function};',
            'LOCALS' : ''
        }
    
    pass

class FunctionDynamicInvocationNode(IExpressionCodeGenerator):
    
    def __init__(self, address, function_name, typeof):
        self._address = address
        self._function = function_name
        self._type = typeof
        pass

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction

    @property
    def Locals(self):
        return [self._address]

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"{self.Value} = VCALL {self._type} {self._function};",
            "LOCALS": "",
        }

    pass

class ArgExpression(IExpressionCodeGenerator):
    def __init__(self, address):
        self._address = address
        pass

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReadInstruction

    @property
    def Locals(self):
        return []

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"ARG {self._address};",
            "LOCALS": "",
        }

    pass

class LengthExpression(IExpressionCodeGenerator):
    def __init__(self, address, value):
        self._address = address
        self._value = value

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction

    @property
    def Locals(self):
        return [self._address]

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"{self._address} = LENGTH {self._value};",
            "LOCALS": "",
        }

    pass

class ConcatExpression(IExpressionCodeGenerator):
    def __init__(self, address, first, second):
        self._address = address
        self._first = first
        self._second = second

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction

    @property
    def Locals(self):
        return [self._address]

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"{self._address} = CONCAT {self._first} {self._second};",
            "LOCALS": "",
        }

    pass

class PrefixExpression(IExpressionCodeGenerator):
    def __init__(self, address, value, prefix):
        self._address = address
        self._value = value
        self._prefix = prefix

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction

    @property
    def Locals(self):
        return [self._address]

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"{self._address} = PREFIX {self._value} {self._prefix};",
            "LOCALS": "",
        }

    pass

class SubStringExpression(IExpressionCodeGenerator):
    def __init__(self, address, value, index):
        self._address = address
        self._value = value
        self._index = index

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction

    @property
    def Locals(self):
        return [self._address]

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"{self._address} = SUBSTRING {self._value} {self._index};",
            "LOCALS": "",
        }

    pass

class StringCastExpression(IExpressionCodeGenerator):
    def __init__(self, address, value):
        self._address = address
        self._value = value

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction

    @property
    def Locals(self):
        return [self._address]

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"{self._address} = STR {self._value};",
            "LOCALS": "",
        }

    pass

class ReadExpression(IExpressionCodeGenerator):
    def __init__(self, address):
        self._address = address

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReadInstruction

    @property
    def Locals(self):
        return [self._address]

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"{self._address} = READ;",
            "LOCALS": "",
        }

    pass

class PrintExpression(IExpressionCodeGenerator):
    def __init__(self, address):
        self._address = address

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.PrintInstruction

    @property
    def Locals(self):
        return []

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"PRINT {self._address};",
            "LOCALS": "",
        }

    pass

class GoToExpression(IExpressionCodeGenerator):
    def __init__(self, address):
        self._address = address

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.JumpInstruction

    @property
    def Locals(self):
        return []

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"GOTO {self._address};",
            "LOCALS": "",
        }

    pass

class IfGoToExpression(IExpressionCodeGenerator):
    def __init__(self, address, bool_ex):
        self._address = address
        self._bool_ex = bool_ex

    @property
    def Value(self):
        return self._address
    
    @property
    def ExpressionType(self):
        return ExpressionType.JumpInstruction

    @property
    def Locals(self):
        return []

    @property
    def Data(self):
        return []

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"IF {self._bool_ex} GOTO {self._address};",
            "LOCALS": "",
        }

    pass

class LabelExpression(IExpressionCodeGenerator):
    def __init__(self, address):
        self._address = address

    @property
    def Value(self):
        return self._address

    @property
    def Locals(self):
        return []

    @property
    def Data(self):
        return []

    @property
    def ExpressionType(self):
        return ExpressionType.JumpInstruction

    @property
    def Template(self):
        return {
            "DATA": "",
            "TEMPLATE": f"LABEL {self._address};",
            "LOCALS": "",
        }

    pass

class BodyNode(IExpressionCodeGenerator):
    
    def __init__(self,expressions):
        self._expressions = expressions
        pass
    
    @property
    def Value(self):
        return self._expressions[len(self._expressions) - 1].Value
    
    @property
    def Locals(self):
        LOCALS = []
        for expression in self._expressions:
            for local in expression.Locals:
                if LOCALS.count(local) == 0:
                    LOCALS.append(local);
                    pass
                pass
            if expression.ExpressionType == ExpressionType.ReturnInstruction:
                LOCALS.append(expression.Value)
                pass
            pass
        return LOCALS
    
    @property
    def ExpressionType(self):
        return ExpressionType.ReturnInstruction
    
    @property
    def Data(self):
        data = []
        for expression in self._expressions:
            for d in expression.Data:
                if data.count(d) == 0:
                    data.append(d)
                    pass
                pass
            pass
        return data
    
    @property
    def Template(self):
        data = ''
        for d in self.Data:
            data += d.Template['DATA']
            pass
        
        template = ''
        LOCALS = ''
        
        for local in self.Locals:
            LOCALS += f'LOCAL {local};'
        
        for expression in self._expressions:
            if not expression.Type == IntermediateCodeType.Expression: continue
            template += expression.Template['TEMPLATE']
            LOCALS += expression.Template['LOCALS']
            pass
        
        template = DeleteDuplicated(template)
        LOCALS = DeleteDuplicated(LOCALS)
        
        return {
            'DATA' : data,
            'TEMPLATE' : f'{template}',
            'LOCALS' : LOCALS
        }
    
    pass

class TypeNode(ITypeCodeGenerator):
    
    def __init__(self,name,*attributes,**methods):
        self._attributes = attributes
        self._methods = methods
        self._name = name
        pass

    @property
    def Attributes(self):
        return self._attributes
    
    @property
    def Methods(self):
        return self._methods
    
    @property
    def Name(self):
        return self._name
    
    pass

class FunctionNode(IFunctionCodeGenerator):
    
    def __init__(self,name,body,return_address,params):
        self._name = name
        self._params = params
        self._body = body
        self._return = return_address
        self.ExpressionType = IntermediateCodeType.Function
        pass
    
    @property
    def Body(self):
        return self._body
    
    @property
    def Name(self):
        return self._name
    
    @property
    def Params(self):
        return self._params
    
    @property
    def ReturnAddress(self):
        return self._return
    
    pass
