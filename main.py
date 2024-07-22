from algoritmy.MatrixCipher import Matrix
import time

if __name__ == "__main__":
    subory = ['testFiles/512', 'testFiles/1024', 'testFiles/2048', 'testFiles/4096',
              'testFiles/8192', 'testFiles/16384','testFiles/32768', 'testFiles/65536',
              'testFiles/131072', 'testFiles/262144', 'testFiles/524288', 'testFiles/1048576']

    images = ['testImages/100.png', 'testImages/200.png', 'testImages/300.png', 'testImages/400.png',
              'testImages/500.png', 'testImages/600.png', 'testImages/700.png', 'testImages/800.png',
              'testImages/900.png', 'testImages/1000.png', 'testImages/1100.png', 'testImages/1200.png']

    for file in subory:
        time_sum = 0
        for x in range(100):
            f = open(file, "r")
            data = f.read()

            binaryCipher = Matrix("VelmiTajneHeslo")

            start = time.time()
            text = binaryCipher.encrypt(data)
            end = time.time()
            time_sum = time_sum + (end - start)
            # print(end - start)
        print(time_sum / 100)

    # AES
    # plaintext = input('Enter the plaintext : ').encode()
    # key = input('Enter key (must be less than 16 symbols and should consist of only alphabets & numbers) : ')
    # AES(plaintext, key)

    # DES
    # plaintext = input("Enter the message to be encrypted : ")
    # key = input("Enter a key of 8 length (64-bits) (characters or numbers only) : ")
    # DES(plaintext, key)

    # RSA
    # bit_length = int(input("Enter bit_length: "))
    # msg = input("Write msg: ")
    # msg = data
    # RSA(4, msg)

    # Elgamal
    # msg = input("Enter message: ")
    # msg = data
    # Elgamal(msg)

    # ECC
    # msg = input("Enter message: ")
    # msg = bytes(msg, 'utf-8')
    # ECC(msg)

    # # Blowfish
    # key = Random.new().read(16)
    # plaintext = input("Enter message: ")
    # plaintext = plaintext.encode('utf-8')
    # msg = bytes(msg, 'utf-8')
    # blowfish = Blowfish_alg()
    # encrypted_data = blowfish.encrypt_data(key, msg)

    # BruteForce
    # BruteForce("TajnyK")

    # VigenerUpdated
    # msg = "sprava"
    # encrypted_text = VigenerUpdated("AYJGZQXIBZFEHOR").encrypt(msg)
    # print(encrypted_text)

    # VigenerUpdated
    # key = "KLUC"
    # vigenere_cipher = VigenereCipher(key)
    # plain_text = "sprava"
    # encrypted_text = vigenere_cipher.encrypt(plain_text)
    # print(encrypted_text)

    # BinaryCipher
    # binaryCipher = BinaryCipher("VelmiTajneHeslo")
    # plain_text = "sprava"
    # plain = binaryCipher.updateText(plain_text)
    # encrypted_text = binaryCipher.encrypt(plain_text)

    # Matrix
    # binaryCipher = Matrix("VelmiTajneHeslo")
    # text = binaryCipher.encrypt("sprava")
    # result = binaryCipher.numberArray_to_charArray(text)
    # print(result)

    # Images
    # imageCipher = ImageCipher("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam pellentesque sed")
    # imageCipher.encrypt("E:\Projekty\pythonProject\images\obama.jpg")
    # imageCipher.decrypt("E:\Projekty\pythonProject\images\encrypted.png")

    # Steganography
    # imageCipher = Steganography("E:\Projekty\pythonProject\images\qfotka.png")
    # imageCipher.encrypt('E:\Projekty\pythonProject\images\qr_code.png')
    # imageCipher.decrypt("E:\Projekty\pythonProject\images\encrypted.png")

