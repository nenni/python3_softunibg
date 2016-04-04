#!/usr/bin/env python3 -tt
"""
Анаграма е игра на думи, при която когато пренаредим буквите от една дума, можем да съставим друга,
 като можем да използваме буквите от оригиналната дума само по веднъж.

По подадено име на файл, който съдържа по една дума на ред, и дума,
изведете всички анаграми на подадената дума сортирани по азбучен ред, без самата нея. Думите във файла не са сортирани.

Ако в подадения файл не могат да бъдат намерени анаграми на подадената дума, трябва да изведете само NO ANAGRAMS
При подадени грешни данни, е необходимо да изведете само INVALID INPUT
ВХОД:
./words.txt
horse

Примерно съдържание на файл:
shore
bibles
heros
horse
beta

РЕЗУЛТАТ:
heros
shore
"""
import sys


def main():
    try:
        # input_words = './words.txt'
        # word = 'horse'

        input_words = input()
        word = input()
        word.strip()
        word_letters_sorted = sorted(word)
        # print(word_letters_sorted)

        with open(input_words) as f:
            words = [l.strip() for l in f.readlines()]

        anagrams = []
        for current_w in words:
            if len(current_w) == len(word) and current_w != word:
                if sorted(current_w) == word_letters_sorted:
                    anagrams.append(current_w)
        if anagrams:
            anagrams.sort()
            print('\n'.join(anagrams))
        else:
            print("NO ANAGRAMS")
        return 0

    except Exception as e:
        print("INVALID INPUT", str(e))
        return 1


if __name__ == '__main__':
    sys.exit(main())
