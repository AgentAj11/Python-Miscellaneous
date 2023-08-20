import random as rd


def get_key():
    k1 = [chr(x) for x in range(65, 91)]
    k2 = [chr(x) for x in range(97, 123)]
    k = k1 + k2
    v1 = [chr(x) for x in range(65, 91)]
    v2 = [chr(x) for x in range(97, 123)]
    v = v1 + v2
    rd.shuffle(v)
    key = {}
    for i in range(len(k)):
        key[k[i]] = v[i]
    return key


def encrypt(msg, key):
    cipher = ""
    for char in msg:
        cipher += key.get(char, char)
    return cipher


def decrypt(cipher, key):
    inverted_key = {v: k for k, v in key.items()}
    msg = ""
    for char in cipher:
        msg += inverted_key.get(char, char)
    return msg


def driver():
    key = get_key()
    msg = "hello hello name is Ajay Gaurav"
    cipher = encrypt(msg, key)
    print(f"Original text : {msg}")
    print(f"Encrypted text : {cipher}")
    print(f"Decrypted text : {decrypt(cipher, key)}")


driver()
