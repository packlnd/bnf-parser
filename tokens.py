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
class TOKEN:
    def __init__(self): self.s = 'TOKEN'
    def __str__(self): return self.s
    def __repr__(self): return self.s
    def __unicode__(self): return self.s
class INDENT(TOKEN):
    def __init__(self): self.s = 'INDENT'
class DEDENT(TOKEN):
    def __init__(self): self.s = 'DEDENT'
class DEF(TOKEN):
    def __init__(self): self.s = 'DEF'
class MAIN(TOKEN):
    def __init__(self): self.s = 'MAIN'
class COLON(TOKEN):
    def __init__(self): self.s = 'COLON'
class PRINT(TOKEN):
    def __init__(self): self.s = 'PRINT'
class PLUS(TOKEN):
    def __init__(self): self.s = 'PLUS'
class INTLIT(TOKEN):
    def __init__(self, n): self.s = 'INT(%s)' % n
class BAD(TOKEN):
    def __init__(self): self.s = 'BAD'
