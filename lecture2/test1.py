
user_input = input("Въдедете текст: ")

if len(user_input) < 10:
    print(user_input)
else:
    print("Изход:" + user_input[:10] + "...")
