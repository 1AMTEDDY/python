#!/usr/local/bin/python3
#they return a boolean value
# == equality
# != Inequality
# > Greater Than
# < Less Than
# >= Greater Than Equal to
# <= Less Than/Equal

print(5 == 5)
print(5 != 5)
print(5 != 6)
print(6 > 5)
print(5 == 5.0)
print(5 == '5') #does some type checking
print('Hello' == 'Hello')
print('Hello' == 'hello') # would return false
print(5 > len('five')) # you can also typecast
print(5 < 6)
print(5 >= 6) # would return false, if one condition returns true the whole thing is true
print(5 >= 5) # returns true
print("hello" * 3) # returns hellohellohello

