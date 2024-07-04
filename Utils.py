import production_class_representation as pcr

def isNumeric(text):
    
    if text.isnumeric():
        return True
    
    if not text.startswith('e') and text.count('e+') == 1 and text.count('+') == 1 and text.count('e') == 1 and not text.endswith('+'):
        parts = text.split('e+')
        if parts[0].isnumeric() and parts[1].isnumeric():
            return True
        return False
    
    if not text.startswith('e') and text.count('e-') == 1 and text.count('-') == 1 and text.count('e') == 1 and not text.endswith('-'):
        parts = text.split('e-')
        if parts[0].isnumeric() and parts[1].isnumeric():
            return True
        return False
    
    return False

def final_reduction( ast:pcr.ASTNode , node=None ):
    
    children = ast.visitor_ast()
    
    count = 0
    
    for child in children:
        if child == None:
            count += 1
    
    if count == len(children): 
        return True
    
    for child in children:
        
        if hasattr(child,"id"):
            
            reduce = final_reduction(child)
            
            if reduce:
                child = None
            
    return False