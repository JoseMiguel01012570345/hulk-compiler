from . import setstools
PowerSet = setstools.PowerSet

class State:
    
    """
    An abstraction of a state for an automaton
    
    kwargs: arguments for the initialization of one state
    
    'value' -> the value stored on this state
    'final' -> true if this state is final
    'fault' -> true if this state is fault
    'formatter' -> function to format the value stored in this state when the property 'Value' is asked(default self-value)
    'label' -> identifier for this state when is compared with other state(default is the string representation for the value)
    """
    
    def __init__(self,**kwargs):
        self._transitions = {}
        self._epsilon_transitions = {}
        if 'value' in kwargs.keys():
            self._value = kwargs['value']
            pass
        else:
            self._value = None
            pass
        if 'final' in kwargs.keys():
            self._final = kwargs['final']
            pass
        else:
            self._final = False
            pass
        if 'fault' in kwargs.keys():
            self._fault = kwargs['fault']
            pass
        else:
            self._fault = False
            pass
        if 'formatter' in kwargs.keys():
            self._formatter = kwargs['formatter']
            pass
        else:
            self._formatter = lambda x: x
            pass
        if 'label' in kwargs.keys():
            self._label = kwargs['label']
            pass
        else:
            self._label = str(self._value)
            pass
        pass
    
    def __str__(self):
        return self._label
    
    def __repr__(self):
        return self._label
    
    @property
    def Label(self):
        """
        the identifier for this state
        """
        return self._label
    
    @property
    def Final(self):
        """
        true if this state is a final state
        """
        return self._final
    
    @property
    def Fault(self):
        """
        true if this state is a fault state
        """
        return self._fault
    
    @property
    def Value(self):
        """
        the value stored in this state
        """
        return self._formatter(self._value)
    
    @property
    def Transitions(self):
        """
        the transitions asociated to this state
        """
        return self._transitions
    
    @property
    def EpsilonTransitions(self):
        """
        the epsilon-transitions asociated to this state
        """
        return self._epsilon_transitions
    
    def has_transition(self,symbol):
        """
        true if there's transition for this state given the symbol
        """
        return symbol in self._transitions.keys() or len(self._epsilon_transitions) > 0
    
    def add_transition(self,symbol,state):
        """
        adds a new transition for the given symbol to the specified state
        """
        if not isinstance(state,State):
            raise Exception('state most be an instance of "State" class')
        self._transitions[symbol] = state
        pass
    
    def add_transitions(self,**kwargs):
        """
        kwargs: symbol,state
        adds a news transitions given the symbols and its states corresponding
        """
        for symbol in kwargs.keys():
            if not isinstance(kwargs[symbol],State):
                raise Exception('all the states most be instances of "State" class')
            self._transitions[symbol] = kwargs[symbol]
            pass
        pass
    
    def add_epsilon_transition(self,symbol,state):
        """
        adds a new epsilon-transition for the given symbol to specified state
        """
        if not isinstance(state,State):
            raise Exception('state most be instance of "State" class')
        if not symbol in self._epsilon_transitions.keys():
            self._epsilon_transitions[symbol] = []
            pass
        self._epsilon_transitions[symbol].append(state)
    
    def add_epsilon_transitions(self,symbol,*states):
        """
        adds a news epsilon-transitions for the given symbol and the given states
        """
        for state in states:
            if not isinstance(state,State):
                raise Exception('all the states most be instances of "State" class')
            pass
        if not symbol in self._epsilon_transitions.keys():
            self._epsilon_transitions[symbol] = []
            pass
        self._epsilon_transitions[symbol] += states
        pass
    
    def next(self,symbol):
        """
        return the next state to go given the symbol
        """
        if symbol in self._transitions.keys():
            return self._transitions[symbol]
        if symbol in self._epsilon_transitions.keys():
            return set([state for state in self._epsilon_transitions[symbol]])
        return State(fault=True)

    pass

