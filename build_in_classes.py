from production_class_representation import ASTNode

class Object(ASTNode):
    
    anotated_type = 'Object'
    name = 'Object'
    
    def __init__(self , anothed_type='Object' , name='Object', id_='super_class' ) -> None:
        
        self.anotated_type = anothed_type
        self.name = name
        self.set_identifier(id_)
    
    pass

class Number(Object):
    
    def __init__(self, anothed_type= 'Number' , name= 'Number',id_= 'build_in') -> None:
        super().__init__(anothed_type, name,id_)
    
    pass

class Boolean(Object):
    
    def __init__(self, anothed_type= 'Boolean' , name= 'Boolean',id_= 'build_in') -> None:
        super().__init__(anothed_type, name,id_)
    
    pass

class String(Object):
    
     def __init__(self, anothed_type= 'String' , name= 'String',id_= 'build_in') -> None:
        super().__init__(anothed_type, name,id_)
 