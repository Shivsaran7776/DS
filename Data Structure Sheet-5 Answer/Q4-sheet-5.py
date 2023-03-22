"""4)	Given a string, eliminate all “b” and “ac” in the string, you have to replace them in-place, and you are only allowed to iterate
over the string once.
Examples: 
		acbac   ==>  ""
		aaac    ==>  aa
		ababac  ==>   aa
		bbbbd   ==>   d	
"""
string1=input("\nEnter your string:")
string2=input("\nEnter the elements that you want to insert the 1st string:")
string3=input("\nEnter the elements that you want to remove from 1st string:")
new=string1.replace(string3,string2)
print(new)
