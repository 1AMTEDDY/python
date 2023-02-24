#!/usr/local/bin/python3
#the famous fizzbuzz
# print the number `0 -100` but if the number is divisible by 3 print `fizz` if the number is divisible by 5 print `buzz` if the number is divisible by 3 and 5 print `fizzbuzz`. if none print the number.
import math

for num in range(0, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
