import pretty_printer

import sys
import lexer
import parser
#import code_generator
#import interpreter

filename = sys.argv[1]
tokens = lexer.tokenize(filename)
#print tokens
goal = parser.parse(tokens)
pretty_printer.pretty_print(goal)
#code_generator.generate(goal)
#interpreter.execute(goal)
