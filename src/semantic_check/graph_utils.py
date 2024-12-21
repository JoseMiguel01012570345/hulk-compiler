import networkx as nx
import matplotlib.pyplot as plt
from ..parser import production_class_representation as pcr
from ..risk import risk
import inspect
log_state_on_error = risk.log_state_on_error

@log_state_on_error
def add_connection( graph:nx.DiGraph , node1:pcr.ASTNode , node1_id:str , node2:pcr.ASTNode , node2_id:str ):
    risk.frame_logger.append( inspect.currentframe() )
    '''
    #### Connection from `node1` to `node2`
    
    '''
    graph.add_node( node1_id , ASTNode= node1   )
    graph.add_node( node2_id , ASTNode= node2   )
    graph.add_edge( node1_id , node2_id   )
    graph.add_edge( node2_id , node1_id   )
    
    return graph

def print_graph(graph):
    nx.draw(graph, with_labels=True, arrows=True)
    plt.show()

@log_state_on_error
def build_graph( graph:nx.DiGraph , def_node_scope:str='' , def_node:pcr.ASTNode=None , ref_node_scope:str='' , ref_node:pcr.ASTNode=None , add_node=True ): 
    # add edge if and only if one node is a definition and the other is a reference    
    risk.frame_logger.append( inspect.currentframe() )
        
    if add_node:
        graph.add_node( def_node_scope , ASTNode=def_node )
        return graph
    
    if graph.has_node(ref_node_scope): # references are already in the graph and are only allowed one edge
        ref_node_neighbor = next(graph.neighbors(ref_node_scope))
        graph.remove_edge(ref_node_scope, ref_node_neighbor)
     
    graph.add_node( ref_node_scope , ASTNode=ref_node )
    graph.add_edge( ref_node_scope , def_node_scope  )
    return graph
    
@log_state_on_error
def build_in(graph:nx.DiGraph ):
    risk.frame_logger.append( inspect.currentframe() )
    
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
    graph.add_node(def_function_sqrt , ASTNode=pcr.sqrt())
    graph.add_node(def_function_sin , ASTNode=pcr.sin())
    graph.add_node(def_function_cos , ASTNode=pcr.cos())
    graph.add_node(def_function_log , ASTNode=pcr.log())
    graph.add_node(def_function_exp , ASTNode=pcr.exp())
    graph.add_node(def_function_rand , ASTNode=pcr.rand())
    graph.add_node(def_function_range , ASTNode=pcr.range())
    graph.add_node(type_String , ASTNode=pcr.String())
    graph.add_node(type_Boolean , ASTNode=pcr.Boolean())
    
    return graph
