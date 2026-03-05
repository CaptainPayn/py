#!/usr/bin/env python3

userInput = int(input("Enter a number: "))

for i in range(1, userInput + 1):
    if userInput  % i == 0:
        print(i)
