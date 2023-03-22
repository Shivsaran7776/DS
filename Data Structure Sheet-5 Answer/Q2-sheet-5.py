"""2)	Given a 2-D matrix. Write a program to print its corner elements and the sum of the corner elements. 
	Input:    
	
    6   4   6   9
    2   6   1   8
    5   5   2   2
    4   4   1   3
	Output:   Corner elements: 6 4 9 3, Corner_Sum = 22
"""
arr=[]
r=int(input("\nEnter the no.of rows to be present in array:"))
c=int(input("\nEnter the no.of columns to be present in array:"))
for i in range(0,r):
    temp=[]
    for j in range(0,c):
        temp.append(int(input("Enter row element and column element in array:")))
    arr.append(temp)
for i in range(0,r):
    for j in range(0,c):
        print(arr[i][j],end=' ')
    print()
sum=0
sum=arr[0][0]+arr[0][c-1]+arr[r-1][0]+arr[r-1][c-1]
print("\nThe Corner Sum of Element in array is:",sum)