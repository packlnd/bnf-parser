class Goal:
    def __init__(self, main):
        self.main = main

class MainMethod:
    def __init__(self, statements):
        self.statements = statements

class Statement: pass

class PrintStatement(Statement):
    def __init__(self, expr):
        self.expr = expr

class Expression: pass

class AddExpression(Expression):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

class IntExpression(Expression):
    def __init__(self, n):
        self.num = n

# TOKENS

class Indent: pass
class Dedent: pass

class DEF: pass
class MAIN: pass
class COLON: pass
class PRINT: pass
class PLUS: pass
