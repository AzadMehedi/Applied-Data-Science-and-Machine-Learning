# Use get() and setdefault() for safe key access.

user = {'name': 'Mehedi'}
age = user.get('age', 30)

user.setdefault('city', 'London')

if __name__ == '__main__':
    print('User dictionary: ', user)
    print('Age (default if missing): ', age)