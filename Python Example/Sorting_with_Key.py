# Sort words by length then alphabetically.

words = ["banana","fig","apple","cherry"]
sorted_words = sorted(words, key=lambda w: (len(w), w))

if __name__ == '__main__':
    print(sorted_words)
    