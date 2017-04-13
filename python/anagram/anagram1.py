def detect_anagrams(word, candidates):
    """
    """
    def is_anagram(letterDict, candidate):
        for char in candidate.lower():
            if (char in letterDict) and (letterDict[char] > 0):
                letterDict[char] -= 1
            else:
                return False
        return True

    letters = {}
    for char in word.lower():
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    anagrams = []
    for item in candidates:
        if len(item) == len(word) and item.lower() != word.lower():
            if is_anagram(dict(letters), item):
                anagrams.append(item)


    return anagrams

# print(detect_anagrams('listen', ["enlists", "google", "inlets", "banana"]))
