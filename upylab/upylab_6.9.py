def belongs_to_file(word, filename):
    with open(filename) as f:
        l = f.readlines()
        for w in l:
            if w.strip() == word:
                return True
    return False


print(belongs_to_file("renard", "words.txt"))
print(belongs_to_file("abbots", "words.txt"))
