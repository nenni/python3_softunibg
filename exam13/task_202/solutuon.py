#!/usr/bin/env python3 -tt

import sys


def main():

    try:

        X = 0
        Y = 0

        with open('202_2.txt', encoding='utf-8') as f:

            for line in f:
                strip_line = line.strip()
                if strip_line:
                    line_list = strip_line.split()
                    direction = line_list[0]
                    step = float(line_list[1])

                    if direction == 'up':
                        Y += step
                    elif direction == 'down':
                        Y -= step
                    elif direction == 'right':
                        X += step
                    elif direction == 'left':
                        X -= step

            if X != 0 and Y != 0:
                print("X {:.3f}".format(X))
                print("Y {:.3f}".format(Y))
            else:
                raise ValueError

        return 0
    except Exception as e:
        print("INVALID INPUT", str(e))

if __name__ == '__main__':
    sys.exit(main())
