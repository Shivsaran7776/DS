"""3.	Write while loops to do the following: 
 *Repeatedly print the value of the variable xValue, decreasing it by 0.5 each time, as long as      xValue remains positive.
 *Print the square roots of the first 25 odd positive integers
"""
num=int(input("Enter a number:"))
while(True):
    if(num>=0):
        print(num)
        num-=0.5
        if(num==0):
            break

print()
print()
num=int(input("Enter a number:"))
for i in range(1,num+1,1):
    print("The square root of the number",i,"is",i*i)