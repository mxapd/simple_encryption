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
        if char in (' ', '\n', '\t', '\"', '\''):
            plaintext += char
            continue

        plainchar = chr((ord(char) - key) % 255)

        plaintext += plainchar

    return plaintext


def validate_key(key):
    if isinstance(key, str) and len(key) == 1 and 0 <= ord(key) <= 255:
        return True
    elif isinstance(key, int) and 0 <= key < 256:
        return True
    else:
        print('Invalid key. Must be a number (0-255) or a single character.')
        return False
