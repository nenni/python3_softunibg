#!/usr/bin/env python -tt

"""
По подадени дължините на трите страни на триъгълник, пресметнете лицето му,
като закръглите резултата до втората цифра след десетичната запетая.
Формулата за пресмятане на лицето на триъгълник с дължини на страните a, b и c е:
S = math.sqrt(p * (p - a) * (p - b) * (p - c)) , където p = (a + b + c) / 2
Ако са подадени невалидни данни, е необходимо да изведете INVALID INPUT
"""
import sys
import math


def main():
    try:
        a_in = input()
        b_in = input()
        c_in = input()

        # TODO: check user input
        a, b, c = _check_user_input(a_in, b_in, c_in)
        p = (a + b + c) / 2
        tri_sqr = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("{:.2f}".format(tri_sqr))

        return 0

    except Exception as e:
        print("INVALID INPUT")
        return 1


def _check_user_input(a, b, c):

    try:
        a = float(a)
        b = float(b)
        c = float(c)

        return a, b, c

    except ValueError as e:
        raise ValueError

if __name__ == "__main__":
    sys.exit(main())