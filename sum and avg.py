# Find the sum and average of a list of numbers.
class Solution:
    def sum(self,lst):
        sum=0
        for number in lst:
            sum+=number
        return sum
    def avg(self,lst):
        return sum(lst)/len(lst)

s=Solution()
print(s.sum([1,2,3,4,5,6]))#21
print(s.avg([1,2,3,4,5,6]))#3.5
    
            
            
