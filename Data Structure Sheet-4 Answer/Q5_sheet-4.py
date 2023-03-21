"""5)	In a gymnastics or diving competition, a contestants score is calculated by dropping the lowest and highest scores and
 then adding the remaining scores. Write a program that allows the user to enter eight judges scores and then outputs the point 
 received by the contestant. A judge awards point between 1 and 10, with 1 being the lowest and 10 being the highest. For example, 
 if the scores are: 9.2, 9.3, 9.0, 9.9, 9.5, 9.5, 9.6 and 9.8, then the contestant receives a total of 56.9 points.

Here is the sample output.

Enter 8 scores out of ten points :
9.1  9.0  8.9  8.8  9.4  7.9  8.6  9.8
Your lowest score is 7.90
Your maximum score is 9.80
Your total point is 53.80
Your average point is 8.97
"""

judges=int(input("\nEnter the no.of judges present in competition:"))
points=[]
for i in range(1,judges+1):
    points.append(float(input("\nEnter the judge {} score for the contestant:".format(i))))
print("Points alloted by judges to the contestant:",points)
max_point=points[0]
low_point=points[0]
total=0
for j in range(0,judges):
    total+=points[j]
    avg=total/judges
    if points[j]>max_point:
        max_point=points[j]
    elif points[j]<low_point:
        low_point=points[j]
print("\nYour lowest score is ",low_point)
print("\nYour maximum score is ",max_point)
print("\nYour total point is ",total)
print("\nYour average point is ",avg)    