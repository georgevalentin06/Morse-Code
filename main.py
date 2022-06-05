MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-' }

# word = input("Write your phrase:\n")
# encryption = ""
# for letter in word:
#     if letter == " ":
#         encryption += " "
#     else:
#         encryption += MORSE_CODE_DICT[letter.upper()]
#
# print(encryption)

def encrypt(message):
    encryption = ""
    for letter in message:
        if letter == " ":
            encryption += "  "
        else:
            encryption += MORSE_CODE_DICT[letter.upper()]
    return encryption
print(encrypt("Morse-Code"))

def decrypt(message):
    decrypt_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    decryption = ""
    message = message.split(" ")
    for letter in message:
        if letter in decrypt_dict:
            decryption += decrypt_dict.get(letter)
    return decryption.lower()
print(decrypt("-- --- .-. ... . -....- -.-. --- -.. ."))




