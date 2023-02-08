#A sequence of immutable python objects. are sequences, just like lists. The difference is: tuples cant be changed and they use parenthesis (), while lists can be changed and use square brackets []
#ListsYouCantChange
tuple = () #empty tuple, dont do this!
print(type(tuple))

x = ('Hello', 21, 'can you do sum for me?')
print(x)
x[1] = (4) #immutable so cant be changed``
del x #throw the whole thing away

