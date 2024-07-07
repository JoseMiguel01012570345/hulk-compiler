import networkx as nx
import production_class_representation as pcr
import matplotlib.pyplot as plt
import copy

def create_graph_and_print(ast:pcr.ASTNode , printig):

    dg = nx.DiGraph()
    
    ast_copy = copy.deepcopy(ast)
    ast_copy.id += " ROOT"
    
    graph =  build_graph(dg , ast=ast_copy)    
    
    if printig: 
      
        nx.draw(graph, with_labels=True, arrows=True)
        plt.show()
      
    return graph

def build_graph( graph , ast ):

    children = ast.visitor_ast()
    
    for child in children:
        
        if child == None: continue
            
        if child.def_node:        
            
            if ast.def_node:
            
                graph.add_edge( f"{ast.id}_{ast.name.name}" , f"{child.id}_{child.name.name}" )
                continue
            
            graph.add_edge( f"{ast.id}_{ast.hash_}" , f"{child.id}_{child.name.name}" )
        
        elif child.id == "var":
            
            if ast.def_node:
                graph.add_edge( f"{ast.id}_{ast.name.name}", f"{child.id}_{child.name}" )
                
            else:
                graph.add_edge( ast.id + str(ast.hash_), f"{child.id}_{child.name}" )
        
        else:
            
            if ast.def_node:
                
                graph.add_edge( f"{ast.id}_{ast.name.name}" , child.id + "_" + str(child.hash_) )
                
            else:
                graph.add_edge( ast.id + "_" + str(ast.hash_), child.id + "_" + str(child.hash_) )
        
        graph = build_graph( graph=graph , ast=child )
        
    return graph