# Demonstrate pop with default.

d = {"a":1, "b":2}
x = d.pop("c", None)

if __name__ == '__main__':
    print("Popped c:", x)
    print("Remaining:", d)