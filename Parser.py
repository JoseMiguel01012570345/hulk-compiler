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
        ['.'],
        [':'],
        ["let"],
        ['as'],
        ['^','%','**'],
        ['*','/'],
        ['+','-'],
        ['>','<','>=','<=','==', '!' ,'is'],
        ['&','|','!'],
        ['if'],
        ['elif'],
        ['else'],
        ['@','@@'],
        ['=','+=','-=','/=','*=','--',':=','++','--'],
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
        
<<<<<<< HEAD
        for operators in self.operator_procedence:
            
            if list(operators).__contains__(pivote) and list(operators).__contains__(pointer):
                return 0
=======
        b = beta[0]
        
        # check if b is a terminal , otherwise we check the non-terminals
        if self.contains( b , self.terminals ):
            return b , ""
        
        if pivote + 2 >= len(derivation):
            return look_ahead,b
        
        non_terminal_first = self.non_terminal_first(derivation[pivote + 2])
        
        if non_terminal_first == "":
            return look_ahead , b
        
        return non_terminal_first,b
        
    def in_stack( self , stack , my_derivation ) -> bool:
        
        for derivation in stack:
>>>>>>> 9c513df (parser bug fixed at repeated states)
            
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
    
<<<<<<< HEAD
    def remove_item_stack(self , stack:list ,pop_number):
=======
    def print_state(self, state_number , state):
        
        print( f"\033[1;32m I{state_number} \033[0m" , "=\033[1;33m { \033[0m")    
        for dic in state:

            self.print_production(dic["production"],dic["look_ahead"],dic["pivote"])

            pass
        
        print("\033[1;33m } \033[0m")
        
        pass
    
    def print_production(self,production,look_ahead,pivote):
        
        s=""
        for item in production[1]:
            s +=  item + " "
        
        print("\033[1m" , production[0] , "->" , s , f", c=\"{look_ahead}\"" , ", pivote:" , pivote , "\033[0m" )
        
        pass
    
    def I0(self):
        
        i = 1
        key_stone = ""
        look_ahead = ""
        
        i0 = [ { "production": ["S" , ["E"]] , "look_ahead": "$" , "pivote": -1 } ]
        key_stone = "E"
        look_ahead = "$"
        
        while True:
            
            self.build_state(state=i0,key_stone=key_stone,look_ahead=look_ahead,pivote=-1) 
            
            if i >= len(i0): break
            
            derivation = i0[i]["production"]
            
            look_ahead , key_stone = self.first( derivation[1] , pivote=-1 ,look_ahead=i0[i]["look_ahead"] )
                
            if key_stone == "": 
                i+=1
                continue
            
            i+=1
        
        self.print_state(state_number=0,state=i0)
        return i0
    
    def build_state( self , state:list , key_stone , look_ahead , pivote= -1):
        
        grammar = self._grammar
        new_stack = []
        
        for feature in grammar:
            
            for productions in feature:
            
                production= { "production": productions , "look_ahead" : look_ahead , "pivote":pivote}
                if productions[0] == key_stone and not self.in_stack( state , production ) :
                    state.append( production )
                
        return new_stack
    
    def fill_row(self,row):
        
        my_row={}
        
        for item in row:
            my_row[item] = "*"
        
        return my_row
    
    def GOTO( self , state=None , item=None , state_number=0, my_row={} ):
        
        i = 0
        key_stone = ""
        look_ahead = ""
        new_state = []
        
        while i < len(state):
            
            right_derivation_side = state[i]["production"][1]
            
            derivation_pivote= state[i]["pivote"]
            
            if  derivation_pivote + 1 >= len(right_derivation_side) or \
                right_derivation_side[ derivation_pivote + 1] != item:
                
                if state[i]["pivote"] == len(state[i]["production"][1]) -1 and state[i]["look_ahead"] == item :
                    my_row[item] = state[i]["production"]
                    if state[i]["production"][0] == "S":
                        my_row[item] = "OK"
                     
                i+=1
                continue
            
            new_state.append( {
                "production":state[i]["production"] ,
                "look_ahead":state[i]["look_ahead"] ,
                "pivote":state[i]["pivote"] + 1 } )
            
            my_row[item] = state_number + 1
            
            look_ahead , key_stone = self.first( right_derivation_side , pivote=new_state[-1]["pivote"] ,look_ahead=new_state[-1]["look_ahead"] )
            
            if key_stone == "": 
                i+=1
                continue
            
            self.build_state( state=new_state, key_stone=key_stone , look_ahead=look_ahead , pivote=-1 ) 
            
            i+=1
        
        return new_state , my_row

    def calculated_state(self, state , stack_state ,item , actual_state )->bool:
>>>>>>> 9c513df (parser bug fixed at repeated states)
        
        i=0
        while i < pop_number:
            
<<<<<<< HEAD
            stack.pop()
=======
            if len(sub_state) == len(state):
                
                for derivation in state:
                    if self.in_stack(sub_state,derivation): count+=1
            
            if count == len(state) and len(state) != 0 :
                print(f"GOTO(I{ actual_state },{item}):")
                print(f"\033[1;31m state I{i} is repeated \033[0m")
                return True,i
>>>>>>> 9c513df (parser bug fixed at repeated states)
            
            i +=1
        
        return stack

    def reduce_stack(self , stack:list , grammar , next_point ):
            
        # ----------------------PRINT_STACK-----------------
                        
        # printing_stack = []
        # for item in stack:
        #     printing_stack.append(item[0])
        
        # print(printing_stack)
        
        # -------------------------------------------------
            
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
            
            # --------------------PRINT_STACK-----------------------------
                        
            # printing_stack = []
            # for item in new_stack:
            #     printing_stack.append(item[0])
            
            # printing_stack.append(best_match)
            # print(printing_stack)
            
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
            print(" \033[1;31m >\033[1;32m CODE HAS BEEN PARSED :) \033[0m")
            
            return True

        print(" \033[1;32m >\033[1;31m CODE HAS ERRORS :( \033[0m")
        
<<<<<<< HEAD
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
=======
        return False,i

    def automaton(self,i0):
        
        T_U_N =  [ item for item in self.terminals]
        T_U_N.extend(self.non_terminals)
        
        parser_table=[]
        
        stack_state = [i0]
        
        current_state=0
        states_created = 0
        while current_state < len(stack_state):
            
            my_row =self.fill_row(T_U_N)
            
            for item in T_U_N:
                if current_state == 5 and item == "T":
                    print()       
                state,my_row = self.GOTO( stack_state[current_state] , item , states_created , my_row )
                
                calculated,index = self.calculated_state( state=state, stack_state=stack_state ,item=item ,actual_state=states_created)
                
                if len(state) !=0  and not calculated :
                    
                    states_created += 1
                    stack_state.append(state) 
                    
                    print(f"GOTO(I{current_state},{item}):")
                    self.print_state(state_number=len(stack_state)-1,state=state)
                
                elif calculated:
                                        
                    my_row[item] = index                    
                    pass
                    
            parser_table.append(my_row)
            current_state += 1
            pass
>>>>>>> 9c513df (parser bug fixed at repeated states)
        
        return self.parsed_code(stack)
    
    def derivation_tree(self, label , token_list):
        
        '''
        pattern to follow -> existing tree is child of the new node
        '''
            
        AST_node = dt.builder( label , token_list ).ASTNode # pick the builder
        
        return AST_node