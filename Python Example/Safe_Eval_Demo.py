# Demonstrate restricted eval using literal_eval.

from ast import literal_eval

expr = "[1,2,3]"
if __name__ == '__main__':
    print(literal_eval(expr))