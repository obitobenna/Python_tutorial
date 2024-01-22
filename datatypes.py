#  python data type
import math
name="Tobenna"
age=20
area =" anambra"

print(f"My name is{name} and i am {age} years old . And i reside in {area} \n")

print( "My name is {} and i am {} years old . And i reside in {}".format(name , age ,area ) ,end="")

b =  25
pi=math.pi
print("{:.3f}".format(pi))
print("{:.0f}" .format(math.sqrt(b)))


name_two = input("what is your name")
num =int (input("choose a number"))

#print(name_two)
print(math.sqrt(num))
print("{}" . format(name_two))
print("{}".format(math.sqrt(num)))

b = 50
c = 45

print(b == c)
print(b is c)
print(b and c)
print(b or c)


