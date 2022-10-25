class Alphabet:
    source: list[str]
    shifted: list[str]
    shift: int

    def __init__(self, source: str = '', shift: int = 0):
        self.source = list(source)
        self.shift = shift
        self.fill_shifted()

    def fill_shifted(self):
        self.shifted = list()
        shifted_index = self.shift
        first_part = self.source[shifted_index:]
        second_part = self.source[:shifted_index]
        self.shifted = first_part + second_part

    def create_swapcased(self):
        source = self.source
        shift = self.shift

        new_source = list()
        for letter in source:
            new_source.append(letter.swapcase())

        return Alphabet(new_source, shift)

    def __add__(self, other):
        first_src = self.source
        first_shifted = self.shifted
        second_src = other.source
        second_shifted = other.shifted

        new = Alphabet()
        new.source = first_src + second_src
        new.shifted = first_shifted + second_shifted
        return new


def do_tests():
    src = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = Alphabet(source=src, shift=3)

    a_swapcased = a.create_swapcased()

    a_total = a + a_swapcased


do_tests()