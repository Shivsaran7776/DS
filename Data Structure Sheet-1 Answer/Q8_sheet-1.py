"""
Write a program to print the entered number in the reversed order. Also perform sum and
multiplication with their digits.
"""

num=int(input("Enter a number:"))
sum=0
mul=1
for i in range(num,0,-1):
    sum=sum+i
    mul=mul*i
    print("\nThe reverse order of the number is:",i)
print("The reverse order of the addition of the value:",sum)
print("The reverse order of multiplication of the value:",mul) 