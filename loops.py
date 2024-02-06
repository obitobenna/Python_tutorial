for i in range (11):
    print(i)

"""i = 0
while i <= 10:
    print(i)
    i += 1
"""

user_limit = int(input("what is the limit?"))
sum =0  

for i in range(1, user_limit):
    if i % 2 == 0:
        sum += i

print(sum)    







user_integer =int(input("what is the number "))
user_stop =int(input("Enter the range"))

for i in range (1, user_stop+1):
    x = user_integer
    y = user_stop
    result = x * i
    print(f"{x} * {i} = {result}" )




while True:
    num =int(input("what is ur number"))
    if num == 0:
        print("Existing the program ...")
        break
    elif num % 2 ==0:
        print ("{} is an even number" .format(num))    
    else:
        print("{} is an odd number" .format(num))    

    


