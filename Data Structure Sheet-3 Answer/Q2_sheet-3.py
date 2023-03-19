"""2)	Write a program to accept a string and perform the following operations without using any string functions:
a.     Print the length of the string
b.     Print the reverse of the string
c.     Copy the string to another new string
"""

string1=input("Enter a string:")
print("Length of the string:",len(string1))
length=len(string1)
for i in range(length-1,-1,-1):
    print("Reverse of the string:",string1[i])
string2=string1
print("The value of the other string is:",string2)
