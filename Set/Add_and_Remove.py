# Demonstrate how to add and remove elements in a set.

numbers = {1, 2, 3}
numbers.add(4)
numbers.discard(2)
numbers.update([5, 6])

if __name__ == '__main__':
    print("Updated set:", numbers)