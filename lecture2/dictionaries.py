#!/usr/bin/env python3

# create dict
# w = dict()
# preferred
weather = {}
weather = {
    'sofia': 2,
    'varna': 10,
    'burgas': 13,
}

# len of the key from the dictionary
print(len(weather))

# print content
print(weather)

# delete key:value pair
del weather['sofia']

print(weather)

# search if key is part of the dict, returns TRUE or FALSE
# in or not in
print('Is varna in dict: ', 'varna'in weather)
print('Is Varna in dict: ', 'Varna'.lower() in weather)
print('Is Sofia in dict:', 'sofia' in weather)

# get value from the dict[key]
print(weather['varna'])
print(weather.get('burgas'))
# if key does not exist, get() returns None
print(weather.get('burgasY'))
# if key does not exist, and second/default parameter is passed to get() function, default value is returned
print(weather.get('burgasY','default=Nikolay'))

# inserting new key:value pair in dict

weather['ruse'] = '40'
# get all the keys
print(weather.keys())

# get all the values
print(weather.values())

#
# iterate dictionary
#
# returns keys
for key in weather:
    print(key, end='')
    print(weather[key])

# dict.items() returns tuples,
# can be unpacked with for loop to key and value keywords directly
for key, value in weather.items():
    print(key)
    print(value)

for value in weather.items():
    print(value, end='')
    print(value.__class__)

# clear/empty dictionary
weather.clear()
print("Empty dict: ", weather)



