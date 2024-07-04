<<<<<<< HEAD
from RegExDefinitions import TokenFinitRegEx
from RegExInterface import State,IRegEx
=======

>>>>>>> 344c94b (all on board)
import GRAMMAR_PRODUCTIONS as GD
<<<<<<< HEAD
import DerivationTree as dt

class Parser():
=======
import production_class_representation as pcr
import builder as B
import visitor as V
import copy
from HULK_LANGUAGE_DEFINITION import SYMBOLS_and_OPERATORS_parser as symb_and_op
import json
import os

class Parser:
>>>>>>> b1116a1 (AST almost integrated to parser)
    
    """
    PARSER

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
    
    def __init__(self , code="" , use_saved_table=1  ):

        self._grammar = GD.grammar
    
        self._error = None
        self._match = False
        self._stack = []
        self.derivation_Tree = None
        
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        parsed_code = self.gradient_parser(grammar,self._stack,code)
        
<<<<<<< HEAD
        if not parsed_code:
=======
        parser_table = self.automaton(i0=i0)
=======
        printing=0
=======
        printing=1
>>>>>>> b1116a1 (AST almost integrated to parser)
=======
        printing=0
>>>>>>> c1b5cd8 (parser-ast integrated)
=======
        printing=1
        
        if printing == 1:
            file = open("automata_states_log","w")
            file.write("")
            file.close()
>>>>>>> cb6fe93 (fixes made to grammar)
        
        i0 = self.I0(printing=printing)
        
        parser_table = self.automaton(i0=i0,printing=printing)
>>>>>>> 20b2c73 (perfect)
        
        self.parser_table = parser_table
=======
        self.read_from_json(1)
=======
        self.read_from_json(use_saved_table)
>>>>>>> e1988ab (fixing context issues)
        
        if len(self.parser_table) == 0:
        
            printing=1
            
            if printing == 1:
                file = open("automata_states_log","w")
                file.write("")
                file.close()
            
            i0 = self.I0(printing=printing)
            
            parser_table = self.automaton(i0=i0,printing=printing)
            
            self.parser_table = parser_table
            
            self.save_table()
            
>>>>>>> ddcf070 (improvements to run the parser , parser_table saved in json)
        
        ok , tree = self.parse_input(code=code)
        self.tree = tree
        
        if not ok:
>>>>>>> 31c5d2d (moving out verbose info)
            self._error = True
        
<<<<<<< HEAD
=======
        else:
            print(f"\033[1;32m {ok} \033[0m")
        
>>>>>>> 5689be6 (steps to code -> search_in_ast <- hard coded)
        pass
    
<<<<<<< HEAD
=======
    def contains(self , my_token , dic: list):
        return dic.__contains__(my_token)
<<<<<<< HEAD
        
>>>>>>> d3a2291 (blocks made)
=======
    
<<<<<<< HEAD
>>>>>>> d553c9f (ast representation with networkx)
=======
    def printing_table(self , allow):
        
        if not allow : 
            return
        
        for row in self.parser_table:
            print(row)
    
>>>>>>> ddcf070 (improvements to run the parser , parser_table saved in json)
    @property
    def Error(self):
        return self._error
    
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
    def save_table(self):
        
        with open("parser_table.json","w") as file:
            json.dump(self.parser_table , file)    
            file.close()
        
        pass
    
    def read_from_json(self, allow):
        
        if not allow : 
            return
        
        with open("parser_table.json","r") as file:
            self.parser_table =  json.load(file)
            
        pass
    
>>>>>>> ddcf070 (improvements to run the parser , parser_table saved in json)
    def non_terminal_first(self , alpha , visited:list=[] , my_set:list=[] ):
        
        if self.contains(alpha,self.terminals): # is alpha , a terminal?
            
            my_set.append(alpha)
            return my_set
>>>>>>> ce54e3f (error detected in parser, fixed)
        
        '''
        compare precedence between operator1 and operator2:
        ->  0: equal procedence
        ->  1: grater procedence
        -> -1: lower procedence        
        '''
        
<<<<<<< HEAD
        if pivote == "(" : return 0
        if pivote == "{" : return 0
        if pivote == "[" : return 0
        
        if pointer == "(" and ( pivote == ")" ) : return -1
=======
        for feature in self._grammar:
>>>>>>> ce54e3f (error detected in parser, fixed)
        
<<<<<<< HEAD
        if pointer == "{" and ( pivote == "}" ): return -1
=======
            for p in feature:
                
                derivation = p.derivation
                        
                if derivation[0] == alpha:
                
                    if self.contains( derivation[1][0] , self.terminals ):
                        
                        my_set.append(derivation[1][0])
                        return my_set
                
                    else:
                        
                        if visited.__contains__(derivation[1][0]):
                            continue
                        
                        if len(derivation[1][0]) != 0:
                        
<<<<<<< HEAD
                            terminal = self.non_terminal_first( derivation[1][0] , visited )
                        
                            if terminal != "":
                                return terminal
>>>>>>> 4ea3226 (another fix to the parser, chose the first reduction)
        
        if pointer == "[" and ( pivote == "]"): return -1
=======
                            self.non_terminal_first( derivation[1][0] , visited , my_set=my_set )
            
        return my_set
>>>>>>> ce54e3f (error detected in parser, fixed)
        
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
            return [look_ahead],b
        
        non_terminal_first = self.non_terminal_first(derivation[pivote + 2],[],[])
        
        if len(non_terminal_first) == 0:
            return [look_ahead] , b
        
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
<<<<<<< HEAD
    def remove_item_stack(self , stack:list ,pop_number):
=======
    def print_state(self, state_number , state):
=======
    def save_state(self, state_number , state):
>>>>>>> ddcf070 (improvements to run the parser , parser_table saved in json)
        
        s = "\n"
        s += f"I{state_number}" + "= { "
        s += "\n"
        for dic in state:

            s += self.save_production(dic["production"],dic["look_ahead"],dic["pivote"])
            s += "\n"

            pass
        
        s += " }"
        
        # input()
        file = open("automata_states_log","a")
        file.write(s)
        file.close()
        
        pass
    
    def save_production(self,production,look_ahead,pivote):
        
        s=""
        for item in production[1]:
            s +=  item + " "
        
        s = str(production[0]) + "->" + s + ", c=\"" + look_ahead + "\""  + ", pivote:" + str(pivote)
        
        return s
    
    def I0(self,printing=True):
        
        i = 1
        key_stone = ""
        look_ahead = ""
        
        AST = pcr.ASTNode({  "derivation": ["S",["exp"]] , "identifier": "S->E" , "definition_node?": False ,"builder": B.replacement , "visitor": V.replacement } ),
        
        i0 = [ { "production": ["S" , ["exp"]] , "look_ahead": "$" , "pivote": -1 ,"AST":AST } ]
        key_stone = "exp"
        look_ahead = "$"
        
        self.build_state(state=i0,key_stone=key_stone,look_ahead=look_ahead,pivote=-1) 
        
        while True:
            
            if i >= len(i0): break
            
            if i == 5: 
                print()
            derivation = i0[i]["production"]
            
            look_ahead , key_stone = self.first( derivation[1] , pivote=-1 ,look_ahead=i0[i]["look_ahead"] )
                
            if key_stone == "": 
                i+=1
                continue
            
            self.build_state(state=i0,key_stone=key_stone,look_ahead=look_ahead,pivote=-1) 
            
            i+=1
        
        if printing:
            self.save_state(state_number=0,state=i0)
        
        return i0
    
    def build_state( self , state:list , key_stone , look_ahead , pivote= -1):
        
        grammar = self._grammar
        
        i = 0
        for feature in grammar:
            
            for productions in feature:
                   
                for c in look_ahead:
                
                    production= { "production": productions.derivation , "look_ahead" : c , "pivote":pivote , "AST": i }
                    
                    if production["production"][0] == key_stone and not self.in_stack( state , production ) :
                        state.append( production )
                
                i += 1
    
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
<<<<<<< HEAD
                # print(f"GOTO(I{ actual_state },{item}):")
                # print(f"\033[1;31m state I{i} is repeated \033[0m")
                return True,i
>>>>>>> 9c513df (parser bug fixed at repeated states)
=======
                return True , i
>>>>>>> d553c9f (ast representation with networkx)
            
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
                        
                        self.save_state(state_number=len(stack_state)-1,state=state)
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
                        
                        self.save_state(state_number=len(stack_state)-1,state=state)
                
                elif calculated:
                                        
                    my_row[item] = index                    
                    pass

            parser_table.append(my_row)
            current_state += 1
            pass
>>>>>>> 9c513df (parser bug fixed at repeated states)
        
<<<<<<< HEAD
        return self.parsed_code(stack)
    
    def derivation_tree(self, label , token_list):
=======
        return parser_table

    def parse_input(self,code) -> bool:
    
        symbols = []
        state = [0]
        tree = []
>>>>>>> c5c76dc (refactoring)
        
        '''
        pattern to follow -> existing tree is child of the new node
        '''
            
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        AST_node = dt.builder( label , token_list ).ASTNode # pick the builder
        
        return AST_node
=======
            # item = code[k].Text
            item = code[k]
=======
            item = code[k].Text
<<<<<<< HEAD
            # item = code[k]
>>>>>>> 344c94b (all on board)
=======
>>>>>>> c5c76dc (refactoring)
=======
            item = code[k]
>>>>>>> 3c71142 (asigment and variable declaration , ok)
=======
            item = code[k].Text
>>>>>>> d3a2291 (blocks made)
            
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
            
            elif type(result) == tuple or type(result) == list : # reduce
                
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
                
                result_ast = self.search_ast_in_grammar(result[1])
                
                ast = copy.deepcopy(result_ast)
                
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
<<<<<<< HEAD
        
<<<<<<< HEAD
        pass
<<<<<<< HEAD

<<<<<<< HEAD
p = Parser()
>>>>>>> 5798f64 (another fix to the parser)
=======
# p = Parser()
>>>>>>> 344c94b (all on board)
=======
>>>>>>> c5c76dc (refactoring)
=======
=======
>>>>>>> cb6fe93 (fixes made to grammar)
    
    def search_ast_in_grammar( self , i ):
        
        grammar = self._grammar    
        
        k = 0
        for feature in grammar:
            
            for productions in feature:
                
                if k == i: 
                    return productions    
                k += 1
                
        raise Exception("no index found")
    
    def special_token(self,item):
        return self.terminals.__contains__(item) or symb_and_op.__contains__(item)
<<<<<<< HEAD
>>>>>>> d3a2291 (blocks made)
=======
    
>>>>>>> 00754c6 (high level expression can peform arithmetic operations)
