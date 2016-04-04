#!/usr/bin/env python3 -tt
"""
От подаден str, изведете най-често срещания символ.
Ако подаденият стринг е празен или
съдържа само whitespace (нов ред, интервал, табулация), трябва да изведете "INVALID INPUT".
"""
import sys


def main():
    user_input = input()
    user_input_list_char = list(user_input)

    if user_input_list_char and not all(c.isspace() for c in user_input_list_char):
        dict_char_count = {}

        for c in user_input_list_char:
            if dict_char_count.get(c, None):
                dict_char_count[c] += 1
            else:
                dict_char_count[c] = 1

        dict_char_count_list = list(dict_char_count.items())
        dict_char_count_list.sort(key=lambda item: item[1], reverse=True)
        print("{}".format(dict_char_count_list[0][0]))
    else:
        print("INVALID INPUT")


if __name__ == "__main__":
    sys.exit(main())
