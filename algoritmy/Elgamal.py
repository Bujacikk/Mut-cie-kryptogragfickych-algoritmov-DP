# Zdroj: https://www.codespeedy.com/elgamal-encryption-algorithm-in-python/
import random
from math import pow

a = random.randint(2, 10)


class Elgamal:

    def __init__(self, msg):
        self.ElgamalAlgorythm(msg)

    def ElgamalAlgorythm(self, msg):
        q = random.randint(pow(10, 20), pow(10, 50))
        g = random.randint(2, q)
        key = self.gen_key(q)
        h = self.power(g, key, q)
        print("g used=", g)
        print("g^a used=", h)
        ct, p = self.encryption(msg, q, h, g)
        print("Original Message=", msg)
        print("Encrypted Maessage=", ct)
        pt = self.decryption(ct, p, key, q)
        d_msg = ''.join(pt)
        print("Decryted Message=", d_msg)

    # To fing gcd of two numbers
    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)
        elif a % b == 0:
            return b
        else:
            return self.gcd(b, a % b)

    # For key generation i.e. large random number
    def gen_key(self, q):
        key = random.randint(pow(10, 20), q)
        while self.gcd(q, key) != 1:
            key = random.randint(pow(10, 20), q)
        return key

    def power(self, a, b, c):
        x = 1
        y = a
        while b > 0:
            if b % 2 == 0:
                x = (x * y) % c;
            y = (y * y) % c
            b = int(b / 2)
        return x % c

    # For asymetric encryption
    def encryption(self, msg, q, h, g):
        ct = []
        k = self.gen_key(q)
        s = self.power(h, k, q)
        p = self.power(g, k, q)
        for i in range(0, len(msg)):
            ct.append(msg[i])
        print("g^k used= ", p)
        print("g^ak used= ", s)
        for i in range(0, len(ct)):
            ct[i] = s * ord(ct[i])
        return ct, p

    # For decryption
    def decryption(self, ct, p, key, q):
        pt = []
        h = self.power(p, key, q)
        for i in range(0, len(ct)):
            pt.append(chr(int(ct[i] / h)))
        return pt

