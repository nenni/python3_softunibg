#!/usr/bin/env python3 -tt
"""
От подаден str, изведете най-често срещания символ.
Ако подаденият стринг е празен или
съдържа само whitespace (нов ред, интервал, табулация), трябва да изведете "INVALID INPUT".
"""
import sys
from collections import Counter


def main():
    # user_input = input()
    user_input = 'Бъдете внимателни какво отпечатвате като резултат от Вашата програма.'
    user_input = user_input.strip()

    if user_input:
        # print(char_count_1(user_input))
        print(char_count_2(user_input))
    else:
        print("INVALID INPUT")


def char_count_1(user_input):
        dict_char_count = {}
        # print(user_input)
        for c in user_input:
            # print(c)
            if c not in dict_char_count:
                dict_char_count[c] = 1
            else:
                dict_char_count[c] += 1

        dict_char_count_list = list(dict_char_count.items())
        dict_char_count_list.sort(key=lambda item: item[1], reverse=True)
        # print(dict_char_count_list)
        return dict_char_count_list[0][0]


def char_count_2(user_input):
    counter = Counter(user_input)
    # print(counter)
    # counter_list = list(counter.items())
    # counter_list.sort(key=lambda item: item[1], reverse=True)
    # print(counter_list[0])
    # return counter_list[0][0]
    #
    counter_most_1 = counter.most_common(1)
    # print(counter_most_1)
    return counter_most_1[0][0]

if __name__ == "__main__":
    sys.exit(main())
