def global_routine(name):
    return (
        'global %s\n'
        '%s:\n' % (name, name)
    )

def routine(name):
    return '%s:\n'

def sys_call():
    return 'int 0x80\n'

def inst(INST, REG, VAL):
    return '%s %s, %s\n' % (INST, REG, VAL)
