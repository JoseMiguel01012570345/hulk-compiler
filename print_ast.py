import networkx as nx
import production_class_representation as pcr
import matplotlib.pyplot as plt

def create_graph_and_print(ast:pcr.ASTNode):

    dg = nx.DiGraph()
    graph =  build_graph(dg , ast=ast)    
    
    nx.draw(graph, with_labels=True, arrows=True)
    plt.show()
    
    pass

def build_graph( graph , ast:pcr.ASTNode ):

    children = ast.visitor_ast()
    
    for child in children:
        
        if child != None:
            
            if hasattr(child,"id"):
                graph.add_node( child.id , obj=child )
                graph.add_edge( ast.id, child.id )
                graph = build_graph( graph=graph , ast=child )
            
            else:
                graph.add_node(child ,obj=child )
                graph.add_edge(ast.id, child)
    
    return graph
