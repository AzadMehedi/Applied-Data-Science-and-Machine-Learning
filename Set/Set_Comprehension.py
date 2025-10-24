# Demonstrate creating sets using comprehensions.

squares = {x*x for x in range(6)}

if __name__ == '__main__':
    print('Squares set: ', squares)