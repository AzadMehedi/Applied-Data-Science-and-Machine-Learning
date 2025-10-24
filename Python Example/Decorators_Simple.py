# Simple decorator that logs function calls.

def log_calls(fn):
    def wrapper(*args, **kwargs):
        print(f'Calling {fn.__name__}')
        return fn(*args, **kwargs)
    return wrapper

@log_calls
def greet(name):
    return f'Hello {name}'

if __name__ == '__main__':
    print(greet('World'))