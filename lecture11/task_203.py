#!/usr/bin/env python3 -tt

import sys
import csv
import os


def main():
    try:
        # in_w = 1.17
        # in_h = 0.70
        # in_d = 0.50
        in_w = float(input())
        in_h = float(input())
        in_d = float(input())
        dimensions = [in_h, in_w, in_d]
        dimensions.sort(reverse=True)
        # file_input = './data203/packages_judge.txt'
        file_input = input()

        if os.access(file_input, os.R_OK) or not os.path.isfile(file_input):
            with open(file_input, encoding='utf-8') as f:
                input_data = csv.reader(f)
                for row in input_data:
                    if len(row) == 4:
                        medicine_name = row[0]
                        medicine_w = float(row[1])
                        medicine_h = float(row[2])
                        medicine_d = float(row[3])
                        dimensions_medicine = [medicine_w, medicine_h, medicine_d]
                        dimensions_medicine.sort(reverse=True)

                        if dimensions[0] >= dimensions_medicine[0] and dimensions[1] >= dimensions_medicine[1] and \
                                        dimensions[2] >= dimensions_medicine[2]:
                            print("{name}".format(name=medicine_name))
                return 0

    except Exception as e:
        print("INVALID INPUT")
        return 1


if __name__ == "__main__":
    sys.exit(main())


