from tokens import *

def _eat(lst, t):
    if isinstance(lst[0], t):
        lst.pop(0)
    else:
        raise Exception

def parse(token_list):
    goal = parse_goal(token_list)
    assert not token_list
    return goal

def parse_goal(token_list):
    return Goal(parse_main(token_list))

def parse_main(token_list):
    _eat(token_list, DEF)
    _eat(token_list, MAIN)
    _eat(token_list, COLON)
    _eat(token_list, INDENT)
    stmts = []
    while not isinstance(token_list[0], DEDENT):
        stmts.append(parse_statement(token_list))
    _eat(token_list, DEDENT)
    return MainMethod(stmts)

def parse_statement(token_list):
    if isinstance(token_list[0], PRINT):
        return parse_print_statement(token_list)

def parse_print_statement(token_list):
    _eat(token_list, PRINT)
    return PrintStatement(parse_expression(token_list))

def parse_expression(token_list):
    n = parse_int(token_list)
    if isinstance(token_list[0], PLUS):
        _eat(token_list, PLUS)
        return AddExpression(n, parse_int(token_list))
    return IntExpression(n)

def parse_int(token_list):
    n = token_list[0].n
    _eat(token_list, INTLIT)
    return n
