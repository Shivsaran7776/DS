#Write a program to check whether the voter is eligible for voting or not. If his/her age is
#equal to or greater than 18.Display message “Eligible” otherwise “Non-Eligible”.

age=int(input("Enter your age"))
if age>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible to vote")