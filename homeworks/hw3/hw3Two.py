
import string

ALPHABET_SIZE = 26
FREQUENCY_E = .12702
MAX_LINE = 80

def decrypt(rotation, encrypted_string):
    
    new_string = ''

    for char in encrypted_string:
        ascii = ord(char)

        if ascii <= ord('Z') and ascii >= ord('A'):
            ascii += rotation
            if ascii > ord('Z'):
               ascii -= ALPHABET_SIZE

            new_string += chr(ascii)

        else:
            new_string += char

    return new_string

def rotation(encrypted_string):
    
    counter = 0

    for char in encrypted_string:
        ascii = ord(char)
        if ascii <= ord('Z') and ascii >= ord('A'):
            counter += 1

    for rotation in range(ALPHABET_SIZE + 1):
        new_string = decrypt(rotation, encrypted_string)

        e_counter = string.count(new_string, 'E')

        freq = float(e_counter) / counter

        if freq >= FREQUENCY_E:
            return rotation

    print "Encryption not english"

def output(decryption):
    
    print
    print
    print "Decryption"
    print

    split_string = string.split(decryption, ' ')
    line_length = 0

    for word in split_string:
        word_length = len(word)
        if line_length + len(word) < MAX_LINE:
            print word,
            line_length += word_length +1
        else:
            print
            line_length = 0

def main():
    
    user_string = raw_input("")
    string_caps = user_string.upper()

    print "The Text to decrypt"
    print
    print string_caps,
    
    shift = rotation(string_caps)
    decryption = decrypt(shift, string_caps)
    output(decryption)
    
main()
