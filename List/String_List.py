# A list of strings and a function that joins them.

string_list = ['apple','banana','cherry','date']

def join_with_comma(lst):
    return ', '.join(lst)

if __name__ == '__main__':
    print('Joined: ', join_with_comma(string_list))
    

