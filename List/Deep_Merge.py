# Merge lists of dictionaries by concatenating list-values and updating scalars.

list_a = [{"id":1, "tags":["a","b"], "count":2}, {"id":2, "tags":["c"], "count":1}]
list_b = [{"id":1, "tags":["d"], "count":3}, {"id":3, "tags":["e"], "count":4}]

def deep_merge_by_id(a,b):
    merged = {}

    for d in a+b:
        _id = d.get('id')
        if _id not in merged:
            merged[_id] = {**d}
            # ensure text exist
            merged[_id].setdefault('tags', list(merged[_id].get('tags',[])))
        else:
            # merge tags
            merged[_id]['tags'] = merged[_id].get('tags', []) + d.get('tags', [])
            # sum counts if present
            if 'count' in d or 'count' in merged[_id]:
                merged[_id]['count'] = merged[_id].get('count', 0) + d.get('count', 0)
    return list(merged.values())


if __name__ == '__main__':
    print('List A: ', list_a)
    print('List B: ', list_b)
    print('Merged: ', deep_merge_by_id(list_a, list_b))


# এই কোডটা দুইটা dictionary-এর list (list_a এবং list_b) কে তাদের id অনুযায়ী একত্র (merge) করছে।
# একই id থাকলে তাদের tags লিস্টগুলো জোড়া লাগিয়ে (concatenate) দিচ্ছে।
# একই id থাকলে তাদের count মান যোগ (sum) করছে।
# # যাদের id আলাদা, তারা আলাদা রেকর্ড হিসেবে থেকে যাচ্ছে।

# id=1 এর ক্ষেত্রে tags = ['a','b','d'] এবং count = 2+3 = 5
# id=2 ও id=3 আলাদা এন্ট্রি হিসেবে রয়ে গেছে।
