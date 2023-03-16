"""Write a program to find the number in between 7 and 100 which is exactly divisible by 4
and if divided by 5 and 6 remainders obtained should be 4."""

for x in range(7,101):
    if x%4==0 and x%5==4 and x%6==4:
        print(x)