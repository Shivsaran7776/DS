  ###A Pen stand can hold only five pens. Ask the user how many pens he would like to put in 
  ###the pen stand. Write a program to print the message “PEN STAND IS FULL” if it exceeds 5 pens.

pen=int(input("Enter the no. of pen required to filled in the pen stand"))
if pen>5:
    print("The penstand maximum capacity is 5 pens you have entered beyond 5 pen value")
elif pen<=5:
    print("You can enter more no. of pens in penstand")