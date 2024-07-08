"""
recognizers

here is defined a basic set of recognizers for tokens in a given language
"""

from string import ascii_letters,digits,punctuation,whitespace
from lexer.automaton_builder import make_finit_values_automaton
from lexer.loader import GetConfig,set_config_file_name
from automaton import *

Configuration = GetConfig()
EXTRAS = ['_']

def make_variable_automaton(extras,*reserveds):
    """
    returns an automaton that recognizes all the valid names for a variable
    
    extras -> string with the extra characters acepted in a variable name
    reserveds -> values that are reserved for the language (keywords,constants,built-in,etc)
    """
    start = State()
    finals = []
    extra = ''
    for e in extras:
        extra += e
        pass
    for char in ascii_letters + digits + extra:
        state = State(value=char,final=True)
        start.add_transition(char,state)
        finals.append(state)
        pass
    for state in finals:
        for char in ascii_letters + digits + extra:
            for s in finals:
                if s.Label == char:
                    state.add_transition(char,s)
                    break
                pass
            pass
        pass
    return Automaton(start,*finals)

def make_numeric_automaton():
    """
    returns an automaton that recognizes numeric strings representations
    """
    start = State()
    finals_0 = [State(value=(int(digit),'before'),final=True) for digit in digits]
    finals_1 = [State(value=(int(digit),'after'),final=True) for digit in digits]
    point = State(value='.')
    floating = State(value='e')
    plus = State(value='+')
    minus = State(value='-')
    not_finals = [point,floating,plus,minus]
    states = finals_0 + finals_1 + not_finals
    
    for state in finals_0 + [start]:
        for digit in digits:
            for s in finals_0:
                if s.Value[0] == int(digit):
                    state.add_transition(digit,s)
                    break
                pass
            pass
        if state == start: continue
        state.add_transitions(**{'.':point,'e':floating})
        pass
    
    for state in finals_1:
        for digit in digits:
            for s in finals_1:
                if s.Value[0] == int(digit):
                    state.add_transition(digit,s)
                    break
                pass
            pass
        pass
    
    for state in not_finals:
        if not state.Label == 'e':
            for digit in digits:
                for s in finals_1:
                    if s.Value[0] == int(digit):
                        state.add_transition(digit,s)
                        break
                    pass
                pass
            pass
        else:
            state.add_transitions(**{'+':plus,'-':minus})
            pass
        pass
    return Automaton(start,*states) | make_finit_values_automaton('e','PI')

def make_string_automaton():
    
    start = State()
    state2 = State(value='"')
    state_reading = State(value='all')
    final = State(value='final',final=True)
    start.add_transition('"',state2)
    for symbol in ascii_letters + digits + punctuation.replace('"','') + whitespace:
        state2.add_transition(symbol,state_reading)
        state_reading.add_transition(symbol,state_reading)
        pass
    state_reading.add_transition('"',final)
    return Automaton(start,state2,state_reading,final)

KeywordRecognizer = make_finit_values_automaton(*Configuration.keywords)
OperatorRecognizer = make_finit_values_automaton(*Configuration.operators)
SymbolRecognizer = make_finit_values_automaton(*Configuration.symbols)
BooleanRecognizer = make_finit_values_automaton('true','false')
VariableRecognizer = make_variable_automaton(EXTRAS,*Configuration.keywords)
NumericRecognizer = make_numeric_automaton()
StringRecognizer = make_string_automaton()