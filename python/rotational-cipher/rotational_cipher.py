from string import ascii_lowercase as lowercase
def rotate(message, key):
    """
    input:
        message: string, message to be encoded
        key: int, key to encode message with
    return: string, encoded message
    """
    def shift(character):
        return lowercase[(lowercase.find(char.lower())+key) % 26]
    rotated = []
    for char in message:
        if not char.isalpha():
            rotated.append(char)
        elif char.isupper():
            rotated.append(shift(char).upper())
        else:
            rotated.append(shift(char))
    return ''.join(rotated)
