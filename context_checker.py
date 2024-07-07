import production_class_representation as pcr
import networkx as nx
import matplotlib.pyplot as plt

def context_checker(ast:pcr.ASTNode=None , error_list=[] , graph:nx.DiGraph=None , printing=0 ):

    # graph = build_in(graph)
    
    solve_context( ast=ast , error_list=error_list  , graph=graph )
    
    if printing :
        nx.draw(graph, with_labels=True, arrows=True)
        
        plt.show()
    
    return
    
def solve_context( ast:pcr.ASTNode=None , error_list=[] , graph: nx.DiGraph= None , children=None , reference_node="type_Object" , all_let = False ):
    
    if children == None:
        children = ast.visitor_ast()    
    
    for child in children :
    
        if child != None:
            
            if all_let and child.id == "var":
                child.id = "let"
            
            # case 1: types , case 2: protocols , case 3: functions , case 4 : let
            if child.id == "type" or child.id == "protocol" or child.id == "def_function" or child.id == "let":
                
                error_list = def_node(graph,child,error_list , reference_node )
                def_children = def_node_children(child=child)
                
                if child.id != "let":
                    error_list = solve_context(child , error_list , graph  , def_children , reference_node= f"{child.id}_{child.name.name}" , all_let= all_let )
                    continue
                
                error_list = solve_context(child , error_list , graph  , def_children , reference_node , all_let )
                
                continue
            
            if child.id == "auto_call":
                
                error_list = solve_context(child , error_list , graph  , None , reference_node= "anonymus" , all_let= all_let )
                
                continue
            
            if child.id == "args" and ast.id != "while" and ast.id != "for" and ast.id != "if" and ast.id != "elif" :
                
                error_list = solve_context(child , error_list , graph  , None , reference_node , all_let=True  )
                continue
                    
            if child.id == "function_call": # check if exits
                error_list = function_call(graph,child,error_list , reference_node )
                error_list = solve_context(child , error_list , graph  , def_children , reference_node ,all_let )
                
                continue

            # check for existence
            if child.id == "var":
                error_list = variable(graph,child,error_list , reference_node )
                
            if child.id == "dot": # check if exits right_node inside left_node
                
                '''
                TODO: verifiy if in child.left_node type hierarchy exists child.right_node 
                
                for that we will check if there exist a path from child.left_node type to
                
                "child.right_node.id_child.right_node.name"
                
                '''
                left_node = ""
                right_node = ""
                
                # line and column most be of the left node
                line = ""
                column =""
                
                dot_case( graph , error_list , right_node , left_node , line , column )
            
            error_list = solve_context( child , error_list , graph , None , reference_node , all_let )
                
    return error_list

def dot_case(graph:nx.DiGraph , error_list:list , right_node="" , left_node="" , line= "" , column = "" ):
    
    if graph.has_edge( right_node , left_node):
        return error_list
    
    error_type = "attr definition"
    error_description = f"attr {left_node} could not be found at {right_node}"
    scope = { "line":line , "column":column }
    error_list.append({ "error_type": error_type , "error_description":error_description , "scope":scope })
    
    return error_list

def def_node_children(child:pcr.ASTNode):
    
    grand_son = child.visitor_ast()
    
    children = []
    
    if child.__dict__.__contains__("parent_name"):
        
        class aux:
            
            name = ""
            
            def __init__(self,my_name) -> None:
                self.name = my_name
        
        child.parent_name.name = aux(child.parent_name.name)
        child.parent_name.id = child.id
        child.parent_name.__dict__["inheritence"] = True
            
    children = [ item for item in grand_son if item != None and item.id != "var" ]
    
    return children

def def_node(graph:nx.DiGraph , ast:pcr.ASTNode , error_list:list , reference_node):
    
    scope = { "line":ast.line , "column":ast.column }
    
    if ast.__dict__.__contains__("inheritence") : # inheritence checking
        
        start_node= reference_node
        end_node = f"{ast.id}_{ast.name.name}"
            
        if graph.has_node(end_node) and nx.has_path( graph , start_node , end_node ):
            
            parent_node = f"{ast.parent.id}_{ast.parent.name.name}"
            graph.add_edge(parent_node , end_node)
            
            return error_list
        else:
            
            error_type , error_description = inheritence_error(ast)
            error_list.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
            
            return error_list
    error_type , error_description = selector(ast)(ast)
    
    # ask for an edge existence
    if graph.has_edge( reference_node , f"{ast.id}_{ast.name.name}"): # let has no name.name
        
        error_list.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
        return error_list
        
    
    new_node = f"{ast.id}_{ast.name.name}"
        
    graph.add_node(new_node)
    graph.add_edge( reference_node  , new_node)
    graph.add_edge( new_node ,reference_node )
    
    return error_list

