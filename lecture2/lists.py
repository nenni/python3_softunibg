
l = list(range(10))

print(l)

l.append(11)

# for idx, value in enumerate(l):
#     print(idx, "-", value)
#


long_text = '''Стандартни операции
... познати от почти всеки език за програмиране:
индексиран достъп до елементите - values[2] # == 'dve',
като индексите започват от 0
'''


# print(long_text)
#
# print(long_text.split())
# print(len(long_text.split()))
#
# print(long_text.split('\n'))
# print(len(long_text.split('\n')))

words = long_text.split()
for word in words:
    print(len(word))


# TypeError: can only concatenate list (not "str") to list
# greshno dobavqne na string kam list
# izpolzva se append method
# print(long_text.split() + 'drugo')
words.append('drugo')
print(words)

#sabirane na 2 lista

words = words + ['drugo2']

print(words)


for i, w in enumerate(words):
    print(i, " - ", w)

# insert -1 vmakva element na posledna pozicia na sashtesvuvashtiq list
# i otmestme posledniq, t.e. vmakva na predposledno mqsto s -1
words.insert(-1,'a')

print(words)

# pop vadi element ot lista
print(words.pop(2))
print(words)

print('почти' in words)
print('почти' not in words)
print(words.index('drugo'))


print(words[1:])
print(words[1:4])
print(words[:4])
#pri greshen index (200) vrashta prazen list
print(words[200:4])

# slicing ne garmi s greshka
words2 = ['test1', 'test2']
print(words2[:4])


#slicing prez edin elemet
print(words)
print(words[1::2])
print(words[1::3])
print(words[1::-1])
#obrashtane na elememti v list
print(words[::-1])
# obrashta sashtesvuvashtiqt list, s methoda reverse()
words.reverse()
print(words)


words.sort()
print(words)
