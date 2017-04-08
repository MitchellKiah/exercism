def hey(phrase):
    """
    input: str, phrase to say to Bob
    return: str, Bob's response
    """
    if type(phrase) != str:
        raise TypeError('Input phrase should be of type string')

    phrase = phrase.rstrip()
    if phrase == '':
        return 'Fine. Be that way!'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase[-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'
