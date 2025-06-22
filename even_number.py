#6. Print all even numbers between 1 and 100 using a for loop


class Solution:
    def print_even(self):
        for i in range(2,100):
            if i%2==0:
                print(i,end=" ")
s=Solution()
s.print_even()
