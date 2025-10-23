# Demonstrate tuple slicing and reversal.

data = tuple(range(10))

if __name__ == '__main__':
    print('Origianl tuple: ', data)
    print('Slice [2:8]: ', data[2:8])
    print('Reversed: ', data[::-1])