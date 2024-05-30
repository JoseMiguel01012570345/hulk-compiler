from EnumIntermediateCodeDefinitions import IntermediateCodeType

def DeleteDuplicated(l):
    l = l.split(';')
    temp = []
    
    for i in l:
        if temp.count(i) == 0:
            temp.append(i)
            pass
        pass
    
    l = ''
    for t in temp:
        l += f'{t};'
        pass
    
    return l

class ICodeIntermediateGenerator:
    
    @property
    def Template(self):
        """
        Template() -> dict<DATA,TEMPLATE>
        Genera el codigo de todos datos que se usaran a la vez que 
        devuelve la plantilla de codigo intermedio correspondiente
        DATA: definicion de los datos usados
        LOCALS: variables locales
        TEMPLATE: codigo generado
        """

        raise NotImplementedError()
    
    @property
    def Type(self):
        """
        retorna el tipo de codigo que generara
        """
        raise NotImplementedError()
    
    @property
    def Code(self):
        """
        retorna el codigo del nodo que representa
        """
        data,locals_vars,code = self.Template['DATA'],self.Template['LOCALS'],self.Template['TEMPLATE']

        d_list = data.split(';')
        l_list = locals_vars.split(';')
        c_list = code.split(';')

        Code = {}
        code = ''

        for d in d_list:
            if len(d) > 0:
                code += f'{d};\n'
                pass
            pass
        
        Code['.DATA'] = ''
        Code['.DATA'] += code
        
        code = ''
        
        for l in l_list:
            if len(l) > 0:
                code += f'{l};\n'
                pass
            pass
        
        if len(code) > 0:
            code += '\n'
            pass
        
        for c in c_list:
            if len(c) > 0:
                code += f'{c};\n'
                pass
            pass
        
        Code['.TYPES'] = ''
        Code['.CODE'] = ''
        
        pos = code.rindex(';')
        if self.Type == IntermediateCodeType.Type:
            code = code[:pos] + code[pos + 1:]
            Code['.TYPES'] += code
            pass
        else:
            code = code[:pos] + code[pos + 1:]
            Code['.CODE'] += code
            pass
        
        return Code
    
    pass

class IDataCodeGenerator(ICodeIntermediateGenerator):
    
    @property
    def Name(self):
        """
        retorna la direccion donde se almacena el valor de string
        """
        
        raise NotImplementedError()
    
    @property
    def Value(self):
        return self.DataName
    
    @property
    def DataName(self):
        """
        retorna la referencia al dato que esta guardando
        """
        
        raise NotImplementedError()
    
    @property
    def Type(self):
        return IntermediateCodeType.Data
    
    @property
    def Data(self):
        """
        retorna el valor del dato guardado
        """
        raise NotImplementedError()
    
    @property
    def Template(self):
        return {
            'DATA' : f'{self.Name} = "{self.Data}";',
            'TEMPLATE': f'{self.DataName} = LOAD {self.Name};',
            'LOCALS' : f'LOCAL {self.DataName};'
        }
    
    pass

class IExpressionCodeGenerator(ICodeIntermediateGenerator):
    
    @property
    def Value(self):
        """
        retorna el lugar donde se almacenara el resultado de la expression
        """
        
        raise NotImplementedError()
        
    @property
    def Locals(self):
        """
        retorna las variables locales de la expression
        """
        
        raise NotImplementedError()
    
    @property
    def Type(self):
        return IntermediateCodeType.Expression
    
    @property
    def Data(self):
        """
        retorna todos los nodos de datos que se usaran en el cuerpo
        """
        
        raise NotImplementedError()
    
    @property
    def ExpressionType(self):
        """
        retorna el tipo de expression
        """
        raise NotImplementedError()

    pass

class IBodyCodeGenerator(IExpressionCodeGenerator):
    
    @property
    def Type(self):
        return IntermediateCodeType.Body
    
    pass

class ITypeCodeGenerator(ICodeIntermediateGenerator):
    
    @property
    def Type(self):
        return IntermediateCodeType.Type
    
    @property
    def Attributes(self):
        """
        retorna los atributos del tipo en cuestion
        """
        
        raise NotImplementedError()
    
    @property
    def Methods(self):
        """
        retorna los metodos definidos en este tipo
        """
        
        raise NotImplementedError()
    
    @property
    def Name(self):
        """
        retorna el nombre del tipo
        """
        
        raise NotImplementedError()
    
    @property
    def Template(self):
        template = f'type {self.Name} ' + '{\n'
        
        for attribute in self.Attributes:
            template += f'\tattribute {attribute};'
            pass
        
        template += '\n'
        
        for method in self.Methods.keys():
            template += f'\tmethod {method} : {self.Methods[method]};'
            pass
        
        template += '}'
        
        return {
            'DATA' : '',
            'TEMPLATE' : template,
            'LOCALS' : ''
        }
    
    pass

class IFunctionCodeGenerator(ITypeCodeGenerator):
    
    @property
    def Body(self):
        """
        retorna el nodo asociado al cuerpo de la funcion
        """
        
        raise NotImplementedError()
    
    @property
    def Type(self):
        return IntermediateCodeType.Function
    
    @property
    def Name(self):
        """
        retorna el nombre de la funcion
        """
        
        raise NotImplementedError()
    
    @property
    def Params(self):
        """
        list(str)
        retorna los parametros que recibe la funcion
        """
        
        raise NotImplementedError()
    
    @property
    def Data(self):
        """
        retorna toda la data generada por la funcion
        """
        return self.Body.Data
    
    @property
    def Locals(self):
        """
        retorna todas las variables locales que se usaran
        """
        return self.Body.Locals
    
    @property
    def ReturnAddress(self):
        """
        retorna la direccion de retorno
        """
        raise NotImplementedError()
    
    @property
    def Value(self):
        """
        retorna la direccion donde se guardara el resultado
        """
        return self.Body.Value
    
    @property
    def Template(self):
        
        template = f'function {self.Name} ' + '{\n'
        
        for param in self.Params:
            template += f'\tPARAM {param.Name};'
            pass
        
        template += '\n'
        
        for local in self.Body.Template['LOCALS'].split(';'):
            if len(local) == 0: continue
            template += f'\t{local};'
            pass
        
        template += '\n'
        
        code = self.Body.Template['TEMPLATE'].split(';')
        
        for instruction in code:
            if len(instruction) == 0: continue
            template += f'\t{instruction};'
            pass
        
        template += f'\tRETURN {self.ReturnAddress};'
        
        template += '\n}'
        
        data = self.Body.Template['DATA']
        
        return { 'DATA' : data , 'TEMPLATE' : template , 'LOCALS' : ''}
        
    pass