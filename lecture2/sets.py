#!/usr/bin/env python3 -tt


set0 = {0,1,2,3}
#  function set( accepts list or tuple)
set1 = set((1,2,3,4,79))
set2 = set([2,6,7,9,0,10])

print(set0)
print(set1)
print(set2)

#empty set
set_empty = set()
print(set_empty)

#empty set is boolean False
if set_empty:
    print(True)
else:
    print(False)

# for i in enumerate(set1):
#     print (i.__class__, i)

set1 = set(range(10))
set2 = set(range(6,16))
print(set1)
print(set2)

#union
print(set1 | set2)
print(set1.union(set2))

#intersection
print(set1 & set2)
print(set1.intersection(set2))


set1.add(110)
print(set1)
set1.remove(110)
print(set1)




