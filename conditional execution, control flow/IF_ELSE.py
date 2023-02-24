#!/usr/local/bin/python3
fav_color = input("What is your favorite color?: ")

#after writing if you have to refer the conditioner(variable) and then write the condition
if fav_color == "red":
    print("That's not my Favorite color!")
elif len(fav_color) == 3:
    print("That's my favorite color!")

if fav_color == "yellow":
    print("That's still not my favorite color too!")
else: print("i hate these colors")
#elif has only one match, if you have multiple matches it will only print the first one.
# in other languages there are switch/case statements
