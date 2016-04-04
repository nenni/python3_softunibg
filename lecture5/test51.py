#!/usr/bin/env python3 -tt

"""
Напишете програма, която търси за файлове във Вашата файлова система.
Програмата трябва да получава два параметъра при извикването - къде да търси, и какво да търси.
Примерно извикване на програмата:
python3  find.py  /home/user/Downloads  me.jpg

В този случай find.py е името на скрипта, /home/user/Downloads в коя папка да се търси,
и me.jpg е името на търсения файл.
Търсенето трябва да да включва всички поддиректории, които се намират в началната директория за търсене.

Ако файлът не е намерен, трябва да се показва съобщение, че файлът не е намерен.
В противен случай трябва да се отпечата пълния път до файла.

Ако има повече от един файл със същото име в различни директории трябва да се покаже списък с всички намерени файлове.

Допълнение на задачата:
Разширете вашия код, така че да може да търсите с прост wild card * - в началото или в края на името.

Пример:
python3   find.py   /home/Downloads   me*

В примера по-горе кодът ще трябва да намери всички файлове,
чието име започва с me, без значение какви символи следват след това.
"""

import os
import sys

# print(sys.argv, len(sys.argv))


def file_search(directory, filename):
    files_list = []
    for root, dirs, files in os.walk(directory):
        if filename in files:
            # print(os.path.abspath(root) + '/' + file_name)
            files_list.append(os.path.join(root, file_name))

    return files_list


if 1 < len(sys.argv) < 4:
    local_dir = sys.argv[1]
    file_name = sys.argv[2]
    files_list = file_search(local_dir, file_name)

    if len(files_list) > 0:
        print(files_list)
    else:
        print("файлът не е намерен")

else:
    print("Usage: python test51.py <directory> <filename>")





