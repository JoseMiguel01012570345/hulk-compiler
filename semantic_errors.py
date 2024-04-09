class context_errors:
    
    error_list = [ ]
    def __init__(self) -> None:
        
        pass
    
    def add_error(self,error_list):
        
        self.error_list = error_list
        
        pass
    
    def print_(self):
        
        if len(self.error_list) == 1:
            print(f"\033[1;32m There is an issue of the type: \033[1;31m {self.error_list[0][0]} \033[1;32m which says \033[1;31m {self.error_list[0][1]} \033[0;m")
        
        elif len(self.error_list) > 1 :
            
            print(f"\033[1;31m There are several errors in your code \033[0;m")
            
            for item in self.error_list:
                
                print(f"\033[1;32m There is an issue of the type: \033[1;31m {item[0]} \033[1;32m which says \033[1;31m {item[1]} \033[0;m")
        else:
            
            print("\033[1,32m All in context \033[0m")
        
        pass