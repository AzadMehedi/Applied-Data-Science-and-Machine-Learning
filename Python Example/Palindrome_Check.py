# Check if a string is palindrome ignoring spaces and case.

def is_pal(s):
    s2 = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s2 == s2[::-1]

if __name__ == '__main__':
    print(is_pal("A man a plan a canal Panama"))