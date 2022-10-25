import cryptoroutine
import caesar


def run():
    run_mode = int(input("Cryptor mode (1 - ENCRYPT, 2 - DECRYPT): "))
    if run_mode == 1:
        run_encrypt()
    if run_mode == 2:
        run_decrypt()


def run_encrypt():
    text = input("Text to crypt: ")
    shift = int(input("Key shift: "))

    cryptor = create_cryptor(shift)
    encrypted_text = cryptor.encrypt(text)

    print("Encrypted text: " + encrypted_text + "\n")
    run()


def run_decrypt():
    text = input("Enter text to crypt: ")
    shift = int(input("Key shift: "))

    cryptor = create_cryptor(shift)
    decrypted_text = cryptor.decrypt(text)

    print("Decrypted text: " + decrypted_text + "\n")
    run()


def create_cryptor(shift):
    alphabet_en = cryptoroutine.Alphabet(source='ABCDEFGHIJKLMNOPQRSTUVWXYZ', shift=shift)
    alphabet_en_swapped = alphabet_en.create_swapcased()

    alphabet_ru = cryptoroutine.Alphabet(source='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', shift=shift)
    alphabet_ru_swapped = alphabet_ru.create_swapcased()

    alphabet_numbers = cryptoroutine.Alphabet(source='0123456789', shift=shift)

    monster_alphabet = alphabet_en + alphabet_en_swapped + alphabet_ru + alphabet_ru_swapped + alphabet_numbers

    return caesar.CaesarCryptor(monster_alphabet)


run()
