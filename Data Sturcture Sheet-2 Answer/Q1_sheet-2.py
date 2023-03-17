"""Write a program to keep asking for a number less than 100 and stop when the
number is multiple of 3, 5, and 7."""

while(True):
    num=int(input("Enter a number within 100:"))
    if num<=100:
        print(num)
        if num%3==0 or num%5==0 or num%7==0:
            break
print("If the entered number is divisible by 3,5 and 7 the loop while be terminated")