import production_class_representation as pcr

def context_checker( ast:pcr.ASTNode=None , error_list=[] ):
    
    children = ast.visitor_ast()
    
    stack = []
    
    stack.extend(children)
    
    def_nodes = build_in()
    
    verified_node= []
    
    while len(stack) != 0:
        
        child = stack[0]
        
        if child != None:
            
            grand_son = child.visitor_ast()
            stack.extend( grand_son )
            
            last_type_seen = ""
            last_protocol_seen = ""
            
            if child.def_node: # improve context
                
                # case 1: types
                # case 2: protocols
                # case 3: functions
                # case 4 : variables
                
                pass
            
            if child.id == "var": # check if exits
                pass
            
            if child.id == "function_call": # check if exits
                pass
            
            if child.id == "dot": # check if exits the right_node inside the left_node
                pass
            
        stack.pop(0)

def type_case( def_node:list , ast:pcr.type_ , error_list:list , error_type , error_description ):
    
    if def_node.__contains__ ("type_" + ast.name.name):
        
        scope = { "line":ast.line , "column":ast.column }
        error_list.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
        
        return 

def protocol_case( def_node:list , ast:pcr.type_ , error_list:list , error_type , error_description ) -> list:
    
    if def_node.__contains__ ("protocol_" + ast.name.name):
        
        scope = { "line":ast.line , "column":ast.column }
        error_list.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
        
        return 
    

def function_case() -> list:
    return

def variable_case() -> list:
    return
        
def build_in():
    
    return  [
             'type_Object' ,
             'type_Number' ,
             'type_String' ,
             'type_Boolean' ,
             'def_function_tan' ,
             "def_function_cot" ,
             "def_function_sqrt" ,
             "def_function_sin" ,
             "def_function_cos" ,
             "def_function_log" ,
             "def_function_exp" ,
             "def_function_rand" ,
             "def_function_range" ,
             "def_function_print" ,
             "let_E" ,
             "let_PI" ,
             "let_self",    
             ]
    
    