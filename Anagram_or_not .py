class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.replace(" ","").lower()
        t=t.replace(" ","").lower()


        
        if len(s)!=len(t):
            return False

        count={}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for j in t:
            if j in count:
                count[j]-=1
            else:
                count[j]=1
        for k in count:
           if count[k]!=0:
            return False
        return True
s=Solution()
s.isAnagram('dog','god')

        
