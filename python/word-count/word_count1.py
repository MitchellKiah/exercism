import string

def word_count(phrase):
    """
    input: string, phrase
    return: dict[string: int], occurance of each word in the phrase
    """
    wordCount = {}
    word = []
    for char in phrase.lower():
        if char in string.ascii_lowercase or char in string.digits:
            word.append(char)
        else:
            word.append(' ')
    for word in ''.join(word).split():
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
    return wordCount
