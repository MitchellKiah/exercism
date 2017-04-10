from re import match

def rotate(message, cipherKey):
    """
    input:
        message: string, message to be encoded
        cipherKey: int, key to encode message with
    return: string, encoded message
    """
    def shift(character):
        """
        input: string, single lowercase character
        return: string, shifted character
        """
        if ord(character)+cipherKey > ord('z'):
            return chr(ord('a')+(ord(character)+cipherKey) % ord('z') - 1)
        else:
            return chr(ord(character)+cipherKey)

    rotatedMessage = []
    for char in message:
        if not match('[a-zA-Z]', char):
            rotatedMessage.append(char)
        elif char.isupper():
            rotatedMessage.append(shift(char.lower()).upper())
        else:
            rotatedMessage.append(shift(char.lower()))
    return ''.join(rotatedMessage)
