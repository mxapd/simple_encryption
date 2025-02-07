def encrypt(key, plaintext):
    keylen = len(key)
    content = []
    transposed = []
    cipher = ''

    # split the plaintext into chunks based on key length
    for i in range(0, len(plaintext), keylen):
        content.append(plaintext[i:i + keylen])

    # pad the last chunk if its length is less then key length
    for i in range(len(content)):
        if len(content[i]) < keylen:
            content[i] += 'Ɔ' * (keylen - len(content[i]))

    # create a list of original column indecies 
    preorder = []
    for x in range(keylen):
        preorder.append(x)

    # create a new list of reordered column indecies 
    sortedkey = sorted(enumerate(key), key=lambda x: x[1])
    postorder = []
    for x in sortedkey:
        postorder.append(x[0])

    # fill the transposed list with empty strings
    for _ in range(keylen):
        transposed.append('')

    # transpose the content based on the sorted key order
    for row in content:
        for index, char in zip(preorder, row):
            transposed[postorder[index]] += char

    # combine the transposed cols to create the ciphertext
    cipher = ''.join(transposed)

    return cipher


def decrypt(key, ciphertext):
    keylen = len(key)

    # sort the key and get thte original order of columns
    sortedkey = sorted(enumerate(key), key=lambda x: x[1])
    postorder = []
    for x in sortedkey:
        postorder.append(x[0])

    # calculate the number of rows based on the ciphertext length and key length
    rowcount = len(ciphertext) // keylen

    # split the ciphertext into columns
    transposed = []
    for i in range(keylen):
        start = i * rowcount
        end = start + rowcount
        transposed.append(ciphertext[start:end])

    # reorder columns to their original position
    reordered = []
    for col_index in postorder:
        reordered.append(transposed[col_index])

    # rebuild the plaintext by reading rowwise from the reordered cols 
    plaintext = ''
    for row in range(rowcount):
        row_text = ''
        for col in range(keylen):
            row_text += reordered[col][row]
        plaintext += row_text

    # remove padding chars
    plaintext = plaintext.replace('Ɔ', '')

    return plaintext
