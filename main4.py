import time
name = input("What is your Name?")
num1 = int(input(f"Hello, {name} Pick a number!"))
num2 = int(input("Pick another number!"))
sum = num1 + num2
difference = num1 - num2
# check if the difference is less than 0 so I can change  the difference into positive
if difference < 0:
    difference = num2 - num1
    print (f"\n{num1} + {num2} = {sum}")
    print (f"\nThe difference between {num1} and {num2} is {difference}.")
    time.sleep(1) 
else:
    print (f"\n{num1} + {num2} = {sum}")
    print (f"\nThe difference between {num1} and {num2} is {difference}.")
    time.sleep(1)
print (f"\n{num1} x {num2} = {num2 * num1}")
time.sleep(1) 
print (f"\n{num1} ÷ {num2} = {num1 / num2}\n\n")
#The code below makes the division not end in decimal

# Write the code to find the power of the number
print (num1**num2)
print (f"\n{num1} ÷ {num2} = {num1 // num2} ")
print (f"\n{num1} ÷ {num2} = {int(num1 / num2)} ")
# This code below is for the remainder
print (f"remainder {num2 % num1}")