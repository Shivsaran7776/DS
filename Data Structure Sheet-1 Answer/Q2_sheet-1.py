#Write a program to check whether the blood donor is eligible or not for donating blood.The
#conditions laid down are as under.
# Age should be greater than 18 years but not more than 55 years.
# Weight should be more than 45 kg.

age=int(input("Enter your age:"))
weight=int(input("enter your weight in kgs:"))
if (age>18 and age<=55):
    if (weight>=45):
        print("You are eligible for blood donation")
else:
    print("Your are not eligible for blood donation")