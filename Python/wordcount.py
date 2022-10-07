def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

string1 = str(input("enter the string")).lower()
number_of_words = len(string1.split())
print(number_of_words)
print(word_count(string1))

