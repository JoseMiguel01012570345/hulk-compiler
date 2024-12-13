"""
a module to work with automatons

Here's defined all the features to work with automatons

Examples:
    State definition: 
        A = State(value=(0,1))
        C = State(value=2,final=True)
        A0 = State(value='01')
        C0 = State(value='2',final=True)
    
    Adding transitions:
        A0.add_transition('0',A0)
        A0.add_transition('1',A0)
        A0.add_transition('2',C0)
        C0.add_transition('0',A0)
        C0.add_transition('1',A0)
        C0.add_transition('2',C0)
        
        A.add_transition(0,A)
        A.add_transition(1,A)
        A.add_transition(2,C)
        C.add_transition(0,A)
        C.add_transition(1,A)
        C.add_transition(2,C)

    Automaton definitions:
        automaton = Automaton(A,C)
        automaton0 = Automaton(A0,C0)
        
    Recognizing strings:
        string1 = '01012'
        string2 = [0,1,0,2]
        print(automaton.recognize(string1)) # prints False
        print(automaton.recognize(string2)) # prints True
        print(automaton0.recognize(string1)) # prints True
        print(automaton0.recognize(string2)) # prints False
        
    Automatons can be componed
    
    Componing automatons:
        Aut = automaton | automaton0 # returns a new automaton that recognizes the strings from automaton's language or automaton0's language

        print(Aut.recognize(string1)) # prints True
        print(Aut.recognize(string2)) # prints True
"""

from . import automaton_definition
State,Automaton = automaton_definition.State , automaton_definition.Automaton