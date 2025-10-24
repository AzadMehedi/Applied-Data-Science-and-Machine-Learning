# Use generator expressions to save memory.

def gen_squares(n):
    return (i*i for i in range(n))

if __name__ == '__main__':
    g = gen_squares(10)
    print("First three:", [next(g) for _ in range(3)])
    print("Remaining sum:", sum(g))