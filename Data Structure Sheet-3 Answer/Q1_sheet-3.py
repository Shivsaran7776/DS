"""1)	Write a program to accept your name and count the number of vowels in it.
Sample Input: Alice
Sample Output:  3 
"""

name=input("Enter your name:")
count=0
for i in range(0,len(name)):
    if (name[i]=='A' or name[i]=='a'):
        print(name[i])
        count+=1
        print("Vowel count:",count)
    if(name[i]=='E' or name[i]=='e'):
        print(name[i])
        count+=1
        print("Vowel count:",count)
    if(name[i]=='I' or name[i]=='i'):
        print(name[i])
        count+=1
        print("Vowel count:",count)
    if(name[i]=='O' or name[i]=='o'):
        print(name[i])
        count+=1
        print("Vowel count:",count)
    if(name[i]=='U' or name[i]=='u'):
        print(name[i])
        count+=1
        print("Vowel count:",count)
            