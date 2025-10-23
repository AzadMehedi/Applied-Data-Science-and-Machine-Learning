# Utility to flatten arbitrarily nested lists (handles tuples too).

def flatten_iterable(it):
    out = []
    for x in it:
        if isinstance(x, (list, tuple)):
            out.extend(flatten_iterable(x))
        else:
            out.append(x)
    return out
example = [1, (2,3), [4, [5,6],(7,)], 8]

if __name__ == '__main__':
    print('Example: ', example)
    print('Flattened: ', flatten_iterable(example))

# এই কোডটা একটি nested list বা tuple  কে একদম flat list এ পরিণত করে।
# অর্থাৎ, ভিতরের সব লিস্ট বা টাপল খুলে একটার পর একটা এলিমেন্ট হিসেবে সাজিয়ে দেয়।