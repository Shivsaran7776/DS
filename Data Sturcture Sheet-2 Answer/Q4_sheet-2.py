"""4.	Write  a program to print the following
        1
       222
      33333
     4444444
    555555555		        
       
       1
      212
     32123
    4321234
   543212345

Challenging Question (CodeChef)		
"""

num=int(input("Enter a number:"))
for i in range(1,num+1,1):
    for s in range(num,i,-1):
        print(" ",end=" ")
    for j in range(0,(i+i)-1,1):
        print(i,end=" ")
    print()

print()
print()

num=int(input("Enter a number:"))
for i in range(1,num+1,1):
    for s in range(num,i,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for k in range(2,i+1):
           print(k,end=" ")
    print()
