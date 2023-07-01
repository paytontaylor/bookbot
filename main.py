def readFile(path):
    with open(path) as f:
        return f.read()


def getWordCount(text):
    return len(text.split())


def countCharacters(text):
    char_count = {}
    words = text.split()
    for word in words:
        for char in word:
            if char.lower() in char_count.keys():
                char_count[char.lower()] += 1
            else:
                char_count[char.lower()] = 1
    return char_count


def getSortedAlphChars(char_count):
    sorted_chars = []
    for char in char_count.keys():
        if char.isalpha():
            sorted_chars.append(char)
    sorted_chars.sort()
    return sorted_chars


def getAlphCharsCounts(sorted_chars, char_count):
    count = []
    for char in sorted_chars:
        if char in char_count.keys():
            count.append(char_count[char])
    return count


def printReport(text, chars, char_counts):
    word_count = getWordCount(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print(" ")
    for i in range(len(chars)):
        print(f"The '{chars[i]} character was found {char_counts[i]} times'")
    print("---End Report---")


text = readFile("./books/frankenstein.txt")
char_counts = countCharacters(text)
sorted_chars = getSortedAlphChars(char_counts)
sorted_chars_count = getAlphCharsCounts(sorted_chars, char_counts)
printReport(text, sorted_chars, sorted_chars_count)
