"""Write a program to accept a string and a width. Wrap the string into a paragraph of width w.
Sample Input 
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

string=input("Enter a string:")
width=int(input("Enter the number of letter to be present each line from the string:"))
length=len(string)
print(length)
print(width)
for i in range(0,length):
    if((i+1)%width==0):
        print(string[i],end="")
        print()
    else:
        print(string[i],end="")
    