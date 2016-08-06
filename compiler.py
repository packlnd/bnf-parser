import sys
import lexer
#import parser
#import code_generator

filename = sys.argv[1]
tokens = lexer.tokenize(filename)
print tokens
#goal = parser.parse(tokens)
#code_generator.generate(goal)
