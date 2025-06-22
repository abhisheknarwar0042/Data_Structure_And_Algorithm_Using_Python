#Count the number of vowels, consonants, digits, and special characters in a given string
#str="abhishek@.#123"
#isdigit() function to check digit
#isalpha() function to check alphabets  

class Solution:
    def digit_count(self,str):
        count=0
        for i in str:
            if i.isdigit():
                count+=1
        return count
    def vowels_count(self,str):
        count=0
        vowels='aeiouAEIOU'
        for i in str:
            if i in vowels :
                count+=1
        return count
    def constants_counts(self,str):
        count=0
        for i in str:
            if i.isalpha() and i not in 'aeiouAEIOU':
                count+=1
        return count
    def special_char_count(self,str):
        count=0
        special_char='.#@!'
        for i in str:
            if i in special_char:
                count+=1
        return count
str="abhishek@.#123"
s=Solution()
print('digit_count:',s.digit_count(str))
print('vowels_count:',s.vowels_count(str))
print('constants_count:',s.constants_counts(str))
print('special_char_count:',s.special_char_count(str))

#output:::
'''Digits: 3
Vowels: 3
Consonants: 5
Special Characters: 3
'''

       
        


    
