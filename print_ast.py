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

def build_graph( graph , ast , reference_node="type_Object", last_reference_node="type_Object" , chift=0 ):

    children = ast.visitor_ast()
    
    for child in children:
        
        if child == None: continue
            
        if child.def_node:        
            
            if ast.def_node:
                
                if chift:
                    graph.add_edge( f"{last_reference_node}_{ast.id}_{ast.name.name}_{ast.line}_{ast.column}" , f"{reference_node}_{child.id}_{child.name.name}_{child.line}_{child.column}" )

                else:
                    graph.add_edge( f"{reference_node}_{ast.id}_{ast.name.name}_{ast.line}_{ast.column}" , f"{reference_node}_{child.id}_{child.name.name}_{child.line}_{child.column}" )
            
            else:
            
                if chift:
                    graph.add_edge( f"{last_reference_node}_{ast.id}_{ast.line}_{ast.column}" , f"{reference_node}_{child.id}_{child.name.name}_{child.line}_{child.column}" )
                
                else:
                    graph.add_edge( f"{reference_node}_{ast.id}_{ast.line}_{ast.column}" , f"{reference_node}_{child.id}_{child.name.name}_{child.line}_{child.column}" )
        
        elif child.id == "var" and not ast.def_node:
            
            if chift:
                graph.add_edge( f"{last_reference_node}_{ast.id}_{ast.line}_{ast.column}", f"{reference_node}_{child.id}_{child.name}_{child.line}_{child.column}" )
            
            else:
                graph.add_edge( f"{reference_node}_{ast.id}_{ast.line}_{ast.column}", f"{reference_node}_{child.id}_{child.name}_{child.line}_{child.column}" )
        
        elif child.id != "var":
            
            if ast.def_node:
                
                if chift:
                    graph.add_edge( f"{last_reference_node}_{ast.id}_{ast.name.name}_{ast.line}_{ast.column}" , f"{reference_node}_{child.id}_{child.line}_{child.column}" )
                else:
                    graph.add_edge( f"{reference_node}_{ast.id}_{ast.line}_{ast.column}" , f"{reference_node}_{child.id}_{child.line}_{child.column}" )
            
            else:
                if chift:
                    graph.add_edge( f"{last_reference_node}_{ast.id}_{ast.line}_{ast.column}" , f"{reference_node}_{child.id}_{child.line}_{child.column}" )
                else:
                    graph.add_edge( f"{reference_node}_{ast.id}_{ast.line}_{ast.column}" , f"{reference_node}_{child.id}_{child.line}_{child.column}" )
        
        if child.def_node:
            graph = build_graph( graph=graph , ast=child , reference_node=f"{child.id}_{child.name.name}", last_reference_node=reference_node , chift=1 )
        else:
            graph = build_graph( graph=graph , ast=child , reference_node=reference_node , last_reference_node=reference_node , chift=0 )
        
    return graph