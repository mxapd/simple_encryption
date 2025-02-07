def load_content(filename):
    try:
        # read the content (message and name) of the file, 
        # excluding header and footer frame 
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
    
    # read the header from the original file
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            header = ''
            for line in file:
                if line.startswith('*'):
                    header += line
                if not line.startswith('*'):
                    break

        # write the header, ciphertext and footer to a new file
        with open(new_filename, 'w', encoding='utf-8') as file:
            file.write(header)
            file.write(ciphertext)
            file.write('\n'+'*'*99)

        return new_filename

    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')


# same as above but writing plaintext instead of ciphertext
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

            return new_filename

    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')


# get a user input 
def get_user_input(promt, allowed):
    user_input = input(promt).strip().upper()

    while user_input not in allowed:
        print(f'Input not valid please input {allowed}')
        user_input = input(promt).strip().upper()

    return user_input


# keeps asking for a valid key until one is given, using validate key method to check for validity
def get_valid_caesar_key():
    while True:
        key = input('Enter key: (0-255)')
        try:
            key = int(key)
            if validate_caesar_key(key):
                return key
        except ValueError:
            print('Invalid key. Must be a number between 0-255.')


# checks that the key given for the ceasar cipher is valid 
def validate_caesar_key(key):
    if isinstance(key, str) and len(key) == 1 and 0 <= ord(key) <= 255:
        return True
    elif isinstance(key, int) and 0 <= key < 256:
        return True
    else:
        print('Invalid key. Must be a number (0-255).')
        return False
