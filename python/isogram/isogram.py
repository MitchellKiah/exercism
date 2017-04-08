def is_isogram(word):
    wordLow = word.lower()
    charCount = {}
    for char in wordLow:
        if char in 'abcdefghijklmnopqrstuvxyz':
            if char in charCount and charCount[char] > 0:
                return False
            else:
                charCount[char] = 1
    return True
