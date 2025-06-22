#Create a program to check if a number is prime
#means number divide by itself or 1----count of numbers is only 2 numbers 
class Solution:
    def is_prime(self, lst):
        for num in lst:
            if num <= 1:
                print(num, "is not a prime number")
                continue
            
            count = 0
            for i in range(1, num + 1):
                if num % i == 0:
                    count += 1

            if count == 2:
                print(num, "is a prime number")
            else:
                print(num, "is not a prime number")

lst = [1, 3, 5, 7]
s = Solution()
s.is_prime(lst)






