whiteChars = ["NULL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL", "BS", "HT", "LF", "VT", "FF", "CR", "SO", "SI",
              "DLE", "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN", "EM", "SUB", "ESC", "FS", "GS", "RS", "US", "SP"]


class Matrix:
    def __init__(self, key):
        self.key = key

    # Encrypt
    def encrypt(self, plaintext):
        matriceTextu = self.rozdel_na_25_znakov(plaintext)
        keyMatrix = self.zvacsi_string(self.key)

        suc = []
        nas = []
        for count in range(len(matriceTextu)):
            suc = suc + self.suc_matic(matriceTextu[count], keyMatrix)

        for count in range(len(matriceTextu)):
            nas = nas + self.nas_matic(matriceTextu[count], keyMatrix)

        result = self.odcitani_matic(nas, suc)
        result = self.uprav_Vysledok(result)

        return result

    def rozdel_na_25_znakov(self, plaintext):
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
                    elif  posledny_znak == 'Z':
                        posledny_znak = 'A'
                    posledny_znak = chr(ord(posledny_znak) + 1)
                    cast += posledny_znak

            casti.append(cast)

        return casti

    def zvacsi_string(self, key, pocet_opakovani=5):
        # Opakujeme vstupny string urcity pocet krat
        opakovany_string = key * pocet_opakovani

        # Ak je vysledny string kratsi ako 25 znakov, opakujeme ho potrebny pocet krat
        while len(opakovany_string) < 25:
            opakovany_string += opakovany_string

        # Vratime prvych 25 znakov
        return opakovany_string[:25]

    def suc_matic(self, maticaText, maticaKey):
        # Zistime rozmery matic
        radky = len(maticaText)
        sloupce = len(maticaText[0])

        # Overime, ci maju obe matice rovnake rozmery
        if radky != len(maticaKey) or sloupce != len(maticaKey[0]):
            raise ValueError("Matice majú rôzne rozmery, nie je možné ich sčítať.")

        # Inicializujeme maticu pre vysledok
        vysledek = []

        # Sčítame jednotlivé prvky matíc a prevádzame znaky na ASCII hodnoty
        for i in range(radky):
            for j in range(sloupce):
                ascii_text = ord(maticaText[i][j])
                ascii_key = ord(maticaKey[i][j])
                vysledek.append(ascii_text + ascii_key)

        return vysledek

    def nas_matic(self, maticaText, maticaKey):
        # Zistime rozmery matic
        radky = len(maticaText)
        sloupce = len(maticaText[0])

        # Overime, ci maju obe matice rovnake rozmery
        if radky != len(maticaKey) or sloupce != len(maticaKey[0]):
            raise ValueError("Matice majú rôzne rozmery, nie je možné ich sčítať.")

        # Inicializujeme maticu pre vysledok
        vysledek = []

        # Sčítame jednotlivé prvky matíc a prevádzame znaky na ASCII hodnoty
        for i in range(radky):
            for j in range(sloupce):
                ascii_text = ord(maticaText[i][j])
                ascii_key = ord(maticaKey[i][j])
                vysledek.append(ascii_text * ascii_key)

        return vysledek

    def odcitani_matic(self, matica1, matica2):
        # Zistime rozmery matic
        radky_m1 = len(matica1)
        radky_m2 = len(matica2)

        # Overime, ci matice maju spravne rozmery na odčítanie
        if radky_m1 != radky_m2:
            raise ValueError("Nemožno odčítať matice. Matice musia mať rovnaké rozmery.")

        # Inicializujeme maticu pre vysledok
        vysledek = []

        # Vypočítame jednotlivé prvky matice vysledku
        for i in range(radky_m1):
            vysledek.append(matica1[i] - matica2[i])

        return vysledek

    def uprav_Vysledok(self, vysledek):
        for x in range(len(vysledek)):
            vysledek[x] = vysledek[x] + 127
            vysledek[x] = vysledek[x] % 127
            if 0 <= vysledek[x] <= 32:
                vysledek[x] = whiteChars[vysledek[x]]
            elif vysledek[x] == 127:
                vysledek[x] = "DEL"
            else:
                vysledek[x] = chr(vysledek[x])
        return vysledek