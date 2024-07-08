import production_class_representation as pcr
import networkx as nx
import matplotlib.pyplot as plt

def context_checker(ast:pcr.ASTNode=None , error_list=[] , printing=0 ):

    graph = nx.DiGraph()
    
    # graph = build_in(graph)
    
    ast.id += " ROOT"
        
    solve_context( ast=ast , error_list=error_list  , graph=graph )
    
    if printing :
        print_graph(graph=graph)
    
    return graph
    
def solve_context( ast:pcr.ASTNode=None , error_list=[] , graph: nx.DiGraph= None , children=None , reference_node="type_Object" , all_let = False , last_referent_node="" ):
    
    if children == None:
        children = ast.visitor_ast()    
    
    for child in children :
    
        if child != None:
            
            if all_let and child.id == "var":
                child.id = "let"
            
            # case 1: types , case 2: protocols , case 3: functions , case 4 : let
            if child.id == "type" or child.id == "protocol" or child.id == "def_function" or child.id == "let":
                
                error_list = def_node_error(graph,child,error_list , reference_node , last_referent_node )
                
                def_children = def_node_children(child=child)
                
                if child.id != "let":
                    
                    new_referent_node =f"{child.id}_{child.name.name}"
                    
                    graph = build_graph( graph=graph , parent=ast , child=child , reference_node=new_referent_node , last_reference_node=reference_node , chift=1 )
                    
                    error_list = solve_context(child , error_list , graph  , def_children , reference_node=new_referent_node , all_let= all_let , last_referent_node=reference_node )
                    continue
                
                graph = build_graph( graph=graph , parent=ast , child=child , reference_node=reference_node , last_reference_node=last_referent_node )
                
                error_list = solve_context(child , error_list , graph  , def_children , reference_node , all_let , last_referent_node )
                continue
            
            graph = build_graph( graph=graph , parent=ast , child=child , reference_node=reference_node , last_reference_node=last_referent_node )
            
            if child.id == "auto_call":
                
                error_list = solve_context(child , error_list , graph  , None , reference_node= "anonymus" , all_let= all_let ,last_referent_node=last_referent_node)
                continue
            
            if child.id == "args" and ast.id != "while" and ast.id != "for" and ast.id != "if" and ast.id != "elif" :
                
                error_list = solve_context(child , error_list , graph  , None , reference_node , all_let=True , last_referent_node=last_referent_node )
                continue
                    
            if child.id == "function_call": # check if exits
                
                error_list = function_call(graph,child,error_list , reference_node )
                children_function_call = def_node_children(child=child)
                
                error_list = solve_context( child , error_list , graph , children_function_call , reference_node , all_let , last_referent_node )
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
                
                dot_case( graph , error_list , right_node , left_node , line , column , last_referent_node)
            
            error_list = solve_context( child , error_list , graph , None , reference_node , all_let , last_referent_node )
                
    return error_list

def dot_case(graph:nx.DiGraph , error_list:list , right_node="" , left_node="" , line= "" , column = "" , last_referent_node=""):
    
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
        
        class aux: # convert parent var <name> into a type <name>
            
            name = ""
            
            def __init__(self,my_name) -> None:
                self.name = my_name
        
        child.parent_name.name = aux(child.parent_name.name)
        child.parent_name.id = child.id
        child.parent_name.__dict__["inheritence"] = True
            
    children = [ item for item in grand_son if item != None and item.id != "var" ]
    
    return children

def def_node_error(graph:nx.DiGraph , ast:pcr.ASTNode , error_list:list , reference_node , last_referent_node):
    
    scope = { "line":ast.line , "column":ast.column }
    
    if ast.__dict__.__contains__("inheritence") : # inheritence checking
        
        inheritence = f"{last_referent_node}_{ast.id}_{ast.name.name}"
            
        if graph.has_node(inheritence):
            
            parent_node = f"{last_referent_node}_{ast.parent.id}_{ast.parent.name.name}"
            graph.add_edge(parent_node , inheritence)
            
            return error_list
        
        else:
            
            error_type , error_description = inheritence_error(ast)
            error_list.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
            
            return error_list
    
    error_type , error_description = selector(ast)(ast)
    
    # ask for an edge existence
    if graph.has_node( f"{reference_node}_{ast.id}_{ast.name.name}"):
        
        error_list.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
        return error_list
    
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
    error_description = f"variable {ast.name.name} has been already defined"
    
    return error_type , error_description

def variable(graph:nx.DiGraph, ast:pcr.variable , error_list:list , reference_node):
    
    if graph.has_node( f"{reference_node}_let_{ast.name}"):
        
        graph.add_edge( f"{reference_node}_let_{ast.name}" , f"{reference_node}_var_{ast.name}" )
        graph.add_edge( f"{reference_node}_var_{ast.name}" , f"{reference_node}_let_{ast.name}" )
        
        return error_list
    
    else:
        error_type = "variable usage"
        error_description = f"variable {ast.name} is used before assigned"    
        scope = { "line":ast.line , "column":ast.column }
        error_list.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
    
        return error_list

def function_call(graph:nx.DiGraph, ast:pcr.function_call , error_list:list , reference_node ):
    
    if graph.has_node( f"{reference_node}_def_function_{ast.name.name}" ):
        
        graph.add_edge( f"{reference_node}_def_function_{ast.name.name}" ,  f"{reference_node}_function_call_{ast.name.name}" )
        graph.add_edge( f"{reference_node}_function_call_{ast.name.name}" , f"{reference_node}_def_function_{ast.name.name}" )
        
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

def print_graph(graph):
    
    nx.draw(graph, with_labels=True, arrows=True)
    plt.show()
    
    pass

def build_graph( graph , parent:pcr.ASTNode , child:pcr.ASTNode , reference_node="type_Object" , last_reference_node="type_Object" , chift=0 ):
    
    if child.__dict__.__contains__("inheritence"):
        return graph
    
    node1_id = ""
    node1 = parent
    node2_id = ""
    node2 = child
    
    if child.def_node:        
        
        if parent.def_node:
        
            node1_id= last_reference_node
            node2_id =reference_node
        
        else:
            
            if chift: # general case            
                
                node1_id=f"{last_reference_node}_{parent.id}"
                node2_id=f"{last_reference_node}_{reference_node}"
                
            else: # let case    
                node1_id=f"{reference_node}_{parent.id}"
                node2_id=f"{reference_node}_{child.id}_{child.name.name}"
                
    elif child.id == "var" and not parent.def_node:
            
        node1_id=f"{reference_node}_{parent.id}"
        node2_id=f"{reference_node}_var_{child.name}"
            
    elif child.id != "var":
        
        if parent.def_node:
            
            node1_id=f"{last_reference_node}_{reference_node}"
            node2_id=f"{reference_node}_{child.id}"
                
        else:
            
            node1_id=f"{reference_node}_{parent.id}"
            node2_id=f"{reference_node}_{child.id}"
    
    if node1_id != "" and node2_id != "":
        graph = add_connection( graph=graph ,node1_id=node1_id ,node1= node1 ,node2= node2 ,node2_id= node2_id )
        
    return graph

def add_connection( graph:nx.DiGraph , node1:pcr.ASTNode , node1_id:str , node2:pcr.ASTNode , node2_id:str ):
    
    '''
    #### Connection from `node1` to `node2`
    
    '''
    graph.add_node( node1_id , ASTNode= node1   )
    graph.add_node( node2_id , ASTNode= node2   )
    graph.add_edge( node1_id , node2_id   )
    
    return graph
