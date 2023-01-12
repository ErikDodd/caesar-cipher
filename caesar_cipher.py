import string
import nltk
import ssl
from collections import Counter

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()


def encrypt(plaintext, key):

    ciphertext = ""

    for char in range(len(plaintext)):
        char = plaintext[char]
        #print(chr(ord(char) + 1))
        if char.islower():
            shift_char = chr((ord(char) + key - 97) % 26 + 97)
            ciphertext += shift_char
        if char.isupper():
            shift_char = chr((ord(char) + key - 65) % 26 + 65)
            ciphertext += shift_char
    return ciphertext


def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)


def crack(ciphertext):
    pass



if __name__ == "__main__":
    # word = "pizza"
    # print(f"the word is: {word}")
    # encrypted_word = encrypt(word, 1)
    # print(f"the encrypted word is: {encrypted_word}")
    # decrypted_word = decrypt(encrypted_word, 1)
    # print(f"the decrypted word is: {decrypted_word}")
    ciphertext = "qjaab"
    decrypted_message = crack(ciphertext)
    print("Decrypted message:", decrypted_message)

