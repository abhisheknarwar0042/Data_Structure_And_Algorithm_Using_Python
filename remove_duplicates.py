#. Remove duplicates from a list without using set() and return it in sorted order

#lst=[1,9,2,8,2,1]    #[1,2,8,9]

class Solution:
    def remove_duplicate(self,lst):
        list=[]
        for i in lst:
            if i not in list:
                list.append(i)
        return sorted(list)
        
s=Solution()
print(s.remove_duplicate([1,9,2,8,2,1]))

