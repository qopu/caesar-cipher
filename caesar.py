import cryptoroutine


class CaesarCryptor:
    alphabet: cryptoroutine.Alphabet
    to_encrypted: dict
    to_decrypted: dict

    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.init_translation_dictionaries()

    def init_translation_dictionaries(self):
        enc = zip(self.alphabet.source, self.alphabet.shifted)
        self.to_encrypted = ''.maketrans(dict(enc))

        dec = zip(self.alphabet.shifted, self.alphabet.source)
        self.to_decrypted = ''.maketrans(dict(dec))

    def encrypt(self, text):
        return text.translate(self.to_encrypted)

    def decrypt(self, text):
        return text.translate(self.to_decrypted)