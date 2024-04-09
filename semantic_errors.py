class context_errors:
    
    error_list = [ ]
    def __init__(self) -> None:
        
        pass
    
    def add_error(self,error_list):
        
        self.error_list = error_list
        
        pass
    
    def print_(self):
        
        if len(self.error_list) == 1:
            
            print( 
                
                f" \033[1;31m >\033[1;32m There is an issue of the type: \033[1;31m {self.error_list[0]['type']} \033[1;32m which says \033[1;31m {self.error_list[0]['description']} \033[1;32m in \033[1;3m {self.error_list[0]['scope']} \033[0;m")
        
        elif len(self.error_list) > 1 :
            
            print(f" \033[1;31m >\033[1;31m There are several errors in your code \033[0;m")
            
            for item in self.error_list:
                
                type_ = item['type']
                description = item['description']
                
                scope = item['scope']
                
                if len(scope) == 0:
                    print(f" \033[1;31m > \033[1;32m There is an issue of the type: \033[1;31m {type_} \033[1;32m which says \033[1;31m {description} \033[0;m ")
                    scope = ""
                
                else:
                    print(f" \033[1;31m > \033[1;32m There is an issue of the type: \033[1;31m {type_} \033[1;32m which says \033[1;31m {description} \033[1;32m in \033[1;31m {scope} \033[0;m ")
        else:
            
            print(" \033[1;31m >\033[1;32m All in context \033[0m")
        
        pass