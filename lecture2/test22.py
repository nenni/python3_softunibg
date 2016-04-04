#!/usr/bin/env python3

user_inp_1 = input("text 1: ")
user_inp_2 = input("text 2: ")

idx = user_inp_1.find(user_inp_2)

if idx == -1:
    print("user2 input not found in user1 input")
else:
    print("Result: " + user_inp_1[idx + len(user_inp_2):])

