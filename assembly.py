INSTR_MOV = 'mov'
INSTR_SUB = 'add'
INSTR_SUB = 'sub'

# TODO: http://www.fabiensanglard.net/macosxassembly/index.php

def write_asm_file(content, fname):
    with open(fname + '.asm', 'r') as f:
        f.write(content)

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
