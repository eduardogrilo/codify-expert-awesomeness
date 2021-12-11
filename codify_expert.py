def codify (normal_text,key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    encrypted_text = ''
    for char in normal_text:
        index = alphabet.find(char)
        encrypted_text = encrypted_text + key[index]
    return encrypted_text