class Automaton:
    
    """
    An abstraction of the automaton's definition
    
    start -> the initial state for this automaton(most be instance of State class)
    states -> the states of this automaton(most be instances of State class)
    WARNING!: start is on states may cause problems in some functionalitys, start is automatically added to the internals states 
    """
    
    def __init__(self,start,*states):
        if not isinstance(start,State):
                raise Exception(message='"start" most be instance from "State" class')
            
        for state in states:
            if not isinstance(state,State):
                raise Exception(message='all the states most be instances from "State" class')
            pass
        pass
    
        self._start = start
        self._states = set(states)
        self._states.add(start)
        self._current_state = start
        self._symbols = set()
        for state in self._states:
            for symbol in state.Transitions.keys():
                if not symbol in self._symbols:
                    self._symbols.add(symbol)
                    pass
                pass
            for symbol in state.EpsilonTransitions.keys():
                if not symbol in self._symbols:
                    self._symbols.add(symbol)
                    pass
                pass
            pass
        pass
    
    @property
    def Start(self):
        """
        returns the start state for this automaton
        """
        return self._start
    
    @property
    def States(self):
        """
        returns all the states for this automaton
        """
        for state in self._states:
            yield state
        pass
    
    @property
    def State(self):
        """
        return the current state for this automaton
        """
        if type(self._current_state) == set:
            label = str(tuple(s.Label for s in self._current_state))
            return State(value=self._current_state,label=label,final=any(s.Final for s in self._current_state),fault=not any(not s.Fault for s in self._current_state))
        return self._current_state
    
    @property
    def Symbols(self):
        """
        returns the symbols's set that this automaton can read
        """
        return self._symbols
    
    def set_symbols(self,symbols):
        """
        sets the symbols set for this automaton, always takes the union bettwen all the symbols transitions existents and the new set
        """
        new_symbols = set(symbols)
        for state in self._states:
            for symbol in state.Transitions.keys():
                if not symbol in new_symbols:
                    new_symbols.add(symbol)
                    pass
                pass
            for symbol in state.EpsilonTransitions.keys():
                if not symbol in new_symbols:
                    new_symbols.add(symbol)
                    pass
                pass
            pass
        self._symbols = new_symbols
        pass
    
    def get_transitions_set(self,states):
        """
        returns the union of the states-sets for which the given set of states has transitions
        WARNING!: THIS METHOD IS INTERNALLY USED, USE THIS METHOD DIRECTLY MAY LEAD TO PROBLEMS
        """
        transitions_set = {}
        for state in states:
            for symbol in state.Transitions.keys():
                if not symbol in transitions_set.keys():
                    transitions_set[symbol] = []
                    pass
                if not state.Transitions[symbol] in transitions_set[symbol]:
                    transitions_set[symbol].append(state.Transitions[symbol])
                    pass
                pass
            for symbol in state.EpsilonTransitions.keys():
                if not symbol in transitions_set.keys():
                    transitions_set[symbol] = []
                    pass
                for s0 in state.EpsilonTransitions[symbol]:
                    if not s0 in transitions_set[symbol]:
                        transitions_set[symbol].append(s0)
                        pass
                    pass
                pass
            pass
        return transitions_set
    
    def set_states_transitions(self,states,transitions):
        """
        sets all the transitions for all the states of for this automaton
        WARNING!: THIS METHOD IS USED INTERNALLY, USE THIS METHOD DIRECTLY MAY CAUSE PROBLEMS
        """
        for state in states:
            for symbol in transitions[state]:
                label = ''
                for s in transitions[state][symbol]:
                    label += s.Label
                    pass
                for s1 in states:
                    if s1.Label == label:
                        state.add_transition(symbol,s1)
                        break
                    pass
                pass
            pass
        pass
    
    def to_deterministic(self):
        """
        returns the deterministic automaton equivalent to this automaton
        WARNING!: FOR A COUNT OF STATES VERY LOW, THIS METHOD CAN BE SO SLOW, NOT RECOMENDED FOR NOW
        """
        states = []
        for state in PowerSet(self._states):
            if len(state) == 0: continue
            states.append(state)
            pass
        automaton_states = set()
        states_transitions_dict = {}
        for state in states:
            label = ''
            for s in state:
                label += s.Label
                pass
            s0 = State(label=label,value=state,final=any(s.Final for s in state))
            state_transitions = self.get_transitions_set(state)
            states_transitions_dict[s0] = state_transitions
            automaton_states.add(s0)
            pass
        self.set_states_transitions(automaton_states,states_transitions_dict)
        start = None
        for state in automaton_states:
            if len(state.Value) == 1 and state.Value[0] == self._start:
                start = state
                break
            pass
        automaton = Automaton(start,*[s for s in automaton_states if not s == start])
        return automaton
    
    def restart(self):
        """
        restart the state for this automaton
        """
        self._current_state = self._start
        pass
    
    def move(self,symbol):
        """
        make the transition asociated to the current state and the given symbol for this automaton
        """
        if type(self._current_state) == set:
            s0 = set()
            for state in self._current_state:
                temp = state.next(symbol)
                if type(temp) == set:
                    for s in temp:
                        if not s.Fault:
                            s0.add(s)
                            pass
                        pass
                    pass
                elif not temp.Fault:
                    s0.add(temp)
                    pass
                pass
            if len(s0) == 0:
                self._current_state = State(fault=True)
                pass
            else:
                self._current_state = s0
                pass
            pass
        else:
            self._current_state = self._current_state.next(symbol)
            pass
        pass
    
    def recognize(self,string):
        """
        returns true if this automaton recognize the given string of symbols
        """
        for i in range(len(string)):
            self.move(string[i])
            if self.State.Fault: break
            pass
        return self.State.Final
    
    def _make_start_transitions(self,new_start,new_states,new_final):
        """
        WARNING! -> USED INTERNALLY, DON'T USE OUT
        """
        for symbol in self._start.Transitions.keys():
            s0 = self._start.Transitions[symbol]
            if s0.Value == new_start.Value:
                new_start.add_transition(symbol,new_start)
                pass
            else:
                for state in new_states:
                    if state.Value == s0.Value:
                        new_start.add_transition(symbol,state)
                        break
                    pass
                pass
            pass
        for symbol in self._start.EpsilonTransitions.keys():
            states = self._start.EpsilonTransitions[symbol]
            for s0 in states:
                if s0.Value == new_start.Value:
                    new_start.add_epsilon_transition(symbol,new_start)
                    pass
                else:
                    for s1 in new_states:
                        if s0.Value == s1.Value:
                            new_start.add_epsilon_transition(symbol,s1)
                            break
                        pass
                    pass
                pass
            pass
        for symbol in self._symbols:
            if not symbol in new_start.Transitions.keys() and not symbol in new_start.EpsilonTransitions.keys():
                new_start.add_transition(symbol,new_final)
                pass
            pass
        pass
    
    def _make_states_transitions(self,new_start,new_states,new_final):
        """
        WARNING! -> USED INTERNALLY, DON'T USE OUT
        """
        for state in new_states:
            real_state = None
            for s in self._states:
                if s.Value == state.Value:
                    real_state = s
                    break
                pass
            for symbol in real_state.Transitions.keys():
                s0 = real_state.Transitions[symbol]
                if new_start.Value == s0.Value:
                    s0.add_transition(state,new_start)
                    pass
                else:
                    for s1 in new_states:
                        if s0.Value == s1.Value:
                            state.add_transition(symbol,s1)
                            break
                        pass
                    pass
                pass
            for symbol in real_state.EpsilonTransitions.keys():
                states = real_state.EpsilonTransitions[symbol]
                for s0 in states:
                    if s0.Value == new_start.Value:
                        state.add_epsilon_transition(symbol,new_start)
                        pass
                    else:
                        for s1 in new_states:
                            if s1.Value == s0.Value:
                                state.add_epsilon_transition(symbol,s1)
                                break
                            pass
                        pass
                    pass
                pass
            pass
        for state in new_states:
            for symbol in self._symbols:
                if not symbol in state.Transitions.keys() and not symbol in state.EpsilonTransitions.keys():
                    state.add_transition(symbol,new_final)
                    pass
                pass
            pass
        pass
    
    def _copy_transitions(self,state0,state1):
        for symbol in state1.Transitions.keys():
            state0.add_epsilon_transition(symbol,state1.Transitions[symbol])
            pass
        for symbol in state1.EpsilonTransitions.keys():
            for state in state1.EpsilonTransitions[symbol]:
                state0.add_epsilon_transition(symbol,state)
                pass
            pass
        pass
    
    def _copy_states(self,automaton,states,finals):
        """
        copy the states of an automaton to states
        """
        for state in automaton.States:
            if state == automaton.Start: continue
            exists = False
            for s in states:
                if s.Label == state.Label:
                    exists = True
                    break
                pass
            if not exists:
                isFinal = False
                for s in finals:
                    if s.Label == state.Label:
                        if s.Final and state.Final:
                            isFinal = True
                            pass
                        break
                    pass
                states.append(State(value=state.Value,label=state.Label,final=isFinal))
                pass
            pass
        pass
    
    def _copy_states_transitions(self,state_from,state_to,states):
        """
        copy all the transitions of 'state_from' to 'state_to' to the state of same label in 'states'
        """
        for symbol in state_from.Transitions.keys():
            state = state_from.Transitions[symbol]
            for s in states:
                if s.Label == state.Label:
                    state_to.add_epsilon_transition(symbol,s)
                    break
                pass
            pass
        for symbol in state_from.EpsilonTransitions.keys():
            for state in state_from.EpsilonTransitions[symbol]:
                for s in states:
                    if s.Label == state.Label:
                        state_to.add_epsilon_transition(symbol,s)
                        break
                    pass
                pass
            pass
        pass
    
    def __or__(self,other):
        """
        returns the automaton that recognizes the union bettwen other's language and self's language
        """
        if isinstance(other,Automaton):
            start = State()
            s0 = other.Start
            states = []
            self._copy_transitions(start,s0)
            self._copy_transitions(start,self._start)
            states += [state for state in other.States if not state == s0]
            states += [state for state in self._states if not state == self._start]
            return Automaton(start,*states)
        return True
    
    def __invert__(self):
        """
        returns the automaton that recognizes the complement language for this automaton
        WARNING! -> THE START'S STATES ARE IGNORED AND A COPY-VALUE IS USED INSTEAD, SO SOMES TRANSITIONS CAN BE LOST
        """
        new_start = State(value=self._start.Value,final=not self._start.Final)
        new_final = State(final=True,fault=True)
        new_states = []
        
        for state in self._states:
            if state == self._start: continue
            new_states.append(State(value=state.Value,final=not state.Final))
            pass
        
        self._make_start_transitions(new_start,new_states,new_final)
        self._make_states_transitions(new_start,new_states,new_final)
        
        new_states += [new_final]
        
        return Automaton(new_start,*new_states)
    
    def __and__(self,other):
        """
        returns the automaton that recognizes the intersection language bettwen this automaton language an the other automaton language
        NOTE: 2 states are equal if they have the same label
        WARNING! -> THE START'S STATES ARE IGNORED AND A COPY-VALUE IS USED INSTEAD, SO SOMES TRANSITIONS CAN BE LOST
        """
        if isinstance(other,Automaton):
            start = State()
            states = []
            
            self._copy_states(other,states,[s for s in self._states if s.Final])
            self._copy_states(self,states,[s for s in other.States if s.Final])                 
            
            for state in other.States:
                if not state == other.Start:
                    for s in states:
                        if s.Label == state.Label:
                            self._copy_states_transitions(state,s,states)
                            break
                        pass
                    pass
                else:
                    self._copy_states_transitions(state,start,states)
                    pass
                pass
            for state in self._states:
                if not state == self._start:
                    for s in states:
                        if s.Label == state.Label:
                            self._copy_states_transitions(state,s,states)
                            break
                        pass
                    pass
                else:
                    self._copy_states_transitions(state,start,states)
                    pass
                pass
            return Automaton(start,*states)
        return not other == None
    
    pass