"""Write a C program to read in two numbers, x and n, and then compute the sum of this
geometric progression: 1+x+x 2 +x 3 +………….+x n
For example: if n is 3 and x is 5, then the program computes 1+5+25+125. Print x, n, the
sum."""

x=int(input("Enter a number for x:"))
n=int(input("Enter a number for n:"))
sum=0
for i in range(0,n+1,1):
    sum=sum+(x**i)
    print("Sum of the series is:",sum)