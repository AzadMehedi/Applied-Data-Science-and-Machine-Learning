# Count the frequency of elements using a dictionary.

words = ['apple', ' banana', 'apple', 'orange', 'banana', 'apple']

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

if __name__ == '__main__':
    print('Word Frequencies: ', freq)