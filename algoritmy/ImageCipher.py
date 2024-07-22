from PIL import Image


class ImageCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, image):
        # Získanie veľkosti obrázka
        # width = riadky
        # height = stplce
        img = Image.open(image)
        width, height = img.size

        # Úprava kľúča
        keyArray = self.create_2d_array(width, height, self.key)

        # Sifrovanie
        for x in range(width):
            for y in range(height):
                current_pixel = img.getpixel((x, y))
                next_x, next_y = self.findCoordination(keyArray[x][y], height, width, x, y)
                next_pixel = img.getpixel((next_x, next_y))

                img.putpixel((next_x, next_y), current_pixel)
                img.putpixel((x, y), next_pixel)

        # Uloženie obrázka
        img.save(r"E:\Projekty\pythonProject\images\encrypted.png")

    def decrypt(self, image):
        # Získanie veľkosti obrázka
        # width = riadky
        # height = stplce
        img = Image.open(image)
        width, height = img.size

        # Úprava kľúča
        keyArray = self.create_2d_array(width, height, self.key)

        # Dešifrovanie
        for x in range((width - 1), -1, -1):
            for y in range((height - 1), -1, -1):
                current_pixel = img.getpixel((x, y))
                next_x, next_y = self.findCoordination(keyArray[x][y], height, width, x, y)
                next_pixel = img.getpixel((next_x, next_y))

                img.putpixel((next_x, next_y), current_pixel)
                img.putpixel((x, y), next_pixel)

        # Uloženie obrázka
        img.save(r"E:\Projekty\pythonProject\images\decrypted.png")

    # Vytvorenie pola z kluca a doplnenie znakov
    def create_2d_array(self, x, y, input_string):
        # Vytvorenie prázdneho 2D poľa
        result_array = [[0] * y for _ in range(x)]

        # Konverzia reťazca na pole ASCII hodnôt
        ascii_values = [ord(char) for char in input_string]

        # Naplnenie 2D poľa hodnotami zo vstupného reťazca
        index = 0
        for i in range(x):
            for j in range(y):
                # Opakovanie znakov, ak zostanú voľné miesta
                result_array[i][j] = ascii_values[index % len(ascii_values)]
                index += 1

        for x in range(x):
            for y in range(y):
                result_array[x][y] = result_array[x][y] * 130000

        return result_array

    # Vypis 2D polia
    def print_2dArray(self, array):
        for x in range(len(array)):
            for y in range(len(array[0])):
                print(array[x][y], end=" ")
            print()

    # Najde suradnice na vymenu
    def findCoordination(self, shift, height, width, x, y):
        overshitf = 0

        y1 = shift % height
        y1 = y1 + y
        if y1 > (height - 1):
            y1 = y1 % height
            overshitf = overshitf + 1

        x1 = shift // height
        x1 = x1 + x + overshitf
        if x1 > (width - 1):
            x1 = x1 % width

        return x1, y1
