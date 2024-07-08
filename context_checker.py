import production_class_representation as pcr
import networkx as nx
import matplotlib.pyplot as plt
from Utils import names

class aux: # convert parent var <name> into a type <name>
            
    name = ""
    
    def __init__(self,my_name) -> None:
        self.name = my_name

def context_checker(ast:pcr.ASTNode=None , error_list=[] , printing=0 ):

    graph = nx.DiGraph()
    
    # graph = build_in(graph)
    
    ast.id += " ROOT"
        
    solve_context( ast=ast , error_list=error_list  , graph=graph )
    
    if printing :
        print_graph(graph=graph)
    
    return graph
    
def solve_context( ast:pcr.ASTNode=None , error_list=[] , graph: nx.DiGraph= None , children=None , all_let = False , stack_referent_node:list=["","type_Object"] ):
    
    if children == None:
        children = ast.visitor_ast()    
    
    for child in children :
    
        if child != None:
            
            if all_let and child.id == "var":
                child.id = "let"
                child.__dict__["name"] = aux(child.name)
            
            # case 1: types , case 2: protocols , case 3: functions , case 4 : let
            if child.id == "type" or child.id == "protocol" or child.id == "def_function" or child.id == "let":
                
                error_list = def_node_error(graph,child,error_list , stack_referent_node[-1] , stack_referent_node[-2] )
                
                def_children = def_node_children(child=child)
                
                if child.id != "let": # let var doesn't open new scope
                    
                    new_referent_node =f"{child.id}_{child.name.name}" # new scope
                    
                    new_stack = [ item for item in stack_referent_node] # add the context to the stack(we are entering in new context)
                    new_stack.append(new_referent_node)
                    
                    graph = build_graph( graph=graph , parent=ast , child=child , reference_node=new_stack[-1] , last_reference_node=new_stack[-2] , chift=1 )
                    
                    error_list = solve_context(child , error_list , graph  , def_children , all_let= all_let , stack_referent_node=new_stack )
                    continue
                
                graph = build_graph( graph=graph , parent=ast , child=child , reference_node=stack_referent_node[-1] , last_reference_node=stack_referent_node[-2] )
                
                error_list = solve_context(child , error_list , graph  , def_children , all_let , stack_referent_node )
                continue
            
            graph = build_graph( graph=graph , parent=ast , child=child , reference_node=stack_referent_node[-1] , last_reference_node=stack_referent_node[-2] )
            
            if child.id == "auto_call":
                
                new_stack = [ item for item in stack_referent_node] # add the context to the stack , we are entering in new context
                new_stack.append("anonymus")    
                
                error_list = solve_context(child , error_list , graph  , None , all_let= all_let ,stack_referent_node=new_stack)
                continue
            
            if child.id == "args" :
                
                error_list = solve_context(child , error_list , graph  , None , all_let=True , stack_referent_node=stack_referent_node )
                continue
                    
            if child.id == "function_call": # check if exits
                
                error_list = function_call(graph,child,error_list , stack_referent_node )
                children_function_call = def_node_children(child=child)
                
                error_list = solve_context( child , error_list , graph , children_function_call , all_let , stack_referent_node )
                continue
            
            # check for existence
            if child.id == "var":
                error_list = variable(graph,child,error_list , stack_referent_node )
            
            if child.id == "instance":

                error_list = instance_case( graph=graph , ast=child , error_list=error_list , stack_referent_node=stack_referent_node )
                
                continue
                
            if child.id == "dot": # check if exits right_node inside left_node
                
                dot_case( graph , error_list , child.right_node ,child.left_node , stack_referent_node[-1])
            
            error_list = solve_context( child , error_list , graph , None , all_let , stack_referent_node )
                
    return error_list

def instance_case(graph:nx.DiGraph , ast:pcr.ASTNode , error_list:list , stack_referent_node:list ): 
    
    i=len(stack_referent_node) - 1
    
    while i >=0:
        
        refence_node = stack_referent_node[i]
        
        type_name = ast.node.name.name
        
        verify_node = f"{refence_node}_type_{type_name}"
        
        if graph.has_node(verify_node):
            
            type_node:pcr.ASTNode = graph.nodes[verify_node]["ASTNode"]
            
            if type_node.__dict__.__contains__("constructor") and \
                len(type_node.constructor.expressions) == len(ast.node.args.expressions):
                    
                    return error_list
            
        i-=1
    
    error_type , error_description = instance_error(ast=ast)
    scope = { "line": ast.line , "column": ast.column }
    
    error_list.append({ "error_type": error_type , "error_description":error_description , "scope":scope })
    
    return error_list

