print("hi world")
#code print's ("hi world")

print(2)
#print's the number 2

print(type(5))
#print's the class

#Setup variables
name = "Peterson"
age = 24
level = 300
Job = "DevOps"
man = True
vars = {name,age,level,Job,man}
print(vars)
print(type(man))

#string concatenation
print("Hi, I'm Peterson!," + " i am a Devops Engineer" + " learning Python")
print("hi i'm" +  name + " I am a DevOps Engineer" + " 24 years old")

#string interpolation add the f and parentheses to the code or use the .format method or you string coerce
#this is the process of substituting the values of the variables into placeholder strings.
print(f"Hi, name's {name} i'm {age} in {level} working as a {Job} Engineer and i'm a man that is {man}")
#or
print("Hi, name's {} i'm {} in {} working as a {} Engineer and i'm a man that is {}".format(name, age, level, Job, man))
#or
bio = ("hi, i am " + name + ", work as " + Job + " Engineer i'm " + str(age) + " also a man that is ", bool(man))
print(bio)

#inputs to get output

age = input("What's your age?: ")
name = input("What's your name?: ")
bio = ("you are {} by name and you are {} by age".format(name, age))
print(bio)

