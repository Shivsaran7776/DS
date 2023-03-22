"""1)	Sparse matrix is a special matrix with most of its elements are zero. Assume that if     (m * n) / 2 elements are zero then it is a sparse matrix. Write a C program to read elements in a matrix and check whether matrix is Sparse matrix or not.
Example
Input
		Input elements in matrix: 
		1 0 3
		0 0 4
		6 0 0
Output
		The given matrix is Sparse matrix
"""
arr=[]
r=int(input("\nEnter the row size of array:"))
c=int(input("\nEnter the column size of array:"))
print("\nEnter sparse matrix values")
for i in range(0,r):
    temp=[]
    for j in range(0,c):
        temp.append(int(input("\nEnter array value:")))
    arr.append(temp)
for i in range(0,r):
    for j in range(0,c):
        print(arr[i][j],end=" ")
    print()
count=0
val=r+c-1
num=0
for i in range(0,r):
    for j in range(0,c):
        if arr[i][j]==num:
            count+=1
if count>=val:
    print("\nIt is a Sparse Matrix")
else:
    print("\nIt is not Sparse Matrix")

