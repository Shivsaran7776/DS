"""1)	Write a program to accept the integer values and display the second largest value in an array."""

arr=[]
num=int(input("\nEnter the number of element to be inserted in array:"))
for i in range(0,num):
    arr.append(int(input("\nEnter array values:")))
print(arr)
brr=[]
while (arr):
    minimum=arr[0]
    for x in arr:
        if x < minimum:
            minimum=x
    brr.append(minimum)
    arr.remove(minimum)
print(brr)
print("The second largest number is:",brr[-2])
