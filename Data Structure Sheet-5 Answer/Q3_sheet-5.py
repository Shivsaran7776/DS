"""3)	Write a program to check whether two given strings are anagram of each other or not. An anagram of a string
 is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc”
  are anagram of each other."""

string1=input("\nEnter 1st string:")
string2=input("\nEnter 2nd string:")
len1=len(string1)
len2=len(string2)
count=0
if len1==len2:
    print("\nBoth String length are equal")
else:
    print("\nString Length is not equal")
    exit(0)
for i in range(0,len1):
    for j in range(0,len2):
        if string1[i]==string2[j]:
            string2=string2.replace(string2[j],'$',1)
            count+=1
            print(string2)
if(count==len1):
    print("\nIt is Anagram")
else:
    print("\nIt is not a Anagram")

            