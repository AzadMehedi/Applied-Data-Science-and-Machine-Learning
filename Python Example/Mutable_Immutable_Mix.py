# Show that tuples can contain lists (mutable inside immutable container).

t = (1, [2,3], 4)
t[1].append(5)

if __name__ == '__main__':
    print(t)