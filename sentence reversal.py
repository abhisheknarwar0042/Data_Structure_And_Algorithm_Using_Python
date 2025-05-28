class Solution:
    def sentence_reversal(self, s: str) -> str:
        return ' '.join(s.split()[::-1]) 

s = Solution()
result = s.sentence_reversal("somesh is good boy")
print(result)  
