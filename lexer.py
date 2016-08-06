from tokens import *

def _determine_indentation(line):
    return len(line) - len(line.lstrip())

def _is_digit(c):
    return c in '0123456789'

def tokenize(fn):
    #current_indentation = 0
    i_list = [0]
    token_list = []
    with open(fn, 'r') as f:
        lines = f.readlines()
    for line in lines:
        indentation = _determine_indentation(line)
        if indentation > i_list[0]:
            token_list.append(INDENT())
            i_list.insert(0, indentation)
        elif indentation < i_list[0]:
            token_list.append(DEDENT())
            i_list.insert(0, indentation)
        current_indentation = indentation
        line = line.strip()
        pos = -1
        while pos < len(line)-1:
            pos += 1
            if line[pos] == ':':
                token_list.append(COLON())
            elif line[pos] == '+':
                token_list.append(PLUS())
            elif line[pos] == 'd':
                if line[pos:pos+3] == 'def':
                    token_list.append(DEF())
                    pos += 2
            elif line[pos] == 'm':
                if line[pos:pos+4] == 'main':
                    token_list.append(MAIN())
                    pos += 3
            elif line[pos] == 'p':
                if line[pos:pos+5] == 'print':
                    token_list.append(PRINT())
                    pos += 4
            elif _is_digit(line[pos]):
                end_pos = pos+1
                while end_pos < len(line) and _is_digit(line[end_pos]):
                    end_pos += 1
                token_list.append(INTLIT(line[pos:end_pos]))
                pos = end_pos-1
            elif line[pos] == ' ':
                continue
            else:
                token_list.append(BAD())
    i_list.pop()
    for i in i_list:
       token_list.append(DEDENT())
    return token_list
