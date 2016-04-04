#!/usr/bin/env python3 -tt

import sys
import math

LOSS = 1 + 9.8/100

def main():

    try:
        sheet_area = float(input())
        box_a = float(input())
        box_b = float(input())
        box_c = float(input())

        # sheet_area = 0.80
        # box_a = 1.23
        # box_b = 0.78
        # box_c = 0.50
        box_area = 2*(box_a*box_b + box_a*box_c + box_b*box_c)
        num_sheets = (box_area*LOSS) / sheet_area

        print("{}".format(math.ceil(num_sheets)))

        return 0

    except Exception as e:
        print("INVALID INPUT")
        return 1

if __name__ == '__main__':
    sys.exit(main())
