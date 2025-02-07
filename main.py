import caesar
import util
import columnar

# get the filename and load the contents of that file
filename = input('Name of file to read from: ')
message = util.load_content(filename)

# get user input for mode and what cipher to use
mode = util.get_user_input('Do you want to encrypt [E] or decrypt [D]?', ('E', 'D'))
cipher = util.get_user_input(
    'Do you want to use substitution [S] or transposition [T]? ', ('S', 'T'))

# if the chosen cipher is substitution get a valid key and encrypt or decrypt based on mode input
if cipher == 'S':
    key = util.get_valid_caesar_key()
    result = caesar.encrypt(key, message) if mode == 'E' else caesar.decrypt(key, message)
else:
    key = input('Enter key: ')
    result = columnar.encrypt(key, message) if mode == 'E' else columnar.decrypt(key, message)


new_filename = filename

# then write to file
if mode == 'E':
    new_filename = util.write_enc_file(filename, result)
else:
    new_filename = util.write_denc_file(filename, result)

print(f'The file {new_filename} was written successfully')
