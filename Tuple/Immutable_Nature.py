# Demonstrate that tuples are immutable.

values = (1,2,3)

try:
    values[0] == 99
except TypeError as e:
    print('Error: ', e)

print('Tuples can not be changed after creation')