import numpy as np

whiteChars = ["NULL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL", "BS", "HT", "LF", "VT", "FF", "CR", "SO", "SI",
              "DLE", "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN", "EM", "SUB", "ESC", "FS", "GS", "RS", "US", "SP"]

x3 = [
    [1, 2, 0, 3, 1],
    [0, 1, 0, 1, 0],
    [2, 4, 1, 5, 2],
    [1, 3, 2, 4, 1],
    [0, 1, 0, 2, 1]
]

pole_encrypted = []


class Matrix:
    def __init__(self, key):
        self.key = key

    # Encrypt
    def encrypt(self, plaintext):

        # Rozdel input na 25
        plaintext_to_25 = self.split_to_25(plaintext)
        x2 = self.matrix_to_number(self.create_matrix(self.update_string_to_25(self.key)))

        # Sifrovanie
        pole_encrypted.clear()
        for x in range(len(plaintext_to_25)):
            xxs = self.create_matrix(plaintext_to_25[x])
            xxs = self.matrix_to_number(xxs)
            x12 = self.add_matrices(xxs, x2)
            x4 = self.multiply_matrices(x12, x3)
            self.matrix_to_array(x4)

        encrypted = pole_encrypted
        return encrypted

    # Desifrovanie
    def decrypt(self, encryptedText):
        # print(encryptedText)
        encrypted_text = self.split_to_25(encryptedText)
        x2 = self.matrix_to_number(self.create_matrix(self.update_string_to_25(self.key)))
        x3_inversed = self.inverse_matrix(x3)
        # print(x2)

        pole_encrypted.clear()
        for x in range(len(encrypted_text)):
            x4 = self.create_matrix(encrypted_text[x])
            x5 = self.multiply_matrices(x4, x3_inversed)
            x12 = self.subtract_matrices(x5, x2)
            self.matrix_to_array(x12)

        decrypted = pole_encrypted
        return decrypted

    def numberArray_to_charArray(self, array):
        arrayChar = []
        for x in range(len(array)):
            ascii_number = array[x] % 127
            if 32 < ascii_number < 127:
                arrayChar.append(chr(ascii_number))
            if 0 <= ascii_number <= 32:
                arrayChar.append(whiteChars[ascii_number])
            if ascii_number == 127:
                arrayChar.append("DEL")
        return arrayChar

    def matrix_to_array(self, matrix):
        for x in range(5):
            for y in range(5):
                pole_encrypted.append(int(matrix[x][y]))

    def multiply_matrices(self, matrix1, matrix2):
        # Skontrolujte, či je počet stĺpcov prvej matice rovnaký s počtom riadkov druhej matice
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Počet stĺpcov prvej matice sa musí rovnať počtu riadkov druhej matice.")

        # Inicializujte výslednú maticu s nulami
        result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

        # Násobte matice
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

        return result_matrix

    def add_matrices(self, matrix1, matrix2):
        # Skontrolujte, či majú obidve matice rovnaké rozmery
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matice majú rôzne rozmery, nie je možné ich sčítať.")

        # Sčítajte matice
        result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

        return result_matrix

    def subtract_matrices(self, matrix1, matrix2):
        # Skontrolujte, či majú obidve matice rovnaké rozmery
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matice majú rôzne rozmery, nie je možné ich odčítať.")

        # Odčítajte matice
        result_matrix = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

        return result_matrix

    def custom_round(self, value, decimal_places=4):
        rounded_value = round(value, decimal_places)
        return rounded_value if rounded_value != 0 else abs(rounded_value)

    def inverse_matrix(self, matrix):
        try:
            # Skontrolujte, či je matica štvorcová (má rovnaký počet riadkov a stĺpcov)
            if len(matrix) != len(matrix[0]):
                raise ValueError("Matica nie je štvorcová, nemá inverznú maticu.")

            # Konvertujte maticu na numpy array
            np_matrix = np.array(matrix)

            # Vytvorte inverznú maticu
            inv_matrix = np.linalg.inv(np_matrix)

            # Použite vlastnú funkciu na zaokrúhľovanie
            rounded_matrix = [[self.custom_round(element) for element in row] for row in inv_matrix]

            return rounded_matrix

        except np.linalg.LinAlgError:
            raise ValueError("Matica nemá inverznú maticu.")

    def matrix_to_number(self, matrix):
        matrix_number = [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ]
        for x in range(5):
            for y in range(5):
                matrix_number[x][y] = ord(matrix[x][y])

        return matrix_number

    def update_string_to_25(self, key, pocet_opakovani=5):
        # Opakujeme vstupny string urcity pocet krat
        opakovany_string = key * pocet_opakovani

        # Ak je vysledny string kratsi ako 25 znakov, opakujeme ho potrebny pocet krat
        while len(opakovany_string) < 25:
            opakovany_string += opakovany_string

        # Vratime prvych 25 znakov
        return opakovany_string[:25]

    # Split string on same 25 lenght parts
    def split_to_25(self, plaintext):
        # Inicializujeme prázdny zoznam pre výsledné časti
        casti = []

        # Iterujeme cez string s krokom 25
        for i in range(0, len(plaintext), 25):
            cast = plaintext[i:i + 25]

            # Ak je posledná časť kratšia ako 25 znakov, doplníme chýbajúce znaky
            if len(cast) < 25:
                chybajuce_znaky = 25 - len(cast)
                posledny_znak = cast[-1]

                for j in range(chybajuce_znaky):
                    # Doplníme znaky od posledného znaku podľa abecedy
                    if posledny_znak == 'z':
                        posledny_znak = 'a'
                    elif posledny_znak == 'Z':
                        posledny_znak = 'A'
                    posledny_znak = chr(ord(posledny_znak) + 1)
                    cast += posledny_znak

            casti.append(cast)

        return casti

    # Create matrix from string
    def create_matrix(self, text):
        matrix = [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ]
        counter = 0
        for x in range(5):
            for y in range(5):
                matrix[x][y] = text[counter]
                counter = counter + 1

        return matrix
