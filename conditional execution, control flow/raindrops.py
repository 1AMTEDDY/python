#!/usr/local/bin/python3
import math
#pling, plang, plong

for num in range(0, 100):
    if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
        print("PlingPlangPlong")
    elif num % 3 == 0 and num % 5 == 0:
        print("PlingPlang")
    elif num % 3 == 0 and num % 7 == 0:
        print("PlingPlong")
    elif num % 5 == 0 and num % 7 == 0:
        print("PlangPlong")
    elif num % 3 == 0:
        print("Pling")
    elif num % 5 == 0:
        print("Plang")
    elif num % 7 == 0:
        print("Plong")
    else:
        print(num)
