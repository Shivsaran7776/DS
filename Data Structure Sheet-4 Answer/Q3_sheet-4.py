"""3)	Write a program to search for a specified number in an array and display with its position."""

arr=[]
n=int(input("\nEnter the no.of element to be present in array:"))
for i in range(0,n):
    arr.append(int(input("\nEnter array elements:")))
print(arr)
val=int(input("\nEnter the element that you want to search in array:"))
for j in range(0,n):
    if arr[j]==val:
        print("The index element in array that you are searching is:",j+1)