def instance_error(ast:pcr.ASTNode):
    
    error_type="type definition"
    error_description=f"type {ast.node.name.name} is not defined in scope"
    
    return error_type , error_description

def dot_case(graph:nx.DiGraph , error_list:list , right_node:pcr.ASTNode , left_node:pcr.ASTNode , reference_node=""):
    
    # verifiy if in child.left_node type hierarchy exists child.right_node 
    # for that we will check if there exist a path from child.left_node type to
    # "child.right_node.id_child.right_node.name"
    
    left_name = names(left_node)
    right_name =names(right_node)
    
    child_left_node = f"{reference_node}_{left_node.id}_{left_name}"
    child_right_node = f"{left_node.type()}_{right_node.id}_{right_name}"
    
    # line and column most be of the left node
    line = left_node.line
    column =left_node.column
    
    if graph.has_node(child_left_node):
        return error_list
    
    else:
        
        error_type = "object used before declared"
        error_description = f"object {left_name} is not declared in scope"
        scope = { "line":line , "column":column }
        error_list.append({ "error_type": error_type , "error_description":error_description , "scope":scope })
        
    if graph.has_node( child_right_node ):
        return error_list
    
    else:
        error_type = "attr definition"
        error_description = f"object {right_name} is not accesable"
        scope = { "line":line , "column":column }
        error_list.append({ "error_type": error_type , "error_description":error_description , "scope":scope })
    
    return error_list

def def_node_children(child:pcr.ASTNode):
    
    grand_son = child.visitor_ast()
    
    children = []
    
    if child.__dict__.__contains__("parent_name"):
        
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
        
        node_ast = graph.nodes[f"{reference_node}_{ast.id}_{ast.name.name}"]["ASTNode"]
        
        args = args_checking( ast , node_ast )
        
        if args:
            error_list.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
        
        return error_list
    
    return error_list

def args_checking( node_ast:pcr.ASTNode , ast:pcr.ASTNode ):
    '''
    returns True if amount of arguments is the same
    '''
    if ast.id == "def_function":
        
        if len(node_ast.args.expressions) != len(ast.args.expressions):
            return False
        
    if ast.id == "type":
        
        if ast.__dict__.__contains__("constructor") and node_ast.__dict__.__contains__("constructor"):
            
            if len(ast.constructor.expressions) != len(node_ast.constructor.expressions):
                return False
        else:
            return False
        
        if ast.__dict__.__contains__("base") and node_ast.__dict__.__contains__("base"):
            
            if len(ast.base.expressions) != len(node_ast.base.expressions):
                return False
        elif ast.__dict__.__contains__("base") or node_ast.__dict__.__contains__("base") :
            return False
        
    return True

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

def variable(graph:nx.DiGraph, ast:pcr.variable , error_list:list , stack_referent_node):
    
    for reference_node in stack_referent_node:
    
        if graph.has_node( f"{reference_node}_let_{ast.name}"): # check if variable is accesable from outter context from its position
            
            graph.add_edge( f"{reference_node}_let_{ast.name}" , f"{reference_node}_var_{ast.name}" )
            graph.add_edge( f"{reference_node}_var_{ast.name}" , f"{reference_node}_let_{ast.name}" )
            
            return error_list
    
    error_type = "variable usage"
    error_description = f"variable {ast.name} is used before assigned"    
    scope = { "line":ast.line , "column":ast.column }
    error_list.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )

    return error_list

def function_call(graph:nx.DiGraph, ast:pcr.function_call , error_list:list , stack_referent_node ):
    
    i = len(stack_referent_node) - 1
    while i >=0:
        
        reference_node = stack_referent_node[i]
        
        if graph.has_node( f"{reference_node}_def_function_{ast.name.name}" ) : # check if call is accesable from outter context from its position
            
            reference_of_the_referent_node = f"{stack_referent_node[i-1]}_{reference_node}"
            
            node_ast = graph.nodes[ f"{reference_node}_def_function_{ast.name.name}" ]["ASTNode"]
            referent_node_ast = graph.nodes[ reference_of_the_referent_node ]["ASTNode"]
            
            if node_ast.args != None and  referent_node_ast.args != None and len(node_ast.args.expressions) == len( referent_node_ast.args.expressions ):   
                
                graph.add_edge( f"{reference_node}_def_function_{ast.name.name}" ,  f"{reference_node}_function_call_{ast.name.name}" )
                graph.add_edge( f"{reference_node}_function_call_{ast.name.name}" , f"{reference_node}_def_function_{ast.name.name}" )
            
                return error_list
        i -= 1
    
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
