#. Write a Python program to find the second largest number in a list without using the sort() method.
#lst=[1,3,6,9,2]    #6
import heapq
class Solution:
    def nth_largest(self,lst):
        min_heap=[]
        for num in lst:
            heapq.heappush(min_heap,num)
            if len(min_heap)>2:
                heapq.heappop(min_heap)
        return min_heap[0]

        

s=Solution()
s.nth_largest([1,3,6,9,2])
