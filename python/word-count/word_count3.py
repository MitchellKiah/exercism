import re

def word_count(phrase):
    """
    input: string, phrase
    return: dict[string: int], occurance of each word in the phrase
    """
    wordList = re.findall('[a-z0-9]+', phrase.lower())
    wordCount = {}
    for word in wordList:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1

    return wordCount
