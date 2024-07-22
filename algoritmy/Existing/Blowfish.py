from Crypto.Cipher import Blowfish
from Crypto import Random

class Blowfish_alg:
    def __init__(self):
        pass

    def pad_data(self, data):
        # Blowfish works with block sizes, so we need to pad the data to fit the block size
        block_size = Blowfish.block_size
        padding = block_size - (len(data) % block_size)
        return data + bytes([padding] * padding)

    def unpad_data(self, data):
        # Remove the padding added during encryption
        padding = data[-1]
        return data[:-padding]

    def encrypt_data(self, key, data):
        data = self.pad_data(data)
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)
        ciphertext = cipher.encrypt(data)
        return ciphertext

    def decrypt_data(self, key, ciphertext):
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)
        data = cipher.decrypt(ciphertext)
        return self.unpad_data(data)


