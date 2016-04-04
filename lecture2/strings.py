

print('adsasfasqqewfqwf')

name = 'ivan'
surname = 'petrov'

print(len(name))


print(name + ' ' + surname)

for ch in name:
    print(ch, end='')

# string moge da se polzva i kato list ot char
print('')
print(name[0])

# stringovete imat methodi
# string method-a find vrashta index-a kadeto e nameren stringa,
#  kojto tarsim v stringa, ako ne nameri stringa vrashta -1
print(name.find('va'))
print(name.find('tamta'))

# format() preferred for formatting strings
a = '{0} is {1} and likes {2} ---- escape na \ $#@!%{{ {{2}} ----- {name}'
b = a.format('ivan', 18, 'beer', name='Nikolay')

print(b)

print('PI is {:.4}'.format(3.14150))
print('PI is {:.7}'.format('test12345'))
