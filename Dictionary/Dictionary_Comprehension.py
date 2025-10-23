# Demonstrate dictionary comprehensions.

squares = {x: x*x for x in range(6)}

if __name__ == '__main__':
    print('Squares dictionary: ', squares)