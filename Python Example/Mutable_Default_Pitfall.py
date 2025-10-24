# Demonstrate avoiding mutable defaults.

def append_to(values, lst=None):
    if lst is None:
        lst = []
    lst.append(values)
    return lst

if __name__ == '__main__':
    print(append_to(1))
    print(append_to(2))