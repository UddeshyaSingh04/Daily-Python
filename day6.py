#  we are going to write a program that generate a random number and ask user to guess the it.

import random 
n = random.randint(1,100)
a = -1
gusses = 1
while(a!=n):
    gusses += 1
    a = int(input("Guess the number:"))
    if(a>n):
        print("lower number please")

    else:
       print("higher number please")

print(f"you guesses the correct {n} number in {gusses} attempt")
