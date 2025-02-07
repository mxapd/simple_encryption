def encrypt(key, plaintext):
    keylen = len(key)
    content = []
    transposed = []
    cipher = ''

    for i in range(0, len(plaintext), keylen):
        content.append(plaintext[i:i + keylen])

    for i in range(len(content)):
        if len(content[i]) < keylen:
            content[i] += 'Ɔ' * (keylen - len(content[i]))

    preorder = []

    for x in range(keylen):
        preorder.append(x)

    sortedkey = sorted(enumerate(key), key=lambda x: x[1])

    postorder = []

    for x in sortedkey:
        postorder.append(x[0])

    for _ in range(keylen):
        transposed.append('')

    for row in content:
        for index, char in zip(preorder, row):
            transposed[postorder[index]] += char

    cipher = ''.join(transposed)

    return cipher


def decrypt(key, ciphertext):
    keylen = len(key)

    sortedkey = sorted(enumerate(key), key=lambda x: x[1])

    postorder = []

    for x in sortedkey:
        postorder.append(x[0])

    rowcount = len(ciphertext) // keylen

    transposed = []

    for i in range(keylen):
        start = i * rowcount
        end = start + rowcount
        transposed.append(ciphertext[start:end])

    reordered = []

    for col_index in postorder:
        reordered.append(transposed[col_index])

    plaintext = ""
    for row in range(rowcount):
        row_text = ""
        for col in range(keylen):
            row_text += reordered[col][row]
        plaintext += row_text

    plaintext = plaintext.replace('Ɔ', '')

    return plaintext
