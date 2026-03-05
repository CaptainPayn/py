#!/usr/bin/env python3

print("Rock(r) paper(p) scissors(s)")
print("Hit enter twice key to exit")

while True:
    userA = input("Enter a letter (r, p, or s): ").lower()
    userB = input("Enter a letter (r, p, or s): ").lower()
    if userA == "" or userB == "":
        break
    if userA == "r" and userB == "s" or userA == "s" and userB == "p" or userA == "p" and userB == "r":
        print("User A wins!")
    else:
        print("User B wins!")

