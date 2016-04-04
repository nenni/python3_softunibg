import os

print(os.access('/etc/hosts', os.R_OK))
print(os.access('/etc/hosts', os.W_OK))


if os.access('/etc/hosts', os.W_OK):
    print("Не би трябвало да можете да пишете в този файл")
elif os.access('/etc/hosts', os.R_OK):
    print("Можете да прочетете списъка с потребителите.")


print(os.path.getsize('./py_os_module.py'))

print(os.path.isfile('./py_os_module.py'))
print(os.path.isdir('./py_os_module.py'))
print(os.path.exists('./py_os_module.py'))

print(os.path.dirname('./py_os_module.py'))
print(os.path.dirname('./'))

print(os.path.abspath('./py_os_module.py'))

print(os.path.dirname(os.path.abspath('./py_os_module.py')))


for i in os.walk('../'):
    print(i)

for root, dirs, files in os.walk('../'):
    print(root, '---', dirs, '---', files)