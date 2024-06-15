def plus(token_list):
    pass

def minus(token_list):
    pass

def multiplier(token_list):
    pass

def divition(token_list):
    pass

def var(token_list):
    pass

def brackets(token_list):
    return [("expression",token_list[1])]

def replacement(token_list):
    return [( "replacement" , token_list[0])]