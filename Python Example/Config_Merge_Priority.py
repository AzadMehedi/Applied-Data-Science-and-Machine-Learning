# Merge configuration dicts with priority: higher overrides lower.

def merge_configs(*configs):
    res = {}
    for cfg in configs:
        res.update(cfg)
    return res

if __name__ == '__main__':
    print(merge_configs({'a':1, 'b':2}, {'b':3}, {'c':4}))