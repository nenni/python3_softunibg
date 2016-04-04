#!/usr/bin/env python3 -tt

import sys
import csv


TEMP_DIFF = 4.0


def main():
    try:

        # input_file = 't.txt'
        input_file = input()
        last_temp = None

        # Solution 1
        # date_temp = _load_temp(input_file)
        #
        # for datetime_str, temp in date_temp:
        #     if last_temp:
        #         if temp - last_temp > TEMP_DIFF:
        #             print(datetime_str)
        #     last_temp = temp

        # Solution 2
        for datetime_str, temp in _load_temp_generator(input_file):
            if last_temp:
                if temp - last_temp > TEMP_DIFF:
                    print(datetime_str)
            last_temp = temp

        return 0

    except Exception as e:
        # print("INVALID INPUT", str(e))
        print("INVALID INPUT")
        return 1


def _load_temp(input_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        # print(list(reader))

        result = []
        for row in reader:
            if len(row) != 2:
                raise ValueError("incorrect line in file")

            result.append(
                (row[0], float(row[1]))
            )
        # print(result)
        return result


def _load_temp_generator(input_file):
    with open(input_file) as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) != 2:
                raise ValueError("incorrect line in file")

            yield (row[0], float(row[1]))


if __name__ == '__main__':
    sys.exit(main())
