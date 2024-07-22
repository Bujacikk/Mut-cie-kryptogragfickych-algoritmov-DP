class VigenerUpdated:

    def __init__(self, key):
        self.key = key
        self.square = self.generateSquare(key[0], key[1])

    # Encrypt
    def encrypt(self, plaintext):
        updatedPlaintext = self.updateText(plaintext)
        updatedKey = self.updateKeyLength(self.updateText(self.key), updatedPlaintext)
        column = ord(self.key[1].upper()) - 65
        encrypted_text = ""

        for x in range(len(updatedKey)):
            encrypted_text = encrypted_text + self.findEncryptedLetter(updatedKey[x], updatedPlaintext[x], column)
        return encrypted_text

    # Decrypt
    def decrypt(self, encrypted):
        updatedEncrypted = self.updateText(encrypted)
        updatedKey = self.updateKeyLength(self.updateText(self.key), updatedEncrypted)
        column = ord(self.key[1].upper()) - 65
        encrypted_text = ""

        for x in range(len(updatedKey)):
            encrypted_text = encrypted_text + self.findDecryptedLetter(updatedKey[x], updatedEncrypted[x], column)
        return encrypted_text

    # Copy key to length of plaintext
    def updateKeyLength(self, key, updatedPlaintext):
        updatedKey = []
        count = 0
        for x in range(len(updatedPlaintext)):
            updatedKey.append(key[count])
            count = count + 1
            if count == len(key):
                count = 0
        return updatedKey

    # Remove spaces, check only ascii letters, toupper
    def updateText(self, plaintext):
        plaintextUpdated = []
        for letter in plaintext:
            letterOrd = ord(letter)
            if 96 < letterOrd < 123 or 64 < letterOrd < 91:
                plaintextUpdated.append(letter.upper())
        return plaintextUpdated

    # Find encrypted letter
    def findEncryptedLetter(self, keyLetter, plaintextLetter, column):
        coordinates = []
        row = column

        for x in range(27):
            if self.square[x][column] == keyLetter:
                coordinates.append(x)

        for x in range(27):
            if self.square[row][x] == plaintextLetter:
                coordinates.append(x)

        return self.square[coordinates[0]][coordinates[1]]

    # Find decrypted letter
    def findDecryptedLetter(self, keyLetter, plaintextLetter, column):
        coordinates = []
        coordinates.append(column)

        for x in range(27):
            if self.square[x][column] == keyLetter:
                row = x

        for x in range(27):
            if self.square[row][x] == plaintextLetter:
                coordinates.append(x)

        return self.square[coordinates[0]][coordinates[1]]

    # Generating vigener square
    def generateSquare(self, shift1, shift2):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        size = 27
        square = [[0 for _ in range(size)] for _ in range(size)]

        shift1 = ord(shift1.upper()) - 65
        shift2 = ord(shift2.upper()) - 65
        self.addAndShiftAxis(square, shift2, alphabet)
        self.fillLetters(square, shift1, shift2, alphabet)
        self.printArray(square)
        return square

    # Shift axis X and Y
    def addAndShiftAxis(self, square, shift2, alphabet):
        y = 0
        alphabetReverse = alphabet.copy()
        alphabetReverse.reverse()
        for x in range(27):
            if x == shift2:
                square[shift2][x] = '*'
                square[x][shift2] = '*'
                continue
            square[shift2][x] = alphabet[y]
            square[x][shift2] = alphabetReverse[y]
            y = y + 1

    # Fill alphabet to empty slots
    def fillLetters(self, square, shift1, shift2, alphabet):
        for x in range(shift1):
            alphabet.append(alphabet[0])
            alphabet.pop(0)

        alphabetOrder = 0
        for x in range(27):
            if x == shift2:
                continue
            for y in range(27):
                if square[x][y] == 0:
                    square[x][y] = alphabet[alphabetOrder]
                    alphabetOrder = alphabetOrder + 1
                    if alphabetOrder == len(alphabet):
                        alphabetOrder = 0
                else:
                    continue
            alphabet.append(alphabet[0])
            alphabet.pop(0)

    def printArray(self, array):
        for line in array:
            print(line)
