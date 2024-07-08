from automaton import State,Automaton

def make_finit_values_automaton(*values):
    """
    returns the automaton that recognizes a finit set of strings
    """
    states = []
    for value in values:
        for i in range(len(value)):
            exists = False
            for state in states:
                if state.Value[0] == value[i] and state.Value[1] == i:
                    exists = True
                    break
                pass
            if not exists:
                states.append(State(value=(value[i],i),final=i==len(value)-1))
                pass
            pass
        pass
    for value in values:
        for i in range(len(value) - 1):
            for state in states:
                if state.Value[0] == value[i] and state.Value[1] == i:
                    added = False
                    for s in states:
                        if s.Value[0] == value[i + 1] and s.Value[1] == i + 1:
                            state.add_transition(value[i + 1],s)
                            added = True
                            break
                        pass
                    if added: break
                    pass
                pass
            pass
        pass
    start = State()
    for state in states:
        if state.Value[1] == 0:
            start.add_transition(state.Value[0],state)
            pass
        pass
    return Automaton(start,*states)