class VigenereCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plain_text):
        encrypted_text = ""
        key_length = len(self.key)

        for i in range(len(plain_text)):
            char = plain_text[i]
            if char.isalpha():
                key_char = self.key[i % key_length]
                key_shift = ord(key_char.upper()) - 65
                if char.isupper():
                    encrypted_char = chr(((ord(char) - 65 + key_shift) % 26) + 65)
                else:
                    encrypted_char = chr(((ord(char) - 97 + key_shift) % 26) + 97)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char

        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = ""
        key_length = len(self.key)

        for i in range(len(encrypted_text)):
            char = encrypted_text[i]
            if char.isalpha():
                key_char = self.key[i % key_length]
                key_shift = ord(key_char.upper()) - 65
                if char.isupper():
                    decrypted_char = chr(((ord(char) - 65 - key_shift) % 26) + 65)
                else:
                    decrypted_char = chr(((ord(char) - 97 - key_shift) % 26) + 97)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char

        return decrypted_text



