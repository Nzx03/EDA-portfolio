class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
         first=0
         second=1
         z=[first,second]
         if n==1:
                print(z[0])
         elif n==2:
                print(z)
         elif n==0:
                print("")
         else:
                for i in range(n-2):
                    third=first+second
                    z.append(third)
                    # if i ==n-3:
                    print(z)
                    first=second
                    second=third
s=Solution()
try:
    n=int(input("Enter the value of n:"))
    s.fibonacciNumbers(n)

except ValueError:
    print("enter valid number")