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
class TOKEN(object):
    _id = 0
    def __init__(self, **kwargs):
        TOKEN._id += 1
        self.token_id = TOKEN._id
        self.s = name

    def __repr__(self):
        return '%s_%s' % (
            self.s,
            self.token_id
        )

class INDENT(TOKEN):
    def __init__(self):
        super(INDENT, self).__init__('INDENT')
class DEDENT(TOKEN):
    def __init__(self):
        super(DEDENT, self).__init__('DEDENT')
class FUNC(TOKEN):
    def __init__(self):
        super(FUNC, self).__init__('FUNC')
class MAIN(TOKEN):
    def __init__(self):
        super(MAIN, self).__init__('MAIN')
class COLON(TOKEN):
    def __init__(self):
        super(COLON, self).__init__('COLON')
class PRINT(TOKEN):
    def __init__(self):
        super(PRINT, self).__init__('PRINT')
class PLUS(TOKEN):
    def __init__(self):
        super(PLUS, self).__init__('PLUS')
class INTLIT(TOKEN):
    def __init__(self, **kwargs):
        super(INTLIT, self).__init__(name='INT(%s)' % n, **kwargs)
        self.n = int(n)
class BAD(TOKEN):
    def __init__(self, **kwargs):
        super(BAD, self).__init__(name='BAD', **kwargs)
