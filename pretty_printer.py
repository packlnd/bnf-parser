from __future__ import print_function
from tokens import *

def pretty_print(goal):
    indent=0
    print_goal(goal)

def print_goal(goal):
    print_main(goal.main)

def print_main(main):
    print('Main: [')
    for s in main.statements:
        print_statement(s, 4)
    print(']')

def print_statement(stmt, indent):
    if isinstance(stmt, PrintStatement):
        print_print_stmt(stmt, indent)

def print_print_stmt(stmt, indent):
    print('%sPrint: ' % (' '*indent), end='')
    print_expr(stmt.expr, 0)

def print_expr(expr, indent):
    if isinstance(expr, AddExpression):
        print_add_expr(expr)
    else:
        print_int_expr(expr)

def print_add_expr(expr):
    print(expr.lhs, end='')
    print('+',end='')
    print(expr.rhs)

def print_int_expr(expr):
    print(expr.num)
