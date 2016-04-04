#!/usr/bin/env python3 -tt

import sys
import csv


def main():
    try:
        file_input = input()
        # file_input = 'data301/301-1-distances.txt'
        # file_input = 'data301/301-2-distances.txt'
        with open(file_input, encoding='utf-8') as f:
            input_data = csv.reader(f)
            hours = 0
            for row in input_data:
                if len(row) == 3:
                    start_km = int(row[0])
                    end_km = int(row[1])
                    limit_kmph = int(row[2])
                    distance = (end_km - start_km) + 1
                    hours += (distance / limit_kmph)

            print("{hours:.2f}".format(hours=hours))
        return 0
    except Exception as e:
        print("INVALID INPUT")
        return 1


if __name__ == "__main__":
    sys.exit(main())


