# Use contextlib to create a simple context manager.

from contextlib import contextmanager

@contextmanager
def simple_cm():
    print('Enter')
    try:
        yield
    finally:
        print('Exit')

if __name__ == '__main__':
    with simple_cm():
        print('Inside')



# print('Enter') → যখন with ব্লকে ঢোকা হয়, তখন এই লাইন চলে।
# yield → এখানে নিয়ন্ত্রণ সাময়িকভাবে with ব্লকের ভেতরে চলে যায়।
# finally ব্লক → যখন with ব্লক থেকে বের হয় (যেভাবেই বের হোক, এমনকি error হলেও), তখন এটি চলে এবং print('Exit') করে।