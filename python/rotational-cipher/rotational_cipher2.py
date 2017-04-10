def rotate(message, key):
    """
    input:
        message: string, message to be encoded
        key: int, key to encode message with
    return: string, encoded message
    """
    def shift(character):
        return chr(((ord(char.lower()) - ord('a') + key) % 26) + ord('a'))

    rotated = []
    for char in message:
        if not char.isalpha():
            rotated.append(char)
        elif char.isupper():
            rotated.append(shift(char).upper())
        else:
            rotated.append(shift(char))
    return ''.join(rotated)
