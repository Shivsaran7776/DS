"""4)	Write a program to find the occurrence of positive, negative, even and odd elements for a given array."""

arr=[]
pos_count=0
neg_count=0
odd_count=0
even_count=0
n=int(input("\nEnter no.of elements to be presented in a array:"))
for i in range(0,n):
    arr.append(int(input("\nEnter array values:")))

for j in range(0,n):
    if arr[j]>0:
        pos_count+=1
        if arr[j]%2==0:
            even_count+=1
        elif arr[j]%2!=0:
            odd_count+=1
    else:
        if arr[j]<0:
            neg_count+=1
            if arr[j]%2==0:
                even_count+=1
            elif arr[j]%2!=0:
                odd_count+=1

print("\nPositive Count:",pos_count)
print("\nNegative Count:",neg_count)
print("\nOdd Count:",odd_count)
print("\nEven Count:",even_count)
