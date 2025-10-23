# Demonstrate common slicing operations.

seq = list(range(10))

if __name__ == '__main__':
    print('Original: ', seq)
    print('First 3: ', seq[:3])
    print('Last 3: ', seq[-3:])
    print('Every 2nd: ', seq[::2])
    print('Reversed: ', seq[::-1])
