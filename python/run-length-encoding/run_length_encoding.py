import re

def decode(encodedStr):
    """
    Decodes run-length encoded string.
    input: str, run length encoded string.
    return: str, decoded version of input string.
    """
    decoded = []
    # Regex below breaks encoded string into tuples of
    # count per character such as ('12', 'W') and ('', 'B')
    for count, char in re.findall('(\d*)(\D)', encodedStr):
        decoded.append(int(count)*char if count != '' else char)
    return ''.join(decoded)

def encode(strToEncode):
    """
    Encodes input using run-length encoding.
    input: str, Must contain only a-z or A-Z and white space
    return: str, run-length encoded version of input string.
    """
    def run_length(count, char):
        return str(count)+char if count > 1 else char

    prevChar = ''
    charCount = 1
    encoded = []
    for index, char in enumerate(strToEncode):
        if index == 0:
            prevChar = char
        elif char == prevChar:
            charCount += 1
        else:
            encoded.append(run_length(charCount, prevChar))
            prevChar = char
            charCount = 1
    encoded.append(run_length(charCount, prevChar))
    return ''.join(encoded)
