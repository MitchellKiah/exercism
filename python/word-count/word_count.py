import re

def word_count(phrase):
    """
    input: string, phrase
    return: dict[string: int], occurance of each word in the phrase
    """
    wordList = re.findall('[a-z0-9]+', phrase.lower())
    wordCount = { word:wordList.count(word) for word in wordList }
    return wordCount
