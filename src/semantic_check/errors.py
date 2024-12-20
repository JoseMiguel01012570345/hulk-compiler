from ..parser import production_class_representation as pcr

def selector(ast): # switch case
    
    type_errors = [ ( type_error , "type") , (protocol_error , "protocol") , (function_error , "def_function") , (let_error , "let" ) ]
    my_func = ""
    
    for element in type_errors:
        
        if element[1] == ast.id:
            my_func = element[0]
            return my_func

def instance_error(ast:pcr.ASTNode):
    
    error_type="type definition"
    error_description=f"type {ast.node.name} is not defined in scope"
    
    return error_type , error_description

def inheritence_error( ast_parent_inheritence , type_or_protocol:str):
    
    error_type = "inheritence"
    
    if type_or_protocol == "type":
        error_description = f"type { ast_parent_inheritence } could not be found"
    else:
        error_description = f"protocol {ast_parent_inheritence} could not be found"
    
    return error_type , error_description

def type_error( ast:pcr.type_ ):
    
    error_type = "type definition"
    error_description = f"type {ast.name} has been already defined"
    
    return error_type , error_description

def protocol_error( ast:pcr.protocol ) -> list:
    
    error_type = "protocol definition"
    error_description = f"protocol {ast.name} has been already defined"
    
    return error_type , error_description
    
def function_error( ast:pcr.def_function) -> list:
    
    error_type = "function definition"
    error_description = f"function {ast.name} has been already defined"
        
    return error_type , error_description

def let_error( ast:pcr.let) -> list:
    
    error_type = "variable definition"
    error_description = f"variable {ast.name} has been already defined"
    
    return error_type , error_description