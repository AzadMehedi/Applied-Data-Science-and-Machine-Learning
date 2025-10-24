# Show join, split, and chained transformations.

words = ["  hello", "world  ", "  from", "python "]
clean = [w.strip().upper() for w in words]
sentence = " ".join(clean)

if __name__ == '__main__':
    print("Clean list:", clean)
    print("Sentence:", sentence)
    print("Words back:", sentence.split())