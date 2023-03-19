"""4)	Write a program that replaces two or more consecutive blanks in a string by a single blank. 
Sample Input
You                      are                     interested   in         programming
Sample Output 
You are interested in programming
"""

string=input("Enter the string:")
sentence=''
for i in range(0,len(string)):
    if not(string[i]==' ' and string[i-1]==' '):
        sentence=sentence+string[i]
        

print(sentence)

