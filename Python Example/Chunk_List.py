# Split a list into chunks of size n.

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

if __name__ == '__main__':
    print(list(chunks(list(range(10)), 3)))