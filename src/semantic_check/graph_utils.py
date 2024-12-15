import networkx as nx
import matplotlib.pyplot as plt
from ..parser import production_class_representation as pcr

def add_connection( graph:nx.DiGraph , node1:pcr.ASTNode , node1_id:str , node2:pcr.ASTNode , node2_id:str ):
    
    '''
    #### Connection from `node1` to `node2`
    
    '''
    graph.add_node( node1_id , ASTNode= node1   )
    graph.add_node( node2_id , ASTNode= node2   )
    graph.add_edge( node1_id , node2_id   )
    
    return graph

def print_graph(graph):
    nx.draw(graph, with_labels=True, arrows=True)
    plt.show()
    
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
                
                node1_id=f"{last_reference_node}"
                node2_id=f"{reference_node}"
                
            else: # let case    
                node1_id=f"{reference_node}_{parent.id}"
                node2_id=f"{reference_node}_{child.id}_{child.name.name}"
                
    elif child.id != "var":
        
        if parent.def_node:
            
            node1_id=f"{reference_node}"
            node2_id=f"{reference_node}_{child.id}"
                
        else:
            
            node1_id=f"{reference_node}_{parent.id}"
            node2_id=f"{reference_node}_{child.id}"
    
    if node1_id != "" and node2_id != "":
        graph = add_connection( graph=graph ,node1_id=node1_id ,node1= node1 ,node2= node2 ,node2_id= node2_id )
        
    return graph


def build_in(graph:nx.DiGraph , stack_referent_node:list ):
    
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
    
    graph.add_node(type_object , ASTNode=pcr.Object())
    graph.add_node(def_function_print , ASTNode=pcr.print())
    graph.add_node(type_Number , ASTNode=pcr.Number())
    graph.add_node(let_e , ASTNode=pcr.e)
    graph.add_node(let_PI , ASTNode=pcr.PI)
    graph.add_node(def_function_tan , ASTNode=pcr.tan())
    graph.add_node(def_function_cot , ASTNode=pcr.cot())
    graph.add_node(def_function_sqrt , ASTNode=pcr.sin())
    graph.add_node(def_function_sin , ASTNode=pcr.sin())
    graph.add_node(def_function_cos , ASTNode=pcr.cos())
    graph.add_node(def_function_log , ASTNode=pcr.log())
    graph.add_node(def_function_exp , ASTNode=pcr.exp())
    graph.add_node(def_function_rand , ASTNode=pcr.rand())
    graph.add_node(def_function_range , ASTNode=pcr.range())
    graph.add_node(type_String , ASTNode=pcr.String())
    graph.add_node(type_Boolean , ASTNode=pcr.Boolean())

    graph.add_edge( f"{stack_referent_node[-1]}" , type_object )
    graph.add_edge( f"{stack_referent_node[-1]}" , type_Number )
    graph.add_edge( f"{stack_referent_node[-1]}" , type_Boolean )
    graph.add_edge( f"{stack_referent_node[-1]}" , type_String )
    graph.add_edge( f"{stack_referent_node[-1]}" , def_function_cos )
    graph.add_edge( f"{stack_referent_node[-1]}" , def_function_cot )
    graph.add_edge( f"{stack_referent_node[-1]}" , def_function_exp )
    graph.add_edge( f"{stack_referent_node[-1]}" , def_function_log )
    graph.add_edge( f"{stack_referent_node[-1]}" , def_function_rand )
    graph.add_edge( f"{stack_referent_node[-1]}" , def_function_sqrt )
    graph.add_edge( f"{stack_referent_node[-1]}" , def_function_range )
    graph.add_edge( f"{stack_referent_node[-1]}" , def_function_tan )
    graph.add_edge( f"{stack_referent_node[-1]}" , def_function_sin )
    graph.add_edge( f"{stack_referent_node[-1]}" , let_e )
    graph.add_edge( f"{stack_referent_node[-1]}" , let_PI )
    graph.add_edge( f"{stack_referent_node[-1]}" , def_function_print )
    
    return graph
