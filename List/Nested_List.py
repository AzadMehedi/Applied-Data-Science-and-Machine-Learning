# A nested list and a small recursive pretty-printer.

nested_list = [1, [2, [3,4], 5], ['a', ['b','c']]]

def flatten(lst):
    out = []
    for item in lst:
        if isinstance(item, list):       # চেক করে যে, item নামের ভেরিয়েবলটা list টাইপের কিনা 
            out.extend(flatten(item))
        else:
            out.append(item)
    return out

if __name__ == '__main__':
    print('Nested: ', nested_list)
    print('Flattened: ', flatten(nested_list))
