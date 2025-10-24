# Simple recursive factorial with guard.

def fact(n):
    if n<=1:
        return 1
    return n*fact((n-1))

if __name__ == '__main__':
    print('5! : ', fact(5))