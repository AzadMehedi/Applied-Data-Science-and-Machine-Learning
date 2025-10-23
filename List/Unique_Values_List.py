# Create a list with duplicates and show how to get unique values preserving order.

dup_list = [3,1,4,1,5,9,3,5]

def unique_preserve_order(lst):
    seen = set()
    out = []

    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

if __name__ == '__main__':
    print ('Original: ', dup_list)
    print('unique (Order preserved): ', unique_preserve_order(dup_list))
