def load_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = ''
            for line in file:
                if not line.startswith('*'):
                    content += line
            return content

    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')


def write_enc_file(filename, ciphertext):

    new_filename = filename.split('.')[0] + '_enc.txt'

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            header = ''
            for line in file:
                if line.startswith('*'):
                    header += line
                if not line.startswith('*'):
                    break

        with open(new_filename, 'w', encoding='utf-8') as file:
            file.write(header)
            file.write(ciphertext)
            file.write('\n'+'*'*99)


    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')


def write_denc_file(filename, plaintext):

    new_filename = filename.split('_')[0] + '_denc.txt'

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            header = ''
            for line in file:
                if line.startswith('*'):
                    header += line
                if not line.startswith('*'):
                    break

        with open(new_filename, 'w', encoding='utf-8') as file:
            file.write(header)
            file.write(plaintext)
            file.write('\n'+'*'*99)


    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')
