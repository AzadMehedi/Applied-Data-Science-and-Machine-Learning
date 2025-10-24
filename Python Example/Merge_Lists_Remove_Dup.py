# Merge multiple lists preserving order and removing duplicates.

def merge_unique(*lists):
    seen = set()
    out = []
    for lst in lists:
        for x in lst:
            if x not in seen:
                seen.add(x)
                out.append(x)
    return out

if __name__ == '__main__':
    print(merge_unique([1,2,3],[3,4],[2,5]))