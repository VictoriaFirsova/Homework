"""Task 4.3. Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
Repeats of letters in the word are removed, then the cipher alphabet is generated
with the keyword matching to A, B, C etc.
until the keyword is used up, whereupon the rest of the ciphertext letters are used
in alphabetical order, excluding those already used in the key."""
import string


class Cipher:
    alphabet = string.ascii_uppercase

    def __init__(self, keyword):
        self.keyword = keyword

    @staticmethod
    def creating_alphabet(keyword):
        alphabet = string.ascii_uppercase
        crypto_alphabet = alphabet
        keyword = keyword.upper()
        for letter in keyword:
            if letter in crypto_alphabet:
                crypto_alphabet = crypto_alphabet.replace(letter, '')
        crypto_alphabet = keyword + crypto_alphabet
        return crypto_alphabet

    def encode(self, word: str):
        crypto_alphabet = cipher.creating_alphabet(self.keyword)
        result = ''
        word = word.upper()
        for letter in word:
            if letter == ' ':
                result += letter
            else:
                result += crypto_alphabet[self.alphabet.find(letter)]
        result = result.capitalize()
        print(result)

    def decode(self, word: str):
        crypto_alphabet = cipher.creating_alphabet(self.keyword)
        result = ''
        word = word.upper()
        for letter in word:
            if letter == ' ':
                result += letter
            else:
                result += self.alphabet[crypto_alphabet.find(letter)]
        result = result.capitalize()
        print(result)

# Encryption: Keyword is "Crypto"

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
# Example:


cipher = Cipher("crypto")
cipher.encode("Hello world")
# "Btggj vjmgp"

cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"