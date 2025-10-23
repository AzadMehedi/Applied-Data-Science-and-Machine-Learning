# Examples of list comprehensions: squares and filtered values.

squares = [x*x for x in range(10)]
even_times_two = [x*x for x in range(20) if x%2==0]


if __name__ == '__main__':
    print('Squares: ', squares)
    print('Even times two: ', even_times_two)