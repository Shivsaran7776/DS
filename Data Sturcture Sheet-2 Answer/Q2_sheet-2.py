"""2.	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
 The sum of these multiples is 23. Write a program to find the sum of all the multiples of 3 or 5 below 1000. 
Hint: Be careful not to add two times a number which is multiple of both 3 and 5.
"""
sum=0
num=int(input("Enter a number for iterations:"))
for i in range(1,num,1):
    if (i%3==0 or i%5==0):
        sum=sum+i
    #else:
        #continue

print("Sum of the series is:",sum)