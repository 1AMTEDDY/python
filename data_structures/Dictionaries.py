#!/usr/local/bin/python3
#Key-Value Store
#An unordered collection of data values, used to store data values like a map. uses 'key':value separated by a comma for the next key-value
#our_dict = {} empty dictionary

x = {'name':'Peter', 'age':2}
print(type(x))
print(x)


#You reference the item by ONLY its key not by its index, because they are unordered
print(x['name'])

#Changing an item in the dictionary with its key, because its not static typed you can change to diff data type
x['age'] = 4
print(x)
#Same dictionary diff values

#Appending you set it like a variable
x['height'] = r"4'7"  #or '6\'7' for making a literal string
print(x)

#delete a key-value
del x['name']
print(x)

#Example
Address = {'house_number':3, 'street_name':'akoka', 'city':'shomolu', 'state':'lagos'}
print(Address)

Address['zip_code'] = '1100001'
print(Address)
