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
    for l in range(len(lines)):
        line = lines[l]
        indentation = _determine_indentation(line)
        if indentation > i_list[0]:
            token_list.append(INDENT(l, 0))
            i_list.insert(0, indentation)
        elif indentation < i_list[0]:
            token_list.append(DEDENT(l, 0))
            i_list.insert(0, indentation)
        current_indentation = indentation
        line = line.strip()
        pos = -1
        while pos < len(line)-1:
            pos += 1
            if line[pos] == ':':
                token_list.append(COLON(l, pos))
            elif line[pos] == '+':
                token_list.append(PLUS(l, pos))
            elif line[pos] == 'f':
                if line[pos:pos+4] == 'func':
                    token_list.append(FUNC(l, pos))
                    pos += 3
            elif line[pos] == 'm':
                if line[pos:pos+4] == 'main':
                    token_list.append(MAIN(l, pos))
                    pos += 3
            elif line[pos] == 'p':
                if line[pos:pos+5] == 'print':
                    token_list.append(PRINT(l, pos))
                    pos += 4
            elif _is_digit(line[pos]):
                end_pos = pos+1
                while end_pos < len(line) and _is_digit(line[end_pos]):
                    end_pos += 1
                token_list.append(INTLIT(line[pos:end_pos], l, pos))
                pos = end_pos-1
            elif line[pos] == ' ':
                continue
            else:
                token_list.append(BAD(l, pos))
    i_list.pop()
    for i in i_list:
       token_list.append(DEDENT())
    return token_list
