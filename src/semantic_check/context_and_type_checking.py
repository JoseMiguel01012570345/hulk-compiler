from ..parser import production_class_representation as pcr
from . import errors
import networkx as nx
from . import graph_utils
print_graph , build_graph , build_in = graph_utils.print_graph , graph_utils.build_graph , graph_utils.build_in
from ..risk import risk
log_state_on_error = risk.log_state_on_error
import inspect
# from src import Utils
# from Utils import names

class aux: # convert parent var <name> into a type <name>
            
    name = ""
    
    def __init__(self,my_name) -> None:
        self.name = my_name

@log_state_on_error
def context_checker( printing=0 ):
    risk.frame_logger.append( inspect.currentframe() )
    
    graph = nx.DiGraph()
    
    # import build-ins
    graph = build_in(graph=graph )
    
    if printing :
        print_graph(graph=graph)
    
    return graph

@log_state_on_error
def solve_context_and_type( ast:pcr.ASTNode=None , error_log=[] , graph: nx.DiGraph= None , children=None , all_let = False , stack_referent_node:list=[""] ):
    risk.frame_logger.append( inspect.currentframe() )
    
    if  children is None:
        children = ast.visitor_ast()
    
    for child in children:
    
        if child is not None:
                        
            if all_let and child.id == "var":
                child.def_node = True
                child.id = "let"
                child.__dict__["name"] = aux(child.name)
            
            # case 1: types , case 2: protocols , case 3: functions , case 4 : let
            if child.id == "type" or child.id == "protocol" or child.id == "def_function" or child.id == "let":
                
                error_log = def_node_error(graph,child,error_log , stack_referent_node )
                
                def_children = def_node_children(child=child)
                
                if child.id != "let": # let var doesn't open new scope
                    
                    new_referent_node =f"{stack_referent_node[-1]}_{child.id}_{child.name.name}" # new scope
                    
                    new_stack = [ item for item in stack_referent_node] # add the context to the stack(we are entering into new context)
                    new_stack.append(new_referent_node)
                    
                    # build graph adding new context
                    graph = build_graph( graph=graph , def_node_scope=new_stack[-1] , def_node=child )
                    
                    if child.id == 'type' or child.id == 'protocol': # all type attr or protocol attr are let
                        error_log = solve_context_and_type(child , error_log , graph  , def_children , all_let= True , stack_referent_node=new_stack )
                        continue
                    
                    error_log = solve_context_and_type(child , error_log , graph  , def_children , all_let= all_let , stack_referent_node=new_stack )
                    continue
                
                let_scope = f'{stack_referent_node[-1]}_let_{child.name.name}'
                graph = build_graph( graph=graph , def_node_scope=let_scope , def_node=child )
                
                error_log = solve_context_and_type(child , error_log , graph  , def_children , all_let , stack_referent_node )
                continue
            
            if child.id == "auto_call": # IN case
                
                new_stack = [ item for item in stack_referent_node] # add the context to the stack , we are entering in new context
                new_stack.append("anonymus")    
                
                error_log = solve_context_and_type(child , error_log , graph  , None , all_let= all_let ,stack_referent_node=new_stack)
                continue
            
            if child.id == "args" and ast.def_node : # set all args var to let var
                
                error_log = solve_context_and_type(child , error_log , graph  , None , all_let=True , stack_referent_node=stack_referent_node )
                continue
            
            if child.id == "function_call": # check if exits
                
                error_log = function_call(graph,child,error_log , stack_referent_node )
                children_function_call = def_node_children(child=child)
                
                error_log = solve_context_and_type( child , error_log , graph , children_function_call , all_let , stack_referent_node )
                continue
            
            if child.id == "var": # check for existence
                error_log = variable(graph,child,error_log , stack_referent_node )
                
            if child.id == "instance": # instance case

                error_log = instance_case( graph=graph , ast=child , error_log=error_log , stack_referent_node=stack_referent_node )
                
                verify_instance_args = child.node.args.expressions
                
                error_log = solve_context_and_type( child , error_log , graph , verify_instance_args , all_let , stack_referent_node )
                
                continue
                
            if child.id == "dot": # check if exits right_node inside left_node
                dot_case( graph , error_log , child.right_node ,child.left_node , stack_referent_node)
                    
            error_log = solve_context_and_type( child , error_log , graph , None , all_let , stack_referent_node )
                
    error_log = type_checking_creteria( graph , ast_node=ast , stack_referent_node=stack_referent_node , error_log=error_log )
    
    return error_log
@log_state_on_error
def instance_case(graph:nx.DiGraph , ast:pcr.ASTNode , error_log:list , stack_referent_node:list ): 
    risk.frame_logger.append( inspect.currentframe() )
    
    i=len(stack_referent_node) - 1
    
    while i >=0:
        
        refence_node = stack_referent_node[i]
        
        type_name = ast.node.name.name
        
        verify_node = f"{refence_node}_type_{type_name}"
        
        if graph.has_node(verify_node):
            
            type_node:pcr.ASTNode = graph.nodes[verify_node]["ASTNode"]
            
            if type_node.__dict__.__contains__("constructor") and \
                len(type_node.constructor.expressions) == len(ast.node.args.expressions):
                    ast.expected_type = type_name
                    return error_log
            
        i-=1
    
    error_type , error_description = errors.instance_error(ast=ast)
    scope = { "line": ast.line , "column": ast.column }
    
    error_log.append({ "error_type": error_type , "error_description":error_description , "scope":scope })
    
    return error_log

