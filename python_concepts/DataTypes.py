#Typecasting interpret this as whatever type you define
int("5")

answers = input("pick a number:")
print(answers)
print(type(answers))
print(10 * int(answers))

if int(answers) == 5:
    print("You win!")
else: print("You lose!")



