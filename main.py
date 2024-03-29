import cryptoroutine
import caesar
import colors


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

    print("Encrypted text: " + colors.RED + encrypted_text + colors.STANDART + "\n")
    run()


def run_decrypt():
    text = input("Enter text to crypt: ")
    shift = int(input("Key shift: "))

    cryptor = create_cryptor(shift)
    decrypted_text = cryptor.decrypt(text)

    print("Decrypted text: " + colors.GREEN + decrypted_text + colors.STANDART + "\n")
    run()


def create_cryptor(shift):
    alphabet_en = cryptoroutine.Alphabet(source='ABCDEFGHIJKLMNOPQRSTUVWXYZ', shift=shift)
    alphabet_en_swapped = alphabet_en.create_swapcased()

    alphabet_ru = cryptoroutine.Alphabet(source='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', shift=shift)
    alphabet_ru_swapped = alphabet_ru.create_swapcased()

    alphabet_numbers = cryptoroutine.Alphabet(source='0123456789', shift=shift)

    monster_alphabet = alphabet_en + alphabet_en_swapped + alphabet_ru + alphabet_ru_swapped + alphabet_numbers

    return caesar.CaesarCryptor(monster_alphabet)


def test():
    text = input("Enter text to crypt: ")
    for i in range(1, 33):
        cryptor = create_cryptor(i)
        decrypted_text = cryptor.decrypt(text)
        print("Decrypted text: " + colors.GREEN + decrypted_text + colors.STANDART + str(i) + "\n")

if __name__ == "__main__":
    test()