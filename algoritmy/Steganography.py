from PIL import Image


class Steganography:
    def __init__(self, image):
        self.image = Image.open(image)

    def encrypt(self, qrcode):
        # Získanie veľkosti obrázka
        # width = riadky
        # height = stplce
        qr_code = Image.open(qrcode)

        # Úprava qr_codu
        updated_qr_code = self.qrcode_change(qr_code)

        # Open QR code
        qr_width, qr_height = updated_qr_code.size

        # Sifrovanie
        for x in range(qr_width):
            for y in range(qr_height):
                current_pixel = updated_qr_code.getpixel((x, y))
                self.image.putpixel((x, y), current_pixel)

        # Zobrazenie obrázka po posunutí pixelov
        self.image.save(r"E:\Projekty\pythonProject\images\encrypted.png")

    def decrypt(self, image):
        # Získanie veľkosti obrázka
        # width = riadky
        # height = stplce
        img = Image.open(image)
        width, height = img.size

        # Desifrovanie
        for x in range(width):
            for y in range(height):
                current_pixel = img.getpixel((x, y))

                # Ak má pixel 4 zložky (RGBA), použijeme všetky
                if len(current_pixel) == 4:
                    red, green, blue, alpha = current_pixel
                else:
                    # Ak má pixel 3 zložky (RGB), ignorujeme alfu
                    red, green, blue = current_pixel
                if red == 1 and green == 0 and blue == 0:
                    red = 255
                    green = 255
                    blue = 255

                # Uloženie upraveného pixelu späť do obrázka
                if len(current_pixel) == 4:
                    img.putpixel((x, y), (red, green, blue, alpha))
                else:
                    img.putpixel((x, y), (red, green, blue))

        # Zobrazenie obrázka po posunutí pixelov
        img.save(r"E:\Projekty\pythonProject\images\decrypted.png")

    # Vytvorenie pola z kluca a doplnenie znakov
    def qrcode_change(self, qr_code):
        img = qr_code
        width, height = img.size

        # Úprava
        for x in range(width):
            for y in range(height):
                current_pixel = img.getpixel((x, y))

                # Ak má pixel 4 zložky (RGBA), použijeme všetky
                if len(current_pixel) == 4:
                    red, green, blue, alpha = current_pixel
                else:
                    # Ak má pixel 3 zložky (RGB), ignorujeme alfu
                    red, green, blue = current_pixel
                if red == 255 and green == 255 and blue == 255:
                    red = 1
                    green = 0
                    blue = 0
                elif red == 242 and green == 242 and blue == 242:
                    red = 1
                    green = 0
                    blue = 0
                elif red == 12 and green == 12 and blue == 12:
                    red = 0
                    green = 0
                    blue = 0

                # Uloženie upraveného pixelu späť do obrázka
                if len(current_pixel) == 4:
                    img.putpixel((x, y), (red, green, blue, alpha))
                else:
                    img.putpixel((x, y), (red, green, blue))
        return img

