#without structure, there's only chaos
# A data structure is a particular way of organizing data in a computer so that it can be used effectively
# A list is a a DS in python that is a mutable, or changeable, its an ORDERED sequence of elements. Each element or value in the list is called an item. lists are defined by having values in a square bracket. []
#our_list = [] #empty list
our_list = [1]
full_list = ["Peter", 24, 3.14, False]
print(full_list)
#List Referencing, starting from 0 indexing
my_name = full_list[0]
print(my_name)

pi = full_list[2]
print(pi)

full_list[2] = "pi"
print(full_list)

#printing out negative numbers prints from the back of the lists looping back one time through the list (Goes to the last item on the list basically)
#printing out False
print(full_list[-1])

#appending to the back of the lists
#First using a variable
our_list.append(full_list)
print(our_list)

full_list.append("True")
print(full_list)

#Deleting an Item in a list
#Two ways of deleting pop() or remove()
full_list.pop(-1) #this can also be used to return the value that was removed from the list
print(full_list)

full_list.remove("Peter")
print(full_list)
