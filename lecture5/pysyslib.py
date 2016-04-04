#!/usr/bin/env python3 -tt

import sys


print("-"*30)
print(sys.platform)
# print(sys.path)

# positional arguments
print(sys.argv)
for i in sys.argv:
    print(i)
print(sys.argv[0])



