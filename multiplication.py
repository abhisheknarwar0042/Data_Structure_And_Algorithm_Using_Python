#. Write a program to print the multiplication table of a number entered by the user

class Solution:
    def multiplication(self,number):
        for i in range(1,11):
            print (number*i)
number=int(input())
s=Solution()
s.multiplication(number)
            
            
            

