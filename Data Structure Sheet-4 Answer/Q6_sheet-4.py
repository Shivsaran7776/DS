"""6)	Write a program that accepts an array and a key value. Rotate the array element by ‘key’ times.
Example:
		Input:  arr[]= [1, 2, 3, 4, 5, 6]

		key=2

		Output : [ 3, 4, 5, 6, 1, 2]

"""
arr=[]
temp=0
key=int(input("\nEnter no.of times to done:"))
val=int(input("\nEnter the no. to enter in array:"))
for i in range(0,val):
    arr.append(int(input("\nEnter array values:")))
print("The array values you entered is:",arr)
while(key>0):
    arr.append(arr[0])
    arr.pop(0)
    key-=1
    print(arr)



