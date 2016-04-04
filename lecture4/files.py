
# opening file and reading line by line

# First method of opening files in python, which DOES NOT guaranty that the file will be closed
# closing the file with close() explicitly

f = open('task2.log')

try:
    for line in f:
        print(line.rstrip())

    # for idx, line in enumerate(f):
    #     print(idx, ' ', line.rstrip())
    #     # 1/0 # dori i pri exception fila shte se zatvori v finally block-a
finally:
    f.close()
    print("file closed", f.name)
    print("-"*70)


# Second method of opening files in python, which guaranties that the file will be closed
with open('task2.log') as f:
    for idx, line in enumerate(f):
        print(idx, ' ', line.rstrip())


# Reading files
with open('task2.log') as f:
    # reads the whole file, not recommended. File can be big
    contents = f.read() # !!!!!
    print(contents)


with open('task2.log') as f:
    # read lines, not recommended. File can be big.
    # Returns list/array, each list element contains a line from the file
    contents = f.readlines() # !!!!!!!!!
    print(contents)

with open('task2.log') as f:
    # Reads single line
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

"""
Open text files - read only mode, open second argument 'r' or empty (default is read-only)
e.g.: with open('task2.log', 'r') as f:
Open text file - write mode 'w', write mode deletes the content of the file
e.g.: with open('task2.log', 'w') as f:
Open text files - append mode
e.g.: with open('task2.log', 'a') as f:
Open binary files - rb or wb
"""


with open('textfile.txt','a') as f:
    for i in range(10):
        f.write(str(i))
        # f.write('\n')
        # f.write('{}\n'.format(i))
    f.write('\n')
    f.write('{}'.format('\n'))


# writelines, takes the list and writes each element on the new line
with open('textfile2.txt', 'w') as f:
    lines = [str(i) + '\n' for i in range(20)]
    print(lines)
    f.writelines(lines)


