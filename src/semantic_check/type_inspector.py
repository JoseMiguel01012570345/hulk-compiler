from ..parser import production_class_representation as pcr
import inspect
from src.risk import risk

@risk.log_state_on_error
def type_inpector( ast:pcr.ASTNode ):
    risk.frame_logger.append( inspect.currentframe())
    
    children = ast.visitor_ast()
    for child in children:
        child_signature = ''
        if child.def_node:
            child_signature = f'{child.id}_{child.name}'
        else:
            child_signature = f'{child.id}'
            
        print( child_signature , '___typing:' , child.node_type )
    
    for child in children:
        type_inpector( child )