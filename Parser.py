from RegExDefinitions import TokenFinitRegEx
from RegExInterface import State,IRegEx
import GRAMMAR_PRODUCTIONS as GD
import DerivationTree as dt

class Parser():
    
    """
    GRAMMATIC PARSING

    """
    operator_procedence =[
        
        ['[','(','{'],
        [']',')'],
        ["c"],
        ['}'],
        ['as'],
        ['^','%','**'],
        ['*','/'],
        ['+','-'],
        ['>','<','>=','<=','==', '!' ,'is'],
        ['&','|','!'],
        ['.'],
        ['=','+=','-=','/=','*=','--',':=','++','--'],
        ["let"],
        ['if'],
        ['elif'],
        ['else'],
        ['@','@@'],
        [','],
        ['in' ],
        ['||'],
        [";"],
        ["$2"],
        ["$1","$3"],
    ]
    
    def __init__(self,grammar,code ):

        self._grammar = grammar
        self._error = None
        self._match = False
        self._stack = []
        self.derivation_Tree = None
        
        parsed_code = self.gradient_parser(grammar,self._stack,code)
        
        print(parsed_code)
        if not parsed_code:
            self._error = True
        
        pass
    
    @property
    def Error(self):
        return self._error
    
    @property
    def Match(self):
        return self._match
    
    @property
    def Expression(self):
        return self._expression
    
    @property
    def State(self):
        return self._state
    
    @property
    def LastState(self):
        return self._laststate
    
    def Restart(self):        
        pass
    
    @property
    def check_point(self,last_reduction):
        self.last_reduction = last_reduction
        
        return self.last_reduction
    
    def compare_procedence(self , pivote , pointer):
        
        '''
        compare precedence between operator1 and operator2:
        ->  0: equal procedence
        ->  1: grater procedence
        -> -1: lower procedence        
        '''
        
        if pivote == "(" : return 0
        if pivote == "{" : return 0
        if pivote == "[" : return 0
        
        if pointer == "(" and ( pivote == ")" ) : return -1
        
        if pointer == "{" and ( pivote == "}" ): return -1
        
        if pointer == "[" and ( pivote == "]"): return -1
        
        if pointer == "$1": return 0 
        if pointer == "$2" or pivote == "$2" : return -1 
        
        if any( pointer == item for item in [']',')','}'] ) or any( pivote == item for item in [']',')','}'] ) :
            return -1
        
        if any( pointer == item for item in ['[','(','{'] ) or any( pivote == item for item in ['[','(','{'] ) :
            return -1
        
        for operators in self.operator_procedence:
            
            if list(operators).__contains__(pivote) and list(operators).__contains__(pointer):
                return 0
            
            if list(operators).__contains__(pivote) and not list(operators).__contains__(pointer):
                return 1
            
            if not list(operators).__contains__(pivote) and list(operators).__contains__(pointer):
                return -1
            
    def is_operator(self,item):
        
        for operators in self.operator_procedence:
            
            if list(operators).__contains__(item): return True
        
        return False
    
    # the stack_pointer has the structure ( "index" in "code" , "operator item" )
    stack_pointer=[( 0 ,"$1")]
    best_match = 0
    
    def match(self , target:list , derivation:list ):
        
        if len(target) != len(derivation):
            return False
        
        index = 0

        while index < len(derivation) :
            
            if target[index][0] != derivation[index]: return False
            
            index += 1
        
        if len(derivation) > self.best_match:
            
            self.best_match = len(derivation)      
            
            return  True
    
        else: return  False
        
    def _shift_reduce(self , pivot , index_pointer ,next_point ):
    
        '''
        return True if shift
        return False if reduce
        return shift if not an operator (True)
        
        '''    
        if len(self.stack_pointer) == 0:
            return True
        
        if self.is_operator(pivot):
            
            result = self.compare_procedence( pivot , self.stack_pointer[next_point][1] )

            if result == 0 or result == 1 :

                self.stack_pointer.append((index_pointer,pivot))

                return True
            
            else:
                return False
        
        return True
    
    def remove_item_stack(self , stack:list ,pop_number):
        
        i=0
        while i < pop_number:
            
            stack.pop()
            
            i +=1
        
        return stack

    def reduce_stack(self , stack:list , grammar , next_point ):
            
        self.best_match =0
        
        sub_stack = stack[ self.stack_pointer[next_point][0] : ]
        
        best_match=[]
        
        index = 0
        
        pop_number = 0
        while index < len(sub_stack):
        
            target = sub_stack[ index: ]
            
            for features in grammar:
                
                for productions in features:
                        
                    for prefix in productions[1]:
                    
                        new_best_match = self.match(target,prefix)
                        
                        if new_best_match :
                            
                            best_match = productions[0]
                            
                            pop_number = len(prefix)
            
            index += 1
            
        if len(best_match) > 0:

            token_list = self.match_derivation_token( stack[ len(stack)- pop_number :] )

            new_derivation_tree = self.derivation_tree( best_match , token_list )
            
            new_stack = self.remove_item_stack(stack=stack , pop_number= pop_number )
            
            # -------------------------------------------------
            
            printing_stack = []
            for item in new_stack:
                printing_stack.append(item[0])
            
            printing_stack.append(best_match)
            print(printing_stack)
            
            # -------------------------------------------------
            new_stack.append(( best_match , new_derivation_tree ))
            
            return new_stack , True
        
        return stack , False
    
    def match_derivation_token(self ,reduced_token):
        
        token_list = []
        
        for item in reduced_token:
            
            
            if item[0] == "$1" or item[0] == "$2" or item[0] == "$3":
                continue
    
            token_list.append(item)
        
        return token_list
    
    def reduce_pointer( self , pointer:list , stack:list ): # pop all pointer which where reduced
        
        pointer.reverse()
        
        new_pointer = []
        for p in pointer:
            
            if p[0] <= len(stack) - 1 and p[1] == stack[p[0]][0]:
                new_pointer.append(p)
        
        new_pointer.append(pointer[-1])
        new_pointer.reverse()
        
        return stack,new_pointer
    
    def parsed_code(self,stack):
        
        if len(stack) == 3 and (stack[1][0] == "E" or stack[1][0] == "b" ):
            
            self.derivation_Tree = stack[1][1]
            return True

        return False
    
    def gradient_parser(self,gramar,stack:list , code ):        
        '''
        parse the string using gradient parser
        
        '''
        index_pointer = 1
        
        shift = True
        
        while index_pointer <  len(code) :
            
            next_pointer =- 1
            
            shift = self._shift_reduce( pivot= code[index_pointer][0] ,index_pointer= len(stack) ,next_point= -1 ) # determines action | shift or reduce
                    
            while not shift:
                
                stack , modified = self.reduce_stack(stack ,gramar , next_pointer ) # try to reduce 
        
                if not modified: # verify any change in the stack
                    
                    next_pointer -=1 # check agin for reduction but using another pointer in the stack pointer
                    shift = self._shift_reduce( pivot= code[index_pointer][0] ,index_pointer = len(stack) , next_point= next_pointer ) 
                
                else: 
                    
                    next_pointer =- 1 # if reduction was made , restart pointer in the stack pointer

                    stack,self.stack_pointer = self.reduce_pointer( self.stack_pointer ,stack) # reduce the stack pointer
                    
                    shift = shift = self._shift_reduce( pivot= code[index_pointer][0] ,index_pointer = len(stack) , next_point= next_pointer ) # check again | shift or reduce
            
            stack.append( code[index_pointer] )
            
            index_pointer += 1
    
        return self.parsed_code(stack)
    
    def derivation_tree(self, label , token_list):
        
        '''
        pattern to follow -> existing tree is child of the new node
        '''
        
        #AST_node = dt.builder( label , token_list ).ASTNode # pick the builder
        
        return None