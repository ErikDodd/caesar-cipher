import string
import nltk
import ssl
import re

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


def decrypt(plaintext, key):
    pass


def crack(plaintext, key):
    pass


if __name__ == "__main__":
    word = "ZZZ"
    print(f"the word is: {word}")
    encrypted_word = encrypt(word, 1)
    print(f"the encrypted word is: {encrypted_word}")
    #new_word = "abc"
    # print(f"the word is: {new_word}")
    # encrypted_new_word = encrypt(new_word, 10)

