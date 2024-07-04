import networkx as nx
import production_class_representation as pcr
import matplotlib.pyplot as plt
import copy

def create_graph_and_print(ast:pcr.ASTNode , printig):

    if not printig: 
        return
    
    dg = nx.DiGraph()
    
    ast_copy = copy.deepcopy(ast)
    ast_copy.id += " ROOT"
    
    graph =  build_graph(dg , ast=ast_copy)    
    
    nx.draw(graph, with_labels=True, arrows=True)
    plt.show()
    
    pass

def build_graph( graph , ast , h=0 ):

    if type(ast) == "list":
    
        for element in child:
            
            if element == None : continue
            
            graph = build_graph( graph=graph , ast=element )
            
            graph.add_edge( ast.id + str(ast.hash_), element.id + str(element.hash_) )
        
    else:
        
        children = ast.visitor_ast()
        
        for child in children:
            
            if child == None: continue
            
            if isinstance(child , list):
                
                for element in child:
                    
                    if element == None:continue
                    
                    graph.add_edge( ast.id + str(ast.hash_) , element.id + str(element.hash_) )
                    graph = build_graph( graph=graph , ast=element )
                
                continue
                
            if hasattr(child,"id"):
                
                graph.add_node( child.id + str(child.hash_) , obj=child )
                graph.add_edge( ast.id + str(ast.hash_), child.id + str(child.hash_) )
                graph = build_graph( graph=graph , ast=child )
                
                continue

            graph.add_node(child ,obj=child )
            graph.add_edge(ast.id +str(ast.hash_) , child)
        
    return graph
