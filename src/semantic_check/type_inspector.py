from ..parser import production_class_representation as pcr
import inspect
from src.risk import risk
import networkx as nx

@risk.log_state_on_error
def type_inpector( ast:pcr.ASTNode , graph:nx.DiGraph  ):
    risk.frame_logger.append( inspect.currentframe())
    
    children = ast.visitor_ast()
    for child in children:
        child_signature = ''
        if child.def_node:
            if child.id == 'let':
                child_signature = f'{child.referent_node}_{child.id}_{child.name}'
            else:
                child_signature = f'{child.referent_node}'
        else:
            if child.__dict__.__contains__('name'):
                child_signature = f'{child.referent_node}_{child.id}_{child.name}'
            else:
                child_signature = f'{child.referent_node}_{child.id}'
        
        print( child_signature , '___typing:' , child.type( graph=graph ) )
    
    for child in children:
        type_inpector( child , graph=graph )