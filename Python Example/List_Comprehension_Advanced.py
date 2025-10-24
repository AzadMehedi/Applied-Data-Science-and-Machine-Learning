# Create a list of squared even numbers and filter with a function.

def is_even(n):
    return n % 2 == 0

squares_even = [x*x for x in range(20) if is_even(x)]

if __name__ == '__main__':
    print("Even squares:", squares_even)
    print("Count:", len(squares_even))