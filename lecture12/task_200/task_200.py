#!/usr/bin/env python3 -tt

import sys
import string


def main():

    try:
        key = int(input())
        ca = create_crypt_alphabet(key)
        message = "SOFTUNI PRACTICE EXAM 2"
        # message = input()
        message.strip()
        print(encrypt_message(message, ca))
        return 0

    except Exception as e:
        print("INVALID INPUT")


def encrypt_message(message, ca):
    result = []
    for c in message:
        if c in ca:
            result.append(ca[c])
        else:
            result.append(c)

    return ''.join(result)


def create_crypt_alphabet(key):
    alphabet = string.ascii_uppercase
    # print(alphabet)
    # print(len(alphabet))
    ord_A = ord("A")
    # print(ord_A)
    # crypt_alphabet = []
    crypt_alphabet = {}
    for c in alphabet:
        enc = (ord(c) - ord_A + key) % len(alphabet)
        # enc = enc % len(alphabet)
        # print(enc)
        # print(enc + ord_A)
        crypt_alphabet[c] = (chr(enc + ord_A))
    # print(crypt_alphabet)
    # print(''.join(crypt_alphabet))
    # print(crypt_alphabet)
    return crypt_alphabet


if __name__ == '__main__':
    sys.exit(main())
