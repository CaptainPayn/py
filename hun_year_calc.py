#!/usr/bin/env python3
from datetime import date

name = input("Enter your name: ")
age = int(input("Enter your age: "))

years = 100 - age
current_year = date.today().year
year_hun = years + current_year

#print(f"Hello {name} you will be 100 in the year {year_hun}")

count = int(input("Enter a number: "))

while count != 0:
    print(f"Hello {name} you will be 100 in the year {year_hun}")
    count -= 1