@log_state_on_error
def dot_case(graph:nx.DiGraph , error_log:list , right_node:pcr.ASTNode , left_node:pcr.ASTNode , stack_referent_node=""):
    risk.frame_logger.append( inspect.currentframe() )
    
    # verifiy if in child.left_node type hierarchy exists child.right_node 
    # for that we will check if there exist a path from child.left_node type to
    # "child.right_node.id_child.right_node.name"
    
    left_name = names(left_node)
    right_name =names(right_node)
    
    target_type = left_node.type()
    attr = f"{right_node.id}_{right_name}"
    
    child_left_node = f"{stack_referent_node[-1]}_{left_node.id}_{left_name}"
    
    # line and column most be of the left node
    line = left_node.line
    column =left_node.column
    
    if not graph.has_node(child_left_node): # left node most exist
        
        error_type = "object used before declared"
        error_description = f"object {left_name} is not declared in scope"
        scope = { "line":line , "column":column }
        error_log.append({ "error_type": error_type , "error_description":error_description , "scope":scope })
        
    result = inheritence_walker( graph=graph , target_type=target_type , attr=attr , stack_referent_node=stack_referent_node , state= len(stack_referent_node) - 1 )
    
    if not result:
        
        error_type = "attr definition"
        error_description = f"object {right_name} is not accesable"
        scope = { "line":line , "column":column }
        error_log.append({ "error_type": error_type , "error_description":error_description , "scope":scope })
    
    return error_log

@log_state_on_error
def inheritence_walker( graph:nx.DiGraph , target_type:str , attr:str , stack_referent_node:list , state= 0 ) -> bool:
    risk.frame_logger.append( inspect.currentframe() )
    
    i = state
    
    # walk through all visible types that match with target_type and in adition , consider its inheritence
    
    while i>=0:
        
        referent_node = stack_referent_node[i]
        
        if graph.has_node(f"{referent_node}_{target_type}"):
        
            if graph.has_node(f"{referent_node}_{target_type}_{attr}"):
                return True
            
            target_type_ast = graph.nodes[f"{referent_node}_{target_type}"]["ASTNode"]
            
            if target_type_ast.parent_name != None:
                
                parent_type = target_type_ast.parent_name.name.name
                
                result = inheritence_walker( graph= graph , target_type= parent_type , state= i - 1 )
                
                if result:
                    return True
            
            pass
        
        i-=1
        
    return False

@log_state_on_error
def def_node_children(child:pcr.ASTNode):
    risk.frame_logger.append( inspect.currentframe() )
    
    grand_son = child.visitor_ast()
    
    children = []
    
    if child.__dict__.__contains__("parent_name"):
        
        child.parent_name.name = aux(child.parent_name.name)
        child.parent_name.id = child.id
        child.parent_name.__dict__["inheritence"] = True
            
    children = [ item for item in grand_son if item != None and item.id != "var" ]
    
    return children

@log_state_on_error
def def_node_error(graph:nx.DiGraph , ast:pcr.ASTNode , error_log:list , stack_referent_node:list):
    risk.frame_logger.append( inspect.currentframe() )
    
    scope = { "line":ast.line , "column":ast.column }
    
    if ast.__dict__.__contains__("inheritence") : # inheritence checking
        
        inheritence = f"{stack_referent_node[-1]}_{ast.id}_{ast.name.name}"
            
        if graph.has_node(inheritence):
            
            parent_node = f"{stack_referent_node[-1]}_{ast.parent.id}_{ast.parent.name.name}"
            graph.add_edge(parent_node , inheritence)
            
            return error_log
        
        else:
            
            error_type , error_description = errors.inheritence_error(ast)
            error_log.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
            
            return error_log
    
    error_type , error_description = errors.selector(ast)(ast)
    
    # ask for an edge existence
    reference_node = f"{stack_referent_node[-1]}_{ast.id}_{ast.name.name}"
    if graph.has_node( reference_node ):
        
        node_ast = graph.nodes[ reference_node ]["ASTNode"]
        
        args = args_checking( ast , node_ast )
        
        if args:
            error_log.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )
        
        return error_log
    
    return error_log

