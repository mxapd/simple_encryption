import caesar
import util
import columnar

def main():

    filename = input('Name of file to read from: ')
    message = util.load_content(filename)

    user_choice_e_d = input('Do you want to encrypt [E] or decrypt [D]?')
    user_choice_s_t = input('Do you want to use substitution [S] or transposition [T]?')

    if user_choice_s_t == 'S':
        while True:
            key = int(input('Input key (0-255): '))
            if caesar.validate_key(key):
                break

        if user_choice_e_d == 'E':
            ciphertext = caesar.encrypt(key, message)
            util.write_enc_file(filename, ciphertext)

        elif user_choice_e_d == 'D':
            plaintext = caesar.decrypt(key, message)
            util.write_denc_file(filename, plaintext)

    elif user_choice_s_t == 'T':
        while True:
            key = input('Input key :')
            break

        if user_choice_e_d == 'E':
            ciphertext = columnar.encrypt(key, message)
            util.write_enc_file(filename, ciphertext)

        elif user_choice_e_d == 'D':
            plaintext = columnar.decrypt(key, message)
            util.write_denc_file(filename, plaintext)


main()
