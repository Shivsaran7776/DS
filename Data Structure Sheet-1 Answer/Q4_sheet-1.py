"""
4)	A Student studying in an institution is examined by course work and written examination. Both components of the assessment
   carry a maximum of 50 marks. The following rules are applied by the examiner in order to determine whether a student passes or fails:
i) A student must secure a total of 45% or more in order to pass.
ii) A total mark of 44% is moderate to 45% however.
iii) Each component must be passed with minimum of 20 out of 50.
iv) If a student scores 45% or more but does not achieve the minimum mark in one component he is failed with 44% which is moderated to 45%.
    Write a program to input the marks for each component and output the final mark along with the result.
"""

mark1=int(input("Enter the mark 1:"))
mark2=int(input("Enter the mark 2:"))
tot=mark1+mark2
if tot>=40:
    if mark1>=20 and mark2>=20:
        print("You are passed")
    else:
        print("You are failed")