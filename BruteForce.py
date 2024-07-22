import itertools

def bruteForce(key):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    count = 0

    for r in range(1, 17):
        for combo in itertools.product(alphabet, repeat=r):
            word = ''.join(combo)
            count = count + 1
            if word == key:
                print(count)
                return

class BruteForce:

    def __init__(self, key):
        bruteForce(key)

