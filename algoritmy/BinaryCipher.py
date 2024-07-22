

whiteChars = ["NULL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL", "BS", "HT", "LF", "VT", "FF", "CR", "SO", "SI",
              "DLE", "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN", "EM", "SUB", "ESC", "FS", "GS", "RS", "US", "SP"]


class BinaryCipher:
    def __init__(self, key):
        self.key = key

    # Encrypt
    def encrypt(self, plaintext):
        znak = None
        encrypted = []
        updatedPlaintext = self.updateText(plaintext)
        updatedKey = self.updateKeyLength(self.updateText(self.key), updatedPlaintext)

        for n in range(len(updatedPlaintext)):
            result = self.XOR(updatedKey[n], updatedPlaintext[n], 1)
            if 0 <= result <= 32:
                znak = whiteChars[result]
            elif result == 127:
                znak = "DEL"
            else:
                znak = chr(result)

            encrypted.append(znak)
        # print(str(encrypted))
        # print(''.join(map(str, encrypted)))
        return encrypted

    # Decryption
    def decrypt(self, encrypted):
        znak = None
        decrypted = []
        updatedKey = self.updateKeyLength(self.updateText(self.key), encrypted)

        for n in range(len(encrypted)):
            if encrypted[n] == "DEL":
                index = chr(127)
            elif len(encrypted[n]) > 1 and encrypted[n] != "DEL":
                index = self.findIndex(encrypted[n])
            elif len(encrypted[n]) == 1:
                index = ord(encrypted[n])

            result = self.XOR(updatedKey[n], index, 0)
            znak = chr(result)
            decrypted.append(znak)

        # print(str(decrypted))
        # print(''.join(map(str, decrypted)))
        return decrypted

    # Funcion find index of white mark in array
    def findIndex(self, string):
        for x in range(len(whiteChars)):
            if whiteChars[x] == string:
                return x

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
            if 32 < letterOrd < 127:
                plaintextUpdated.append(letter)
            elif letterOrd > 127:
                print(letterOrd)
                print("NEPLATNY VSTUP")
                exit()
        return plaintextUpdated

    # XOR function for encryption and decryption
    # You can send key (letter) and plaintext (letter)
    # encryption = 1 , decryption = 0
    def XOR(self, key, plaintext, true):
        key_ascii_hodnota = ord(key)
        if true == 1:
            plaintext_ascii_hodnota = ord(plaintext)
            result = key_ascii_hodnota ^ plaintext_ascii_hodnota
            return result
        if true == 0:
            result = key_ascii_hodnota ^ plaintext
            return result
