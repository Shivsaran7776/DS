# 2)	Write a program to sort the list of numbers in an ascending and descending order.

num=int(input("\nEnter the number of element to be present in array:"))
arr=[]
for i in range(0,num):
    arr.append(int(input("\nEnter array values:")))
print(arr)
brr=[]
while(arr):
    minimum=arr[0]
    for j in arr:
        if j<=minimum:
            minimum=j
    brr.append(minimum)
    arr.remove(minimum)
print("Ascending order of the array:",brr)
crr=[]
for j in range(len(brr)-1,-1,-1):
    crr.append(brr[j])
print("\nDescending order of the array:",crr)

