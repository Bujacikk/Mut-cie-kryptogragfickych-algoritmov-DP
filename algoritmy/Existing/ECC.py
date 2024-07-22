from tinyec import registry
from Crypto.Cipher import AES
import hashlib, secrets, binascii
import time

class ECC:
    def __init__(self, msg):
        self.ECCalgorythm(msg)

    def ECCalgorythm(self, msg):
        # print("original msg:", msg)
        privKey = secrets.randbelow(self.curve.field.n)
        pubKey = privKey * self.curve.g

        encryptedMsg = self.encrypt_ECC(msg, pubKey)
        encryptedMsgObj = {
            'ciphertext': binascii.hexlify(encryptedMsg[0]),
            'nonce': binascii.hexlify(encryptedMsg[1]),
            'authTag': binascii.hexlify(encryptedMsg[2]),
            'ciphertextPubKey': hex(encryptedMsg[3].x) + hex(encryptedMsg[3].y % 2)[2:]
        }
        # print("encrypted msg:", encryptedMsgObj)
        start_time = time.time()
        decryptedMsg = self.decrypt_ECC(encryptedMsg, privKey)
        end_time = time.time()
        print(end_time - start_time)
        # print("decrypted msg:", decryptedMsg)

    def encrypt_AES_GCM(self, msg, secretKey):
        aesCipher = AES.new(secretKey, AES.MODE_GCM)
        ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
        return (ciphertext, aesCipher.nonce, authTag)

    def decrypt_AES_GCM(self, ciphertext, nonce, authTag, secretKey):
        aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
        return plaintext

    def ecc_point_to_256_bit_key(self, point):
        sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
        sha.update(int.to_bytes(point.y, 32, 'big'))
        return sha.digest()

    curve = registry.get_curve('brainpoolP256r1')

    def encrypt_ECC(self, msg, pubKey):
        ciphertextPrivKey = secrets.randbelow(self.curve.field.n)
        sharedECCKey = ciphertextPrivKey * pubKey
        secretKey = self.ecc_point_to_256_bit_key(sharedECCKey)
        ciphertext, nonce, authTag = self.encrypt_AES_GCM(msg, secretKey)
        ciphertextPubKey = ciphertextPrivKey * self.curve.g
        return (ciphertext, nonce, authTag, ciphertextPubKey)

    def decrypt_ECC(self, encryptedMsg, privKey):
        (ciphertext, nonce, authTag, ciphertextPubKey) = encryptedMsg
        sharedECCKey = privKey * ciphertextPubKey
        secretKey = self.ecc_point_to_256_bit_key(sharedECCKey)
        plaintext = self.decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey)
        return plaintext
