import util


def encrypt(key, plaintext):
    # check if the key is valid
    if not util.validate_caesar_key(key):
        return "Invalid key"

    ciphertext = ''
    # encrypt each character in the plaintext, exluding special chars
    for char in plaintext:
        if char in (' ', '\n', '\t', '\'', '\"'):
            ciphertext += char
            continue

        # shift each char by the key value
        new_char = chr((ord(char) + key) % 256)

        ciphertext += new_char

    return ciphertext


def decrypt(key, ciphertext):
    plaintext = ''

    for char in ciphertext:
        if char in (' ', '\n', '\t', '\'', '\"'):
            plaintext += char
            continue

        plainchar = chr((ord(char) - key) % 256)

        plaintext += plainchar

    return plaintext

