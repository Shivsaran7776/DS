#Write a program to calculate the telephone bill. Read the total number of phone calls made
#and calculate the total charges as per the following rates given below.
#Telephone      Call Rate per call
#<100           Rs 50 (Fixed)
#>99 and <200   Rs1
#>199 and <300  Rs2
#<299 Rs3

p_calls=int(input("Enter the no.of phone calls for telephone bill:"))
if p_calls<100:
    print("Rs 50")
elif p_calls>99 and p_calls<200:
    print("Rs ",50+(p_calls+1))
elif p_calls>199 and p_calls<300:
    print("Rs ",50+(p_calls*2))
elif p_calls<299:
    print("Rs ",50+(p_calls*3))
