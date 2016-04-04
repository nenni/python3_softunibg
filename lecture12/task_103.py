#!/usr/bin/env python3 -tt

import sys
import math


def main():
    try:
        # input_w = float(4)
        # input_h = float(3)
        input_w = float(input())
        input_h = float(input())
        # spray capacity 1.76 m2
        spray_capacity = float(1.76)

        area = input_h * input_w
        spray_num = area / spray_capacity
        print(math.ceil(spray_num))
        return 0

    except Exception as e:
        print("INVALID INPUT")
        return 1


if __name__ == '__main__':
    sys.exit(main())
