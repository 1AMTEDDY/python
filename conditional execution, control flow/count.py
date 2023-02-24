#!/usr/local/bin/python3
#a loop statement that prints out the numbers 0 to 100,
#there is cases you can get a off by one error, you can make the while counter <= 100 to while counter < 101 to fix it or you make the while counter < 100 to while counter <= 100 to fix it
counter = 0
while counter <= 100:
    if counter % 15 == 0: #i'd think put the most specific condition first. if statements when matched will stop running the rest of the if statements.
        print("fizzbuzz")
    elif counter % 3 == 0:
        print("fizz")
    elif counter % 5 == 0:
        print("buzz")
    else:
       print(counter)
    counter += 1 #this assigns the value of counter + 1 to counter, so when the loop runs again, it will be 1 higher than the previous time
    #counter = counter + 1 #this is the same as the above line, it assigns the value of counter + 1 to counter, so when the loop runs again, it will be 1 higher than the previous time
