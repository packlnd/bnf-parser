from tokens import *

def execute(goal):
    interpret_goal(goal)

def interpret_goal(goal):
    interpret_main(goal.main)

def interpret_main(main):
    for stmt in main.statements:
        interpret_stmt(stmt)

def interpret_stmt(stmt):
    if isinstance(stmt, PrintStatement):
        interpret_print(stmt)

def interpret_print(stmt):
    if isinstance(stmt.expr, AddExpression):
        res = interpret_add(stmt.expr)
    else:
        res = interpret_int(stmt.expr)
    print res

def interpret_add(expr):
    return expr.lhs + expr.rhs

def interpret_int(expr):
    return expr.num
