
import HULK_LANGUAGE_DEFINITION as HK

def traslator(token_list:list):
    
    import DerivationTree as DT
    
    parse_list=[("$1",None)]
    parse_list.append(("$2",None))
    
    parse_list.append(("{",None))
    index=0
    
    while index < len(token_list ):
        
        if token_list[index].Text =="'" or token_list[index].Text == "\"" : 
            index+=1
            continue    
                    
        kw = False                    
        for arg in HK.SYMBOLS_and_OPERATORS_parser:            
            
            if token_list[index].Text == arg:
            
                if arg == "in":
                    parse_list.append(("$2",None))
                    
                parse_list.append((token_list[index].Text,None))
                
                if arg == ";" or arg == ")" or arg == "}" or arg == "]" or arg == "," or arg == "=>":
                    
                    parse_list.append(("$2",None))
                
                kw =True
                break
            
        if not kw:
            
            if index + 1 < len(token_list) and token_list[index + 1 ].Text == "(" :
                
                AST_node = DT.builder( "var", [ (token_list[index], None ) ] ).ASTNode
                parse_list.append(("c", AST_node ) )
                
                #parse_list.append(("c", None ) )
            
            else:
                
                AST_node = DT.builder("var" , [ (token_list[index] , None) ] ).ASTNode
                parse_list.append(("T", AST_node) )
                #parse_list.append(("T", None) )
                    
        index += 1
    
    parse_list.append(("$3",None))
    parse_list.insert(-1,("}",None))
        
    return parse_list
