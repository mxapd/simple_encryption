def encrypt(key, plaintext):
    if not validate_key(key):
        return "Invalid key"

    ciphertext = ''
    for char in plaintext:
        if char in (' ', '\n', '\t'):
            ciphertext += char
            continue

        new_char = chr((ord(char) + key) % 256)

        ciphertext += new_char

    return ciphertext


def decrypt(key, ciphertext):
    plaintext = ''

    for char in ciphertext:
        if char in (' ', '\n', '\t'):
            plaintext += char
            continue

        plainchar = chr((ord(char) - key) % 256)

        plaintext += plainchar

    return plaintext
