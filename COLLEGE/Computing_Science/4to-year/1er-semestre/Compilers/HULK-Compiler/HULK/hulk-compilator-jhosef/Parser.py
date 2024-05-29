# from RegExDefinitions import TokenFinitRegEx
# from RegExInterface import State,IRegEx
# import GRAMMAR_PRODUCTIONS as GD
# import DerivationTree as dt

from os import system

class Parser:
    
    """
    GRAMMATIC PARSING

    """
    parser_table = []
    def __init__(self,grammar,code ):

        self._grammar = grammar
        self._error = None
        self._match = False
        self.derivation_Tree = None
        
        i0 = self.I0()
        
        parser_table = self.automaton(i0=i0)
        
        self.parser_table = parser_table
        
        i=0
        for element in parser_table:
            print(f"I{i}={element}")
            i+=1
        
        ok = self.parse_input(code=code)
        
        if not ok:
            self._error = True
        
        else:
            print(f"\033[1;32m {ok} \033[0m")
        
        pass
        
    non_terminals = [
            
            
            "E",
            "A",
            "X",
        ]
    
    terminals= [
        
            "+" ,
            "=" ,
            "i" ,
            "$" , 
        ]
    
    grammar = [
        
        [ "S" ,  [ "E" ] ] ,
        [ "E" ,  ["A", "X" , "=","A"] ] ,
        [ "E" ,  ["i"] ] ,
        [ "A" ,  ["i","+","A"] ] ,
        [ "A" ,  ["i"] ] ,
        
     ]
    
    def contains(self , my_token , dic: list):
        
        return dic.__contains__(my_token)
            
    @property
    def Error(self):
        return self._error
    
    def non_terminal_first(self , alpha , visited:list=[] ):
        
        if self.contains(alpha,self.terminals):
            return alpha
        
        visited.append(alpha)
        
        terminal = ""
        for p in self.grammar:
            
            if p[0] == alpha:
            
                if self.contains( p[1][0] , self.terminals ):
                    return p[1][0]
            
                else:
                    
                    if visited.__contains__(p[1][0]):
                        continue
                    
                    if len(p[1][0]) != 0:
                    
                        terminal = self.non_termina_first( p[1][0] , visited )
                    
                        if terminal != "":
                            return terminal
        
        return ""
        
    def first(self , derivation:list , pivote: int ,look_ahead="$"):
        
        beta = derivation[pivote + 1:]
        
        if len(beta) == 0:
            return "$" , ""
        
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
            
            if self.equal_(derivation1=derivation , derivation2=my_derivation):
                return True
        
        return False
    
    def equal_(self,derivation1,derivation2):
        
        if derivation1["production"][0] != derivation2["production"][0] or len(derivation1["production"][1]) != len(derivation2["production"][1]) : 
            return False
        
        deriv_tuple = zip(derivation1["production"][1],derivation2["production"][1])
        
        for deriv in deriv_tuple:
            
            if deriv[0] != deriv[1]: return False
        
        if derivation1["look_ahead"] != derivation2["look_ahead"]: 
            return False
        
        if derivation1["pivote"] != derivation2["pivote"]: 
            return False
        
        return True
    
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
        
        i = 0
        key_stone = ""
        look_ahead = ""
        
        i0 = [ { "production": self.grammar[0] , "look_ahead": "$" , "pivote": -1 } ]
        key_stone = "E"
        look_ahead = "$"
        
        while True:
            
            self.build_state(state=i0,key_stone=key_stone,look_ahead=look_ahead,pivote=-1) 
            
            i+=1
            if i == len(i0): break
            
            derivation = i0[i]["production"]
            
            look_ahead , key_stone = self.first( derivation[1] , pivote=-1 ,look_ahead=i0[i]["look_ahead"] )
                
            if key_stone == "": 
                i+=1
                continue
            
            i+=1
        
        # self.print_state(state_number=0,state=i0)
        return i0
    
    def build_state( self , state:list , key_stone , look_ahead , pivote= -1):
        
        grammar = self.grammar
        new_stack = []
        for productions in grammar:
            
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
        
        i=0
        for sub_state in stack_state:
            count = 0
            
            if len(sub_state) == len(state):
                
                for derivation in state:
                    if self.in_stack(sub_state,derivation): count+=1
                
            if count == len(state):
                # print(f"GOTO(I{ actual_state },{item}):")
                # print(f"\033[1;31m state I{i} is repeated \033[0m")
                return True
            
            i+=1
        
        return False

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
                                
                state,my_row = self.GOTO( stack_state[current_state] , item , states_created , my_row )
                
                if len(state) !=0  and not self.calculated_state( state=state, stack_state=stack_state ,item=item ,actual_state=states_created):
                    
                    states_created += 1
                    stack_state.append(state) 
                    
                    # print(f"GOTO(I{current_state},{item}):")
                    # self.print_state(state_number=len(stack_state)-1,state=state)
                
                pass
            
            parser_table.append(my_row)
            current_state += 1
            pass
        
        return parser_table

    def parse_input(self,code) -> bool:

        state = [0]
        tree = []
        
        k = 0
        while k < len(code):
            
            item = code[k]
            
            result =""
            
            if dict(self.parser_table[ state[-1] ]).__contains__( item ) : 
                result = self.parser_table[ state[-1] ][item]
            else:
                print(f"\033[1;31m >> ERROR: item \033[1;33m {item} \033[1;31m is not valid \033[0m")
                return False

            if type(result) == int: # shift
                
                state.append(result)
                pass
            
            elif type(result) == list: # reduce
                
                i = 0
                while i < len(result[1]):
                    state.pop()
                    i += 1
                
                key_stone = result[0]
                last_state_number = state[-1]
                state.append( self.parser_table[ last_state_number ][ key_stone ] )
                
                continue  
                
            elif result == "OK":
                return True
            
            else:
                print(f"\033[1;31m >> ERROR: item \033[1;33m {item} \033[1;31m is not valid \033[0m")
                return False
            
            k +=1
        
        pass

system("cls")
p = Parser(None,[ "i" , "=" , "i" , "$"])