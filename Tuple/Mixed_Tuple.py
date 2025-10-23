# A tuple with mixed data types.

mixed = (1, 'hello', 3.14, False, None)

if __name__ == '__main__':
    for item in mixed:
        print(f'{item!r} id of type {type(item).__name__}')