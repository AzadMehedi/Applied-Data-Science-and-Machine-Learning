# Show try/except and cleaning up with finally.

def safe_div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
    finally:
        pass

if __name__ == '__main__':
    print("10/2:", safe_div(10,2))
    print("10/0:", safe_div(10,0))