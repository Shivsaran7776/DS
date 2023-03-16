"""Write a program to enter few numbers and count the positive and negative numbers
together with their sums. When 0 is entered program should be terminated."""

pos_sum=0
pos_count=0
neg_sum=0
neg_count=0
while(True):
    num=int(input("Enter a number:"))
    if num>0:
        pos_count+=1
        pos_sum+=num
        print("Positive sum count:",pos_count)
        print("Positive sum:",pos_sum)
    elif num<0:
        neg_count+=1
        neg_sum+=num
        print("Negative count:",neg_count)
        print("Negative sum:",neg_sum)
    elif num==0:
        break