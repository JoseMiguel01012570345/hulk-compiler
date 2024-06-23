
import GRAMMAR_PRODUCTIONS as GD
import production_class_representation as pcr
import builder as B
import visitor as V
import copy
from HULK_LANGUAGE_DEFINITION import SYMBOLS_and_OPERATORS_parser as symb_and_op

class Parser:
    
    """
    GRAMMATIC PARSING

    """
    parser_table = []
    terminals = GD.terminals
    non_terminals = GD.non_terminals
    
    def __init__(self , code="" ):

        self._grammar = GD.grammar
    
        self._error = None
        self.derivation_Tree = None
        
        printing=1
        
        if printing == 1:
            file = open("automata_states_log","w")
            file.write("")
            file.close()
        
        i0 = self.I0(printing=printing)
        
        parser_table = self.automaton(i0=i0,printing=printing)
        
        self.parser_table = parser_table
        
        # if printing:
        #     i=0
        #     for element in parser_table:
        #         print(f"I{i}={element}")
        #         i+=1
        
        ok , tree = self.parse_input(code=code)
        self.tree = tree
        
        if not ok:
            self._error = True
        
        else:
            print(f"\033[1;32m {ok} \033[0m")
        
        pass
    
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
        
        for feature in self._grammar:
        
            for p in feature:
                
                derivation = p.derivation
                        
                if derivation[0] == alpha:
                
                    if self.contains( derivation[1][0] , self.terminals ):
                        return derivation[1][0]
                
                    else:
                        
                        if visited.__contains__(derivation[1][0]):
                            continue
                        
                        if len(derivation[1][0]) != 0:
                        
                            terminal = self.non_terminal_first( derivation[1][0] , visited )
                        
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
        
        s = "\n"
        s += f"I{state_number}" + "= { "
        s += "\n"
        for dic in state:

            s += self.print_production(dic["production"],dic["look_ahead"],dic["pivote"])
            s += "\n"

            pass
        
        s += " }"
        
        # input()
        file = open("automata_states_log","a")
        file.write(s)
        file.close()
        
        pass
    
    def print_production(self,production,look_ahead,pivote):
        
        s=""
        for item in production[1]:
            s +=  item + " "
        
        s = str(production[0]) + "->" + s + ", c=\"" + look_ahead + "\""  + ", pivote:" + str(pivote)
        
        return s
    
    def I0(self,printing=True):
        
        i = 1
        key_stone = ""
        look_ahead = ""
        
        AST = pcr.ASTNode({  "derivation": ["S",["E"]] , "identifier": "S->E" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ),
        
        i0 = [ { "production": ["S" , ["E"]] , "look_ahead": "$" , "pivote": -1 ,"AST":AST } ]
        key_stone = "E"
        look_ahead = "$"
        
        self.build_state(state=i0,key_stone=key_stone,look_ahead=look_ahead,pivote=-1) 
        
        while True:
            
            if i >= len(i0): break
            
            derivation = i0[i]["production"]
            
            look_ahead , key_stone = self.first( derivation[1] , pivote=-1 ,look_ahead=i0[i]["look_ahead"] )
                
            if key_stone == "": 
                i+=1
                continue
            
            self.build_state(state=i0,key_stone=key_stone,look_ahead=look_ahead,pivote=-1) 
            
            i+=1
        
        if printing:
            self.print_state(state_number=0,state=i0)
        
        return i0
    
    def build_state( self , state:list , key_stone , look_ahead , pivote= -1):
        
        grammar = self._grammar
        
        for feature in grammar:
            
            for productions in feature:
            
                production= { "production": productions.derivation , "look_ahead" : look_ahead , "pivote":pivote , "AST": productions }
                
                if production["production"][0] == key_stone and not self.in_stack( state , production ) :
                    state.append( production )
                    
        pass
    
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
        found = False
        error = False
        
        while i < len(state):
            
            right_derivation_side = state[i]["production"][1]
            
            derivation_pivote= state[i]["pivote"]
            
            if  derivation_pivote + 1 >= len(right_derivation_side) or \
                right_derivation_side[ derivation_pivote + 1] != item:
                
                if  state[i]["pivote"] == len(state[i]["production"][1]) -1 and state[i]["look_ahead"] == item :
                    
                    if found:
                        error = True
                    
                    found = True
                    my_row[item] = (state[i]["production"],state[i]["AST"])
                    if state[i]["production"][0] == "S":
                        my_row[item] = "OK"
                     
                i+=1
                continue
            
            new_state.append( {
                "production":state[i]["production"] ,
                "look_ahead":state[i]["look_ahead"] ,
                "pivote":state[i]["pivote"] + 1 ,
                "AST": state[i]["AST"]
                } )
            
            my_row[item] = state_number + 1
            
            look_ahead , key_stone = self.first( right_derivation_side , pivote=new_state[-1]["pivote"] ,look_ahead=new_state[-1]["look_ahead"] )
            
            if key_stone == "": 
                i+=1
                continue
            
            j = len(new_state)
            
            self.build_state( state=new_state, key_stone=key_stone , look_ahead=look_ahead , pivote=-1 ) 
            
            while True:
            
                if j >= len(new_state): break
                
                derivation = new_state[j]["production"]
                
                look_ahead , key_stone = self.first( derivation[1] , pivote=-1 ,look_ahead=new_state[j]["look_ahead"] )
                    
                if key_stone == "": 
                    j+=1
                    continue
                
                self.build_state(state=new_state,key_stone=key_stone,look_ahead=look_ahead,pivote=-1) 
                
                j+=1
            
            i+=1
        
        return new_state , my_row , error

    def calculated_state(self, state , stack_state ,item , actual_state )->bool:
        
        i=0
        for sub_state in stack_state:
            count = 0
            
            if len(sub_state) == len(state):
                
                for derivation in state:
                    if self.in_stack(sub_state,derivation): count+=1
            
            if count == len(state) and len(state) != 0 :
                # print(f"GOTO(I{ actual_state },{item}):")
                # print(f"\033[1;31m state I{i} is repeated \033[0m")
                return True,i
            
            i+=1
        
        return False,i

    def automaton(self,i0 , printing=True):
        
        T_U_N =  [ item for item in self.terminals]
        T_U_N.extend(self.non_terminals)
        
        parser_table=[]
        
        stack_state = [i0]
        
        current_state=0
        states_created = 0
    
        while current_state < len(stack_state):
            
            my_row =self.fill_row(T_U_N)
            
            for item in T_U_N:
                
                state,my_row,error = self.GOTO( stack_state[current_state] , item , states_created , my_row )
                
                if error:
                    
                    if printing:
                        
                        file = open("automata_states_log","a")
                        file.write(f"\n GOTO(I{current_state},{item}):")
                        file.close()
                        
                        self.print_state(state_number=len(stack_state)-1,state=state)
                        print("grammar is not LR(1)")
                        exit()
                    
                    else:
                        print("grammar is not LR(1)")
                        exit()
                
                calculated,index = self.calculated_state( state=state, stack_state=stack_state ,item=item ,actual_state=states_created)
                
                if len(state) !=0  and not calculated :
                    
                    states_created += 1
                    stack_state.append(state) 
                    
                    if printing:
                        file = open("automata_states_log","a")
                        file.write(f"\n GOTO(I{current_state},{item}):")
                        file.close()
                        
                        self.print_state(state_number=len(stack_state)-1,state=state)
                
                elif calculated:
                                        
                    my_row[item] = index                    
                    pass

            parser_table.append(my_row)
            current_state += 1
            pass
        
        return parser_table

    def parse_input(self,code) -> bool:
    
        symbols = []
        state = [0]
        tree = []
        
        k = 0
        while k < len(code):
            
            item = code[k].Text
            
            if not self.special_token(item=item):
                item = "int"
                
            result =""
            
            if dict(self.parser_table[ state[-1] ]).__contains__( item ) : 
                result = self.parser_table[ state[-1] ][ item ]
                
                if result == "*":
                    print("invalid string in language")
                    return False , None
            
            else: # no language belongness
                print(f"\033[1;31m >> ERROR: item \033[1;33m {item} \033[1;31m is not valid \033[0m")
                return False , None

            if type(result) == int: # shift
                
                state.append(result)
                
                symbols.append(item)
                    
                print(symbols , f"state={state[-1]}" )
                
                tree.append(code[k])
                
                pass
            
            elif type(result) == tuple: # reduce
                
                i = 0
                token_list = []
                
                while i < len(result[0][1]):
                    state.pop()
                    
                    token = tree[-1]
                    
                    token_list.insert(0,token)
                    
                    symbols.pop()
                    tree.pop()
                    i += 1
                
                    print(symbols, f"state={state[-1]}")
                
                ast = copy.deepcopy(result[1])
                
                ast_initialized = ast.ignition(token_list=token_list)
                tree.append(ast_initialized)
                    
                key_stone = result[0][0]
                last_state_number = state[-1]
                
                if self.parser_table[ last_state_number ][ key_stone ] == "*":
                    print("invalid string")    
                    return False , None
                
                state.append( self.parser_table[ last_state_number ][ key_stone ] )
                
                symbols.append(key_stone)
                print(symbols, f"state={state[-1]}" )
                
                continue  
                
            elif result == "OK":
                return True , tree[0]
            
            else: # error
                print(f"\033[1;31m >> ERROR: item \033[1;33m {item} \033[1;31m is not valid \033[0m")
                return False , None
            
            k +=1
    
    def special_token(self,item):
        return self.terminals.__contains__(item) or symb_and_op.__contains__(item)