@log_state_on_error
def args_checking( referent_node:pcr.ASTNode , ast:pcr.ASTNode ):
    risk.frame_logger.append( inspect.currentframe() )
    
    '''
    returns True if amount of arguments is the same
    
    ast: is the node to be checked
    
    '''
    
    if ast.id == "def_function":
        
        if len(referent_node.args.expressions) != len(ast.args.expressions):
            return False
        
    if ast.id == "type":
        
        if ast.__dict__.__contains__("constructor") and referent_node.__dict__.__contains__("constructor"):
            
            if len(ast.constructor.expressions) != len(referent_node.constructor.expressions):
                return False # they are not the same type because of different number of arguments
        else:
            return False # ast is a static class and referent node is a class with constructor
        
        if ast.__dict__.__contains__("base") and referent_node.__dict__.__contains__("base"):
            
            if len(ast.base.expressions) != len(referent_node.base.expressions):
                return False #  they are not the same type because of different number of arguments in base constructor
        elif ast.__dict__.__contains__("base") or referent_node.__dict__.__contains__("base") :
            return False # they are different because one of them has a base constructor
        
    return True

@log_state_on_error
def function_call(graph:nx.DiGraph, ast:pcr.function_call , error_log:list , stack_referent_node ):
    risk.frame_logger.append( inspect.currentframe() )
    
    i = len(stack_referent_node) - 1    
    my_node = None # ast node
    my_node_signature = '' # graph representation name of my_node
    
    while i >= 0:
        
        node = stack_referent_node[i] # recursive case
        
        if f"def_function_{ast.name.name}" in node:
            
            my_node = graph.nodes[node]["ASTNode"]
            my_node_signature = node 
            ast.node_type =  my_node.pointer_to_node_type # use pointer_to_node_type function to point to the current type
            
            break
        i-=1
        
    if my_node == None: # outter scope ( non-recursive )
        
        i = len(stack_referent_node) - 1
        while i>=0:
            
            if stack_referent_node[i] == '':
                node = f"def_function_{ast.name.name}"
            else:
                node = f"{stack_referent_node[i]}_def_function_{ast.name.name}"
                
            if graph.has_node(node):
                
                my_node = graph.nodes[node]["ASTNode"]
                my_node_signature = node
                ast.node_type = my_node.pointer_to_node_type # use pointer_to_node_type function to point to the current type
                
                break        
            i-=1
    
    if my_node is not None and my_node.args is not None and len(ast.args.expressions) == len( my_node.args.expressions ):
        
        ref_node_scope = f"{stack_referent_node[-1]}_{ast.id}_{ast.name.name}"
        build_graph( graph=graph, def_node_scope=my_node_signature , ref_node_scope=ref_node_scope , ref_node=ast , add_node=False )
        
        return error_log
    
    scope = { "line":ast.line , "column":ast.column }
    error_type = "function usage"
    error_description = f"function {ast.name.name} is used before declared"    
    error_log.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )

    return error_log

@log_state_on_error
def variable(graph:nx.DiGraph, ast:pcr.variable , error_log:list , stack_referent_node):
    risk.frame_logger.append( inspect.currentframe() )
    
    if ast.name == "self": # self case
            
        referent_node = stack_referent_node[-1]
        referent_node_ast: pcr.ASTNode = graph.nodes[stack_referent_node[-1]]["ASTNode"]    
        
        if "type" in referent_node and referent_node_ast.constructor != None : # if there is a referent type node with a constructor , we add var self to graph
            return error_log
        
    for reference_node in stack_referent_node:
    
        if graph.has_node( f"{reference_node}_let_{ast.name}"): # check if variable is accesable from outter context from its position
            
            ref_node_scope = f'{stack_referent_node[-1]}_var_{ast.name}'
            build_graph( graph=graph , def_node_scope=f"{reference_node}_let_{ast.name}" , ref_node_scope=ref_node_scope , ref_node=ast , add_node=False )
            return error_log
    
    error_type = "variable usage"
    error_description = f"variable {ast.name} is used before assigned"    
    scope = { "line":ast.line , "column":ast.column }
    error_log.append( { "error_type": error_type , "error_description":error_description , "scope":scope } )

    return error_log

@log_state_on_error
def typing_error( ast_node:pcr.ASTNode ):
    risk.frame_logger.append( inspect.currentframe() )
    
    error_type=""
    error_description=""
    
    if type(ast_node) == pcr.binary_opt:
        error_type="type error"
        error_description = "operation can not be peformed between different types"
    else:
        error_type="type error"
        error_description = f"operation can not be peformed , expected type { ast_node.expected_type } , dismatchs"
    
    return error_type , error_description

@log_state_on_error
def type_checking_creteria( graph:nx.DiGraph , ast_node:pcr.ASTNode , stack_referent_node:list , error_log:list ):
    risk.frame_logger.append( inspect.currentframe() )
    
    if ast_node.type_checker:
        
        ast_type = ast_node.type(graph=graph , referent_node=stack_referent_node[-1] )
        expected_type = ast_node.expected_type
        
        if expected_type != "Object" and ast_type != expected_type :
            
            error_type , error_description = typing_error( ast_node=ast_node )
            
            scope= { "line": ast_node.line , "column": ast_node.column }
            
            error_log.append( { "error_type": error_type , "error_description": error_description , "scope":scope } )
            
            return error_log
                
    return error_log

@log_state_on_error
def names(node):
    risk.frame_logger.append( inspect.currentframe() )
    
    if node.id == "var":
        return node.name
    else:
        return node.name.name
    