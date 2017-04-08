import re

def hey(phrase):
    """
    input: str, phrase to say to Bob
    return: str, Bob's response
    """
    if type(phrase) != str:
        raise TypeError('Input phrase should be of type string')
    elif re.findall('\S', phrase) == []:
        return 'Fine. Be that way!'
    elif not re.search('[a-z]', phrase) and re.search('[A-Z]', phrase):
        return 'Whoa, chill out!'
    elif re.sub('\s', '', phrase)[-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'