def inheritence_error(ast:pcr.ASTNode):
    
    error_type = "inheritence"
    
    if ast.id == "type":
        error_description = f"type {ast.name.name} could not be found"
    else:
        error_description = f"protocol {ast.name.name} could not be found"
    
    return error_type , error_description

def selector(ast):
    
    type_errors = [ ( type_case , "type") , (protocol_case , "protocol") , (function_case , "def_function") , (let_case , "let" ) ]
    my_func = ""
    
    for element in type_errors:
        
        if element[1] == ast.id:
            my_func = element[0]
            return my_func
    
def type_case( ast:pcr.type_ ):
    
    error_type = "type definition"
    error_description = f"type {ast.name.name} has been already defined"
    
    return error_type , error_description

def protocol_case( ast:pcr.protocol ) -> list:
    
    error_type = "protocol definition"
    error_description = f"protocol {ast.name.name} has been already defined"
    
    return error_type , error_description
    
def function_case( ast:pcr.def_function) -> list:
    
    error_type = "function definition"
    error_description = f"function {ast.name.name} has been already defined"
        
    return error_type , error_description

def let_case( ast:pcr.let) -> list:
    
    error_type = "variable definition"
    error_description = f"variable {ast.name} has been already defined"
    
    return error_type , error_description

def variable(graph:nx.DiGraph, ast:pcr.variable , error_list:list , reference_node ):
    
    if graph.has_edge( reference_node , "let_"+ast.name):
        
        graph.add_edge( f"let_{ast.name}_{ast.hash_}" , f"var_{ast.name}_{ast.hash_}" )
        graph.add_edge( f"var_{ast.name}_{ast.hash_}" , f"let_{ast.name}_{ast.hash_}" )
        
        return error_list
    
    else:
        error_type = "variable usage"
        error_description = f"variable {ast.name} is used before assigned"    
        scope = { "line":ast.line , "column":ast.column }
        error_list.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
    
        return error_list

def function_call(graph:nx.DiGraph, ast:pcr.function_call , error_list:list , reference_node):
    
    if graph.has_edge( reference_node , "def_function"+ast.name.name):
        
        graph.add_edge( f"def_function_{ast.name.name}_{ast.hash_}" , f"function_call_{ast.name.name}_{ast.hash_}" )
        graph.add_edge( f"function_call_{ast.name.name}_{ast.hash_}" , f"def_function_{ast.name.name}_{ast.hash_}" )
        
        return error_list
    
    else:
        
        scope = { "line":ast.line , "column":ast.column }
        error_type = "function usage"
        error_description = f"function {ast.name.name} is used before declared"    
        error_list.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
    
        return error_list
        
def build_in(graph:nx.DiGraph):
    
    type_object = "type_Object"
    def_function_print = "def_function_print"
    type_Number = "type_Number"
    let_e = "let_e"
    let_PI = "let_PI"
    def_function_tan = "def_function_tan"
    def_function_cot = "def_function_cot"
    def_function_sqrt = "def_function_sqrt"
    def_function_sin = "def_function_sin"
    def_function_cos = "def_function_cos"
    def_function_log = "def_function_log"
    def_function_exp = "def_function_exp"
    def_function_rand = "def_function_rand"
    def_function_range = "def_function_range"
    type_String = "type_String"
    type_Boolean = "type_Boolean"
    
    
    graph.add_node(type_object)
    graph.add_node(def_function_print)    
    graph.add_edge( type_object , type_Number )
    graph.add_edge( type_object , type_Boolean )
    graph.add_edge( type_object , type_String )
    
    graph.add_node(type_Number)
    
    graph.add_node(def_function_cos)
    graph.add_edge( type_Number , def_function_cos )
    
    graph.add_node(def_function_cot)
    graph.add_edge( type_Number , def_function_cot )
    
    graph.add_node(def_function_exp)
    graph.add_edge( type_Number , def_function_exp )
    
    graph.add_node(def_function_log)
    graph.add_edge( type_Number , def_function_log )
    
    graph.add_node(def_function_rand)
    graph.add_edge( type_Number , def_function_rand )
    
    graph.add_node(def_function_sqrt)
    graph.add_edge( type_Number , def_function_sqrt )
    
    graph.add_node(def_function_range)
    graph.add_edge( type_Number , def_function_range )
    
    graph.add_node(def_function_tan)
    graph.add_edge( type_Number , def_function_tan )
    
    graph.add_node(def_function_sin)
    graph.add_edge( type_Number , def_function_sin )
    
    graph.add_node(let_e)
    graph.add_edge( type_Number , let_e )
    
    graph.add_node(let_PI)
    graph.add_edge( type_Number , let_PI )
    
    graph.add_node(type_String)
    graph.add_edge( type_String , def_function_print )
    graph.add_node(type_Boolean)
    
    return graph
