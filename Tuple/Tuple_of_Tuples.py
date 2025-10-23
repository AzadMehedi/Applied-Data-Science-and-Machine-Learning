# Demonstrate how to work with a tuple of tuples.

records = (('id','name'), (1, 'Alice'), (2, 'Bob'), (3, 'Charlie'))

if __name__ == '__main__':
    headers = records[0]
    data = records[1:]
    print('Headers: ', headers)
    print('Data rows: ')
    for row in data:
        print(dict(zip(headers, row)))