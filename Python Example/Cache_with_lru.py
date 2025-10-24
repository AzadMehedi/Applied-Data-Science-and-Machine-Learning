# Use functools.lru_cache to cache expensive calls.

from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n<2 : return n
    return fib(n-1)+fib(n-2)

if __name__ == '__main__':
    print('Fib(20): ', fib(20)) 