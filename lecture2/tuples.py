#!/usr/bin/env python3

var0 = 4, 5, 6
var = (1, 2, 'Test')

print(var0)
print(var.__class__)
print(var)

print(var[1])
print(var[1:2])
# tuples does not allow changing the content
# var[1] = 1213
# print(var)
#
#
print(var.index('Test'))
print(var.count(1))

a = 1
b = 20
# unpacking b, a on the right side to tuple on the left side: a, b
a, b = b, a
print(a, b)


l1 = list(var0)
print(l1)
t1 = tuple(l1)
print(t1)
