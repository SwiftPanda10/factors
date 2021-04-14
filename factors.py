# Author: Samuel Bennett
# Date: 4/14/2021
# Description: Prints all positive integers that divide evenly into a user entered number

integer = int(input("Please enter a positive integer: "))

print("The factors of", integer, "are: ")

for i in range(1,integer+1) :
    if integer%i==0 :
        print(i)

