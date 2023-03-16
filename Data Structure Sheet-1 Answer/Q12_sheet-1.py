"""2.	Print a pattern of numbers from 1 to n as shown below. Each of the numbers is separated by a single space.								(HackerRank)
Input Format: The input will contain a single integer n.
Constraints: 1<=n<=1000
Sample Input 
5
Sample Output
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5
"""
MAX = 100
  
def prints(a, size): 
    for i in range(size): 
        for j in range(size):
            print(a[i][j], end = '')
        print()

def innerPattern(n): 
       
    size = 2 * n - 1
    front = 0
    back = size - 1
    a = [[0 for i in range(MAX)]  
            for i in range(MAX)]
    while (n != 0): 
        for i in range(front, back + 1):
            for j in range(front, back + 1):
                if (i == front or i == back or
                    j == front or j == back):
                    a[i][j] = n
        front += 1
        back -= 1
        n -= 1
    prints(a, size); 
  
n = 4 
innerPattern(n)
