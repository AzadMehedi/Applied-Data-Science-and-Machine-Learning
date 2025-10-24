# Use a set to remove duplicates from a list.

data = [1,2,2,3,4,4,5]
unique = set(data)

if __name__ == '__main__':
    print('Original list: ', data)
    print('Unique values: ', unique)