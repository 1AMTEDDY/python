#!/usr/local/bin/python3
# coding sprinkles
#GOTO W3SCHOOLS STRING_METHODS
greeting = "HELLO, DEY PLAY"
name = "wetin be your name?"
divide = "Ijustdeyplayforlifesad"
sentence = "I just dey play for life sad"
tuple = ("hi", "i'm Peterson")
#this capitalizes the first letter on the string
x = name.capitalize()
print(x)
#reduces the whole thing to lowercase, can also use the method casefold
y = greeting.lower()
print(y)
#uppercase the whole thing
z = name.upper()
print(z)
#capitalizes the first letter of each word as a title
a = greeting.title()
print(a)
#split up a string based on a char you pass in and gives you a list, if you dont then it splits everything,
b = sentence.split()#"play")
print(b)
#this works too and excludes play
c = divide.split("play")
print(c)
#this ones funny it concats strings by appending "i" in the empty space between each declared strings
d = "i".join(tuple)
print(d)
#laptops = [ 'mac', 'hp', 'lenovo' ]
#cars=[ 'nord', 'toyota', 'lambotruck' ]
#laptops_cars = laptops.extend(cars)
#print (laptops_cars)
