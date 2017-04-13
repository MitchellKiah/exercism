def detect_anagrams(word, candidates):
    """
    input(word): string, word to check anagrams against
    input(candidates): list, possible anagrams of word
    return: list, candidate words that are anagrams of word
    """
    anagrams = []
    for item in candidates:
        if len(item) == len(word) and item.lower() != word.lower():
            if sorted(word.lower()) == sorted(item.lower()):
                anagrams.append(item)
    return anagrams

# print(detect_anagrams('listen', ["enlists", "google", "inlets", "banana"]))